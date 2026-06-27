# chat.py

import gradio as gr
from agent import Me
from style import get_footer_html, get_header_html, get_initial_message, get_profile

me = Me()

PROFILE = get_profile()
HEADER_HTML = get_header_html()
INITIAL_MESSAGE = get_initial_message()
FOOTER_HTML = get_footer_html()

FAVICON_URL = PROFILE["avatar_url"]


def user_submit(message, history):
    history = history + [{"role": "user", "content": message}]
    return "", history


def bot_reply(history):
    last_user_msg = history[-1]["content"]
    chat_history = history[:-1]
    response = me.chat(last_user_msg, chat_history)
    history = history + [{"role": "assistant", "content": response}]
    return history


def build_chat(css: str) -> gr.Blocks:
    with gr.Blocks(
        title="Godwill Alexis AGUEMON — Digital Twin",
        css=css,
        theme=gr.themes.Base(
            primary_hue="purple",
            neutral_hue="slate",
            font=["Space Grotesk", "sans-serif"],
        ),
        head=f'<link rel="icon" type="image/svg+xml" href="{FAVICON_URL}">',
    ) as demo:

        gr.HTML(HEADER_HTML)

        chatbot = gr.Chatbot(
            value=INITIAL_MESSAGE,
            elem_id="chatbot",
            height=460,
            show_label=False,
            avatar_images=(None, PROFILE["avatar_url"]),
        )

        with gr.Row():
            msg = gr.Textbox(
                elem_id="msg-input",
                placeholder="Pose une question à Godwill…",
                show_label=False,
                scale=8,
                lines=1,
                max_lines=4,
                container=False,
            )
            send_btn = gr.Button("Envoyer →", variant="primary", scale=1, min_width=110)
            clear_btn = gr.Button("Effacer", variant="secondary", scale=1, min_width=80)

        gr.HTML(FOOTER_HTML)

        msg.submit(user_submit, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot_reply, chatbot, chatbot
        )
        send_btn.click(user_submit, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot_reply, chatbot, chatbot
        )
        clear_btn.click(lambda: INITIAL_MESSAGE, None, chatbot, queue=False)

    return demo