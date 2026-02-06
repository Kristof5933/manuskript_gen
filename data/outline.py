#!/usr/bin/env python
# --!-- coding: utf8 --!--

from __future__ import annotations
import os
from config import Config
from util import safeFilename, formatNumber
from util.fakeService import FakeService
from dataclasses import dataclass, field, fields
from typing import ClassVar
from data.abstractMmd import AbstractMmd
from data.abstractData import AbstractData
from data.characters import Character, Characters
from data.status import Status
from data.labels import Labels
from util.references import References

@dataclass
class OutlineItem(AbstractData):
    LEVEL_TITLES: ClassVar[tuple[str, ...]] = ('Scene', 'Chapter', 'Section', 'Book', 'Arc', 'Saga', 'Universe')

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
        self.config = config
        self.items: list[OutlineItem] = []

    def generateNextLevel(self, level: int, references: References, uniqueID:int):

        for i in range(1, self.config.sectionsQuantity+1):
            if level == 1:
                text = OutlineText(self.dataPath, self.config, self.outline, i, uniqueID, OutlineItem.LEVEL_TITLES[level-1])
                references.addOutlineItem(text.ID, text.title)
                self.items.append(text)
                uniqueID+=1
            else:
                folder = OutlineFolder(self.dataPath, self.config, self.outline, i, uniqueID, OutlineItem.LEVEL_TITLES[level-1])                
                references.addOutlineItem(folder.ID, folder.title)
                uniqueID = folder.generateNextLevel(level - 1, references, uniqueID+1)
                self.items.append(folder)

        return uniqueID

@dataclass
class OulineFolderDescriptor(AbstractMmd):
    title: str = None
    ID: int = None 
    type: str = None
    compile: int = None
    charCount: int = None

    def __init__(self, dataPath: str, title: str, ID: int, charCount: int):
        AbstractMmd.__init__(self, os.path.join(dataPath, "folder.txt"))
        self.ID = ID
        self.charCount = charCount
        self.title = title
        self.compile = 2
        self.type = "folder"


@dataclass
class OutlineFolder(OutlineItem):
    def __init__(self, dataPath: str, config: Config, outline: Outline, itemNumber:int, ID: int, levelTitle: str):

        OutlineItem.__init__(self, dataPath, config, ID, outline)
        self.type = 'folder'
        self.title = f"{levelTitle} {itemNumber}"

        self.folderPath = os.path.join(dataPath,safeFilename(f"{formatNumber(itemNumber, config.sectionsQuantity)}-{self.title}"))
        self._changePath(self.folderPath)
        
        self.folderDescriptor = OulineFolderDescriptor(self.folderPath, self.title, self.ID, 777)

    def save(self):
        os.makedirs(self.folderPath, exist_ok=True)
        OutlineItem.save(self)

        self.folderDescriptor.save()

        for item in self.items:
            item.save()


@dataclass
class OutlineText(OutlineItem, AbstractMmd):
    summarySentence: str = None
    summaryFull: str = None
    POV: int = None
    label: int = None
    status: int = None
    setGoal: int = None
    charCount: int = None

    def __init__(self, dataPath: str, config: Config, outline: Outline, itemNumber:int, ID: int, levelTitle: str):
        OutlineItem.__init__(self, dataPath, config, ID, outline)
        AbstractMmd.__init__(self, dataPath)
        fakeService = FakeService()

        self.type = 'md'
        self.title = f"{levelTitle} {itemNumber}"
        self.summarySentence = fakeService.words(10)
        self.summaryFull = fakeService.markdown(1)
        self.POV = self.outline.characters.getRandomPOVId()
        self.label = self.outline.labels.getRandomLabelById()
        self.status = self.outline.status.getRandomStatusID()
        
        self.body = fakeService.markdown(config.sectionsParagraphs, False)
        wordCount = len(self.body.split())
        self.charCount = wordCount
        self.setGoal = fakeService.int(int(wordCount * 0.5), int(wordCount * 1.5))

        # TODO : generate notes

        self._changePath(os.path.join(dataPath,safeFilename(f"{formatNumber(itemNumber, config.sectionsQuantity)}-{self.title}", "md")))

    def save(self):
        AbstractMmd.save(self)
        for item in self.items:
            item.save()

@dataclass
class Outline(OutlineItem):

    def __init__(self, dataPath: str, config: Config, status: Status, characters: Characters, labels: Labels, references: References):
        OutlineItem.__init__(self, os.path.join(dataPath, "outline"), config, 1, self)

        self.status = status
        self.characters = characters
        self.labels = labels

        self.generateNextLevel(config.sectionsLevels, references, 1)

    def save(self):
        os.makedirs(self.dataPath, exist_ok=True)
        for item in self.items:
            item.save()