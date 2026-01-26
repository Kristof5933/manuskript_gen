import json
from pathlib import Path

class Config:
    def __init__(self, data: dict):
        labels = data.get("labels", {})
        self.labelsQuantity: int = labels.get("quantity", 0)

        characters = data.get("characters", {})
        self.charactersQuantity: int = characters.get("quantity", 0)

        plots = data.get("plots", {})
        self.plotsQuantity: int = plots.get("quantity", 0)

        world = data.get("world", {})
        self.worldQuantity: int = world.get("quantity", 0)
        self.worldLevels: int = world.get("levels", 0)

        sections = data.get("sections", {})
        self.sectionsQuantity: int = sections.get("quantity", 0)
        self.sectionsLevels: int = sections.get("levels", 0)
        self.sectionsParagraphs: int = sections.get("paragraphs", 0)
        self.sectionsRevisions: int = sections.get("revisions", 0)

class ConfigLoader:
    _instance = None
        
    def __new__(cls, jsonPath=None):
        if cls._instance is None:
            if jsonPath is None:
                raise ValueError("JSON file must be specified")
            cls._instance = super().__new__(cls)
            cls._instance._init(jsonPath)
        return cls._instance
    
    def loadConfig(self, profileName: str) -> Config:
        if profileName not in self._data:
            raise KeyError(f"Unkown profile : {profileName}")
        
        self.currentConfig = Config(self._data[profileName])
        return self.currentConfig

    def _init(self, json_path: str):
        self.jsonPath: Path = Path(json_path)
        self.currentConfig: Config = None

        if not self.jsonPath.exists():
            raise FileNotFoundError(f"Config file can't be found : {json_path}")
        
        with open(self.jsonPath, "r", encoding="utf-8") as f:
            self._data = json.load(f)
        
    def reload(self, profileName: str):
        self._loadConfig(profileName)

    def getCurrentConfiguration(self) -> Config:
        return self.currentConfig

    def listAvailableConfigurations(self):
        return [
            (key, value.get("title"))
            for key, value in self._data.items()
        ]