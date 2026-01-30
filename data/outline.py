#!/usr/bin/env python
# --!-- coding: utf8 --!--

from __future__ import annotations
import os
from config import Config
from util import safeFilename, FakeService
from dataclasses import dataclass, field, fields
from data.abstractMmd import AbstractMmd
from data.abstractData import AbstractData
from data.characters import Character, Characters
from data.status import Status
from data.labels import Labels

@dataclass
class OutlineItem(AbstractData):
    title: str = None
    ID: int = None
    type: str = None
    compile: int = None
    charCount: int = None

    def __init__(self, dataPath: str, config: Config, ID: int, outline: Outline):
        AbstractData.__init__(self, dataPath)
        self.outline = outline
        self.ID = ID
        self.compile = 2

@dataclass
class OutlineFolder(OutlineItem):
#    levelTitles: list[str] = ['Universe', 'Saga', 'Arc', 'Book', 'Section', 'Chapter', 'Scene']
    def __init__(self, dataPath: str, config: Config, outline: Outline):
        OutlineItem.__init__(self, dataPath, 0, outline)
        self.type = 'folder'

@dataclass
class OutlineText(OutlineItem, AbstractMmd):
    summarySentence: str = None
    summaryFull: str = None
    #POV: Character
    POV: int = None
    label: int = None
    status: int = None
    setGoal: int = None
    charCount: int = None

    def __init__(self, dataPath: str, config: Config, outline: Outline, ID: int):
        OutlineItem.__init__(self, dataPath, config, 0, outline)
        AbstractMmd.__init__(self, dataPath)
        fakeService = FakeService()

        self.ID = ID
        self.type = 'md'
        self.title = f"Scene {self.ID}"
        self.summarySentence = fakeService.words(10)
        self.summaryFull = fakeService.markdown(1)
        self.POV = self.outline.characters.getRandomPOVId()
        self.label = self.outline.labels.getRandomLabelById()
        self.status = self.outline.status.getRandomStatusID()
        self.setGoal = 100
        self.charCount = 50

        self._changePath(os.path.join(dataPath,safeFilename(f"{self.ID}-{self.title}", "md")))

@dataclass
class Outline(AbstractData):

    def __init__(self, dataPath: str, config: Config, status: Status, characters: Characters, labels: Labels):
        AbstractData.__init__(self, os.path.join(dataPath, "outline"))
        self.items: list[OutlineItem] = []

        self.status = status
        self.characters = characters
        self.labels = labels

        for i in range(config.sectionsQuantity):
            self.items.append(OutlineText(self.dataPath, config, self, i))

    def save(self):
        os.makedirs(self.dataPath, exist_ok=True)
        for item in self.items:
            item.save()