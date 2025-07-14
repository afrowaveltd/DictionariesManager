import json
import locale
from pathlib import Path

class LocalizationService:
    def __init__(self, lang: str, path: Path = Path("./locales")):
        print(Path.home())
        self.path = path
        self.language = self._detect_language(lang)
        self._cache = {}

    def _detect_language(self, lang: str) -> str:
        if lang.lower() == "auto":
            lang_code, _ = locale.getdefaultlocale()
            return lang_code.split("_")[0] if lang_code else "en"
        return lang

    def _load(self) -> dict:
        if self.language in self._cache:
            return self._cache[self.language]

        file_path = self.path / f"{self.language}.json"
        this_path = Path.cwd()
        print(this_path)
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}

        self._cache[self.language] = data
        return data

    def get(self, key: str) -> str:
        return self._load().get(key, key)