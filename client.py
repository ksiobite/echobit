from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Header, Input, Log, Static

class MessengerApp(App):
    CSS = """
    Screen {
        layout: vertical;
    }

    #main-container {
        layout: horizontal;
        height: 1fr;
    }

    #sidebar {
        width: 25%;
        border: solid green;
        background: #111111;
    }

    #chat-area {
        width: 80%;
        layout: vertical;
        border: solid blue;
    }

    #user-panel {
        width: 20%;
        border: solid yellow;
        padding: 1;
    }

    #chat-log {
        height: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Horizontal(id='main-container'):
            with Vertical(id='sidebar'):
                yield Static(" Users:\n ")

            with Vertical(id='chat-area'):
                yield Log(id="chat-log")

                yield Input(placeholder="Enter Message: ", id="message-input")

                yield Button("Send", variant="primary", id="send-btn")
        yield Footer()

    @on(Button.Pressed, '#send-btn')
    @on(Input.Submitted, '#message-input')
    def handle_send(self) -> None:
        user_input = self.query_one('#message-input', Input)
        chat_log = self.query_one('#chat-log', Log)

        text = user_input.value.strip()
        if text:
            chat_log.write(f'you: {text}')
            user_input.value = ''


app = MessengerApp()
app.run()
