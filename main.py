from textual.app import App, ComposeResult
from textual.widgets import Label
from src.services.settings_service import Settings
from src.services.localization_service import LocalizationService

class DictionariesManager(App):
    CSS_PATH = "themes/theme_dark.css"

    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.t = LocalizationService(self.settings.language)

    def compose(self) -> ComposeResult:
        yield Label(self.t.get("hello"))

if __name__ == '__main__':
    app = DictionariesManager()
    app.run()