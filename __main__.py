bl_info = {
    "name": "Ollama API Client",
    "blender": (4, 0, 0),
    "category": "3D View",
}

import bpy
import requests
import threading

class OLLAMA_PT_Panel(bpy.types.Panel):
    bl_label = "Ollama API Client"
    bl_idname = "OLLAMA_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Ollama API'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        ollama_props = scene.ollama_props

        layout.prop(ollama_props, "input_text")
        layout.operator("ollama.submit", text="Submit")
        layout.prop(ollama_props, "output_text", text="Response")

class OLLAMA_OT_Submit(bpy.types.Operator):
    bl_idname = "ollama.submit"
    bl_label = "Submit"

    def execute(self, context):
        scene = context.scene
        ollama_props = scene.ollama_props

        # Run the request in a separate thread
        thread = threading.Thread(target=self.send_request, args=(ollama_props.input_text, context))
        thread.start()

        return {'FINISHED'}

    def send_request(self, prompt, context):
        url = "http://localhost:11434/api/generate"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama3:70b",
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                result = response.json().get("response", "No response field found in API response.")
                update_output_text()
            else:
                result = f"Error {response.status_code}: {response.text}"
        except requests.RequestException as e:
            result = f"Request failed: {e}"

        # Update the output text in the main thread
        def update_output_text():
            context.scene.ollama_props.output_text = result

        # bpy.app.driver_namespace['update_output_text'] = update_output_text
        # bpy.app.timers.register(bpy.app.driver_namespace['update_output_text'])

class OLLAMA_Props(bpy.types.PropertyGroup):
    input_text: bpy.props.StringProperty(
        name="Input Text",
        description="Enter the text to send to the Ollama API",
        default=""
    )
    output_text: bpy.props.StringProperty(
        name="Output Text",
        description="Response from the Ollama API",
        default=""
    )

def register():
    bpy.utils.register_class(OLLAMA_PT_Panel)
    bpy.utils.register_class(OLLAMA_OT_Submit)
    bpy.utils.register_class(OLLAMA_Props)
    bpy.types.Scene.ollama_props = bpy.props.PointerProperty(type=OLLAMA_Props)

def unregister():
    bpy.utils.unregister_class(OLLAMA_PT_Panel)
    bpy.utils.unregister_class(OLLAMA_OT_Submit)
    bpy.utils.unregister_class(OLLAMA_Props)
    del bpy.types.Scene.ollama_props

if __name__ == "__main__":
    register()
