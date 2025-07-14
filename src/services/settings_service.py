import json
from pathlib import Path

class Settings:
    def __init__(self, file_path: Path = Path("./settings.json")):
        self.file_path = file_path
        self._data = self._load()

    def _load(self) -> dict:
        if not self.file_path.exists():
            raise FileNotFoundError(self.file_path)
        with open(self.file_path) as json_file:
            return json.load(json_file)

    def get(self, key: str, default= None):
        return self._data.get(key, default)

    @property
    def language(self) -> str:
        return self.get("language", "en")

    @property
    def theme(self) -> str:
        return self.get("theme", "dark")

    @property
    def translate_settings(self) -> dict:
        return self._data.get("translate", {})