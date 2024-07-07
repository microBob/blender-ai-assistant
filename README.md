# Blender AI Assistant

A Blender add-on that utilizes LLMs to create.

Use plain english to describe actions in Blender and an LLM (Llama 3 70b) perform the task for you in Blender.

[📺 Demo Video](https://youtu.be/z2ceCeu7Imw)

# Usage
[Ollama](https://ollama.com/) needs to be running and available at `http://localhost:11434`

1. Download [`ai_assistant.py`](https://github.com/microBob/amd-pervasive-ai/blob/main/ai_assistant.py)
2. From Blender, press Preferences > Add-ons > Install and select `ai_assistant.py`
3. Enable the add-on
4. From the side bar (<kbd>n</kbd>) go to the "AI Assistant tab"
5. Type instructions into the text box and press submit.

The add-on will use Ollama and Llama 3 70b to perform inference. If this is your first time using Ollama and Llama 3 70b the first command will take a long time to execute since Ollama needs to install and initialize Llama 3.

The add-on also will allow Ollama to automatically release the model from GPU memory after 5 minutes of inactivity. Expect delays after trying to make a call to it after 5 minutes.