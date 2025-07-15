from textual.app import App, ComposeResult
from textual.widgets import Label, Header, Footer
from src.services.settings_service import Settings
from src.services.localization_service import LocalizationService

class DictionariesManager(App):
    CSS_PATH = "themes/theme_dark.css"
    t = LocalizationService(Settings().language)
    BINDINGS = [("d", "toggle_dark", t.get("Toggle dark mode"))]

    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.t = LocalizationService(self.settings.language)
        self.title = "Afrowave " + self.t.get("Dictionaries Manager")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )    

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Label(self.t.get("hello"))
        yield Footer()

if __name__ == '__main__':
    t = LocalizationService(Settings().language)
    app = DictionariesManager()
    app.run()