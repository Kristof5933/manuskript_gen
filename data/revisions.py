#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
import random
from config import Config
from util import safeFilename
from util.fakeService import FakeService
from dataclasses import dataclass, field, fields
from data.abstractXml import AbstractXml
from data.outline import Outline, OutlineFolder, OutlineText, OutlineItem

@dataclass
class RevisionItem(AbstractXml):
    def copyOutlineElement(self, outline: OutlineItem):
        for item in outline.items:
            if type(item) is OutlineFolder:
                self.addChild(RevisionFolder(self.dataPath, item))
            else:
                self.addChild(RevisionText(self.dataPath, item))


@dataclass 
class RevisionFolder(RevisionItem):
    title: str = None
    ID: int = None
    type: str = None
    compile: int = None
    lastPath: str = None

    def __init__(self, dataPath: str, outlineFolder: OutlineFolder):
        AbstractXml.__init__(self)

        self.nodeName = "outlineItem"
        self.title = outlineFolder.title
        self.ID = outlineFolder.ID
        self.type = "folder"
        self.compile = 2
        self.lastPath = outlineFolder.dataPath

        self.copyOutlineElement(outlineFolder)

@dataclass
class RevisionEntry(AbstractXml):
    timestamp: int = None
    text: str = None

    def __init__(self, originalText: str, iteration: int):
        AbstractXml.__init__(self)
        self.nodeName = "revision" 
        self.text = originalText[:random.randint(0, len(originalText))] 
        self.timestamp = 1765097721 + iteration * 6548


@dataclass 
class RevisionText(RevisionItem):
    title: str = None
    ID: int = None
    type: str = None
    summaryFull: str = None
    POV: int = None
    notes: str = None
    label: int = None
    status: int = None
    compile: int = None
    text: str = None
    setGoal: int = None
    lastPath: str = None

    def __init__(self, dataPath: str, outlineText: OutlineText):
        AbstractXml.__init__(self)

        self.nodeName = "outlineItem"
        self.title = outlineText.title
        self.ID = outlineText.ID
        self.type = "md"
        self.summaryFull = outlineText.summaryFull
        self.POV = outlineText.POV

        # TODO: missing notes
        self.notes = "To be implemented"
        self.label = outlineText.label
        self.status = outlineText.status
        self.compile = outlineText.compile
        self.text = outlineText.body
        self.setGoal = outlineText.setGoal        
        self.lastPath = outlineText.dataPath

        for i in range(5):
            self.addChild(RevisionEntry(self.text, i))

@dataclass 
class Revisions(RevisionFolder):

    def __init__(self, dataPath: str, config: Config, outline: Outline):
        AbstractXml.__init__(self)
        self.dataPath = os.path.join(dataPath, "revisions.xml")
        self.config = config
        self.nodeName = "outlineItem"
        self.title = "root"
        self.ID = 0
        self.type = "folder"
        self.compile = 2
        self.lastPath = ""

        if not config.sectionsRevisions:
            return
        
        self.copyOutlineElement(outline)
        
    def save(self):
        if self.config.sectionsRevisions:
            AbstractXml.save(self)

