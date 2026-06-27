# main.py

import gradio as gr
from chat import build_chat
from style import get_css

if __name__ == "__main__":
    app = build_chat(css=get_css())
    app.launch()