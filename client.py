from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Header, Input, Log, Static

class echobit(App):
    CSS ="""
    Screen {
        background: #0d0d0d;
        color: #00ff66;
    }

    Header {
        background: #1a1a1a;
        color: #00ff66;
        text-style: bold;
    }

    /* лог */
    Log {
        height: 1fr;
        background: #080808;
        color: #e0e0e0;
        border: dashed #333333;
    }

    /* =========================================== */

    /* контейнер(чат + юзер) */
    #main-container {
        layout: horizontal;
        height: 1fr;
    }

    /* чат */
    #chat-area {
        width: 5fr;
        layout: vertical;
        padding: 1;
        border: solid #00ff66;
        background: #121212;
    }

    /* юзеры  */
    #sidebar {
        width: 1fr;
        border: solid #00aa44;
        background: #121212;
        padding: 1;
    }

    /* ============================================ */

    /* контейнер ввода (поле ввода + кнопка отправки) */
    #input-container {
        height: 5;
        margin-top: 1;
        padding: 0;
    }

    /* поле ввода */
    Input {
        width: 1fr;
        height: 3;
        background: #1a1a1a;
        min-width: 10;
        border: solid #00ff66;
        color: #ffffff;
        background: transparent;
    }

    /* кнопка отправки */
    Button {
        width: 12;
        height: 3;
        margin-left: 0;
        background: #00ff66;
        color: #000000;
        text-style: bold;
    }

    /* =========================================== */

    Button:hover {
        background: #00cc52;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Horizontal(id='main-container'):
            with Vertical(id='sidebar'):
                yield Static(" Users:\n ")

            with Vertical(id="chat-area"):
                yield Log(id="chat-log")

                with Horizontal(id="input-container"):
                    yield Input(
                        placeholder="Enter Message:",
                        id="message-input"
                    )
                    yield Button("Send",
                        variant="primary",
                        id="send-btn"
                    )
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


app = echobit()
app.run()
