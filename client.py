from curses import echo

from textual import screen
from textual.screen import Screen
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Header, Input, Log, Static

class Login(Screen):
    def compose(self) -> ComposeResult:
        with Vertical(id="login-container"):
            yield Static("echobit | Alpha version by ksio")
            yield Input(placeholder="Enter your name", id="nick-input")
            yield Input(placeholder="Ip server", id="ip-server")
            yield Input(placeholder="Port server", id="port-server")
            yield Button("join", variant="primary", id="login-btn")

    @on(Button.Pressed, "#login-btn")
    @on(Input.Submitted, "#nick-input")
    def handle_login(self) -> None:
        nick_input = self.query_one("#nick-input", Input)
        nickname = nick_input.value.strip()
        if nickname:
            self.app.current_user = nickname
            self.app.switch_screen("chat")

class Messenger(Screen):
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

        yield Footer()

    @on(Input.Submitted, '#message-input')
    def handle_send(self) -> None:
        user_input = self.query_one('#message-input', Input)
        chat_log = self.query_one('#chat-log', Log)

        text = user_input.value.strip()
        if text:
            chat_log.write(f'{self.app.current_user}: {text}\n')
            user_input.value = ''

class echobit(App):
    CSS_PATH = "style.css"

    SCREENS = {
        "login": Login,
        "chat": Messenger,
    }

    def on_mount(self) -> None:
        self.current_user = "Elliot"
        self.push_screen("login")

app = echobit()
app.run()
