#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
import random
from config import Config
from data.abstractMmd import AbstractMmd
from data.abstractData import AbstractData
from util.references import References
from util.fakeService import FakeService
from util import safeFilename
from dataclasses import dataclass, field, fields

@dataclass(init=False)
class Character(AbstractMmd):
    # caution: property name case corresponds to file output case
    Name: str
    ID: int
    Importance: int 
    POV: bool 
    Motivation: str
    Goal: str
    Conflict: str
    Epiphany: str
    Notes: str
    Color: str

    def __init__(self, dataPath: str, ID: int):
        AbstractMmd.__init__(self)
        fakeService = FakeService()
        self.metaSpacing = 21
        
        self.Name = fakeService.name()
        self.ID = ID
        self.Importance = fakeService.int(0, 2)
        self.POV = fakeService.boolean(chance_of_getting_true=25)
        self.Motivation = fakeService.markdown(2)
        self.Goal = fakeService.markdown(2)
        self.Conflict = fakeService.markdown(2)
        self.Epiphany = fakeService.markdown(2)
        self.additionalProperties["Phrase Summary"] = fakeService.words(20)
        self.additionalProperties["Paragraph Summary"] = fakeService.words(2)
        self.additionalProperties["Full Summary"] = fakeService.markdown(2)
        self.Notes: str = fakeService.markdown(2)
        self.Color: str = fakeService.color()

        for i in range(5):
            self.additionalProperties[fakeService.words(3)] = fakeService.words(5)

        self._changePath(os.path.join(dataPath,safeFilename(f"{self.ID}-{self.Name}", "txt")))

class Characters(AbstractData):
    def __init__(self, dataPath: str, config: Config, references: References):
        AbstractData.__init__(self,os.path.join(dataPath, "characters"))

        self.characters: list[Character] = []
        for i in range(config.charactersQuantity):
            character = Character(self.dataPath, i)
            self.characters.append(character)
            references.addCharacterItem(character.ID, character.Name)

        self.charactersWithPOV: list[Character] = [item for item in self.characters if item.POV == 1]

    def getRandomPOVId(self):
        if len(self.charactersWithPOV) > 0:
            POV = random.choice(self.charactersWithPOV)
            return POV.ID
        else:
            return None

    def getRandomCharactersId(self):
        if len(self.characters) > 0:
            result = set()

            for i in range(random.randint(0, len(self.characters) // 5)):

                result.add(random.choice(self.characters).ID)
            
            return list(result)
        else:
            return None


    def save(self):
        os.makedirs(self.dataPath, exist_ok=True)
        for character in self.characters:
            character.save()

