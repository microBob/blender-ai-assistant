bl_info = {
    "name": "AI Assistant",
    "author": "Kenneth Y (Microbob)",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "3D View",
}

import bpy
import requests
import threading
import traceback
import functools


result = ""


class ASSISTANT_PT_Panel(bpy.types.Panel):
    bl_label = "AI Assistant"
    bl_idname = "ASSISTANT_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AI Assistant"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        assistant_props = scene.assistant_props

        layout.prop(assistant_props, "input_text")
        layout.operator(
            "assistant.submit",
            text="Generating" if assistant_props.is_generating else "Submit",
            emboss=not assistant_props.is_generating,
        )
        layout.label(text="Response:")
        for line in assistant_props.output_text.split("\n"):
            layout.label(text=line)


def send_request(prompt, system, flag):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3:70b",
        "prompt": prompt,
        "stream": False,
        "system": system,
        "keep_alive": -1,
    }

    global result

    try:
        response = requests.post(url, headers=headers, json=data)
    except requests.RequestException as e:
        result = f"Request failed: {e}"
    else:
        if response.status_code == 200:
            result = response.json().get("response", "NO RESULT")

            if result == "NO RESULT":
                flag.set()
                raise ValueError("No result field found in API call.")
        else:
            result = f"Error {response.status_code}: {response.text}"
            flag.set()
            return

        # Extract code fragment.
        try:
            start_of_fragment_index = result.index("```")
        except ValueError:
            # Show response if no code.
            flag.set()
        else:
            end_of_fragment_index = (
                result[start_of_fragment_index + 3 :].index("```")
                + start_of_fragment_index
                + 3
            )
            code = result[start_of_fragment_index + 3 : end_of_fragment_index]

            # Try to run the command
            try:
                exec(code)
            except Exception:
                # Get the error and request a fix.
                error = traceback.format_exc()
                print(error)

                # Recurse with new prompt and setup.
                send_request(
                    f"Command: {prompt}\nError: {error}",
                    "You are a programming assistant for Blender 3D's Python API. I will give you a Blender Python command and the associated error it produced. Fix the command with the correct Blender Python code and place it between three tick marks like this '```'. Do not explain your answer. No need to import bpy. If a command is not possible, respond with `not possible` and a one sentence description of why. If my question is not related to Blender, respond with `not possible` and a one sentence description of why.",
                    flag,
                )
            else:
                # On successful exec.
                flag.set()


class ASSISTANT_OT_Submit(bpy.types.Operator):
    bl_idname = "assistant.submit"
    bl_label = "Submit"

    def execute(self, context):
        scene = context.scene
        assistant_props = scene.assistant_props

        # Skip if already generating.
        if assistant_props.is_generating:
            return {"FINISHED"}

        assistant_props.is_generating = True

        # Run the request in a separate thread.
        thread_flag = threading.Event()
        thread = threading.Thread(
            target=send_request,
            args=(
                assistant_props.input_text,
                "You are a programming assistant for Blender 3D's Python API. I will ask you to perform actions in Blender and you will respond with the corresponding Blender Python commands surrounded by three tick marks like this '```'. Do not explain your answer. No need to import bpy. If a command is not possible, respond with `not possible` and a one sentence description of why. If my question is not related to Blender, respond with `not possible` and a one sentence description of why.",
                thread_flag,
            ),
        )
        thread.start()

        check_thread = functools.partial(self.update_scene, context, thread_flag)
        bpy.app.timers.register(check_thread)

        return {"FINISHED"}

    def update_scene(self, context, flag):
        if flag.is_set():
            global result

            context.scene.assistant_props.is_generating = False
            context.scene.assistant_props.output_text = result

            # Reset after using it.
            result = ""

            return None  # Return None to indicate the callback should not be repeated
        return 0.1


class ASSISTANT_Props(bpy.types.PropertyGroup):
    input_text: bpy.props.StringProperty(
        name="Input Text", description="Describe what you'd like to do", default=""
    )
    output_text: bpy.props.StringProperty(
        name="Output Text", description="Response from the assistant", default=""
    )
    is_generating: bpy.props.BoolProperty(
        name="Is Generating",
        description="Indicates whether the assistant is generating a response",
        default=False,
    )


def register():
    bpy.utils.register_class(ASSISTANT_PT_Panel)
    bpy.utils.register_class(ASSISTANT_OT_Submit)
    bpy.utils.register_class(ASSISTANT_Props)
    bpy.types.Scene.assistant_props = bpy.props.PointerProperty(type=ASSISTANT_Props)


def unregister():
    bpy.utils.unregister_class(ASSISTANT_PT_Panel)
    bpy.utils.unregister_class(ASSISTANT_OT_Submit)
    bpy.utils.unregister_class(ASSISTANT_Props)
    del bpy.types.Scene.assistant_props


if __name__ == "__main__":
    register()
