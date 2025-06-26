import gradio as gr
from main import generate, prepare_prompt
from typing import Iterator
import re


def extract_final_answer(text: str) -> str:
    # use regular expression to match \boxed{...} content
    match = re.search(r'\\boxed{([^}]*)}', text)
    if match:
        return match.group(1)
    return "Final answer not found"


def process_question_stream(question: str, history: list = None) -> Iterator[tuple[str, str]]:
    completions = generate([prepare_prompt(question, history)])
    full_response = completions[0][0]

    # simulate stream output
    words = full_response.split()
    current_text = ""

    for word in words:
        current_text += word + " "
        yield current_text, extract_final_answer(current_text)


def create_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Satori-7B Math Problem Solver")

        chatbot = gr.Chatbot(
            label="Chat History",
            height=400,
            show_label=True,
        )

        with gr.Row():
            with gr.Column(scale=4):
                question_input = gr.Textbox(
                    label="Enter a math problem",
                    placeholder="e.g., Which number is larger? 9.11 or 9.9?",
                    lines=2
                )
            with gr.Column(scale=1):
                submit_btn = gr.Button("Submit", variant="primary")

        final_answer = gr.Textbox(
            label="Reasoning Process",
            lines=10,
            interactive=False
        )

        def user_input(user_message: str, history: list) -> tuple[str, list]:
            return "", history + [[user_message, None]]

        def bot_response(history: list) -> tuple[list, str]:
            # Get the conversation history except the last question
            chat_history = history[:-1] if len(history) > 1 else None
            for response, answer in process_question_stream(history[-1][0], chat_history):
                history[-1][1] = answer  # Show only the last answer in the conversation history
                yield history, response  # Output the reasoning process to the original final answer box

        question_input.submit(user_input, [question_input, chatbot], [question_input, chatbot]).then(
            bot_response, chatbot, [chatbot, final_answer]
        )

        submit_btn.click(user_input, [question_input, chatbot], [question_input, chatbot]).then(
            bot_response, chatbot, [chatbot, final_answer]
        )

    return demo


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Launch Satori-7B Math Problem Solver')
    parser.add_argument('--share', action='store_true',
                        help='Whether to allow public network access (only local access is allowed by default)')
    parser.add_argument('--host', type=str, default='127.0.0.1',
                        help='Server listening address (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=7860,
                        help='Server listening port (default: 7860)')
    args = parser.parse_args()

    demo = create_interface()
    demo.queue()
    demo.launch(share=args.share,
                server_name=args.host,
                server_port=args.port)
