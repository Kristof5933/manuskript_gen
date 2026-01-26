from util import FakeService
from config import Config

class CharacterProperty:
    def __init__(self, fakeService: FakeService):
        self.propertyName: str= fakeService.words(3)
        self.propertyValue: str = fakeService.words(5)

class Character:
    def __init__(self, ID: int):
        fakeService = FakeService()
        self.name: str = fakeService.name()
        self.ID: int = ID
        self.importance: int = fakeService.int(0, 2)
        self.POV: bool = fakeService.boolean(chance_of_getting_true=25)
        self.motivation: str = fakeService.markdown(2)
        self.goal: str = fakeService.markdown(2)
        self.conflict: str = fakeService.markdown(2)
        self.epiphany: str = fakeService.markdown(2)
        self.phraseSummary: str = fakeService.words(20)
        self.paragraphSummary: str = fakeService.markdown(2)
        self.fullSummary: str = fakeService.markdown(5)
        self.notes: str = fakeService.markdown(2)
        self.color: str = fakeService.color()

        self.additionalProperties = []

        for i in range(5):
            self.additionalProperties.append(CharacterProperty(fakeService))

class Characters:
    def __init__(self, config: Config):
        self.characters: list[Character] = []
        for i in range(config.charactersQuantity):
            self.characters.append(Character(i))

    def debug(self):
        for character in self.characters:
            print(f"{character.ID} = {character.name}")

