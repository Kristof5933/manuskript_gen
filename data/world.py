#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
from config import Config
from util import safeFilename, FakeService
from dataclasses import dataclass, field, fields
from data.abstractXml import AbstractXml

@dataclass
class WorldBody(AbstractXml):
    def __init__(self, config: Config):
        AbstractXml.__init__(self)
        self.config = config
        self.nodeName = "body"
        self.ID=0
        self.fakeService = FakeService()

        for i in range(config.worldQuantity):
            self.addChild(WorldOutline(config, self))

@dataclass
class World(AbstractXml):
    version: str = "1.0"

    def __init__(self, dataPath: str, config: Config):
        AbstractXml.__init__(self)
        self.dataPath = os.path.join(dataPath, "world.opml")
        self.config = config
        self.version = "1.0"
        self.nodeName = "opml"

        self.addChild(WorldBody(config))

    def save(self):
        AbstractXml.save(self)

@dataclass
class WorldOutline(AbstractXml):
    name: str = None
    ID: int = None
    description: str = None
    passion: str = None
    conflict: str = None
    nodeName: str = "outline"

    def __init__(self, config: Config, worldBody: WorldBody, level: int=2):
        AbstractXml.__init__(self)

        self.name = worldBody.fakeService.words(5)
        self.ID = worldBody.ID
        worldBody.ID+=1
        self.description = worldBody.fakeService.markdown(1)
        self.passion = worldBody.fakeService.markdown(1)
        self.conflict = worldBody.fakeService.markdown(1)

        if level <= config.worldLevels:
            for i in range(config.worldQuantity):
                self.addChild(WorldOutline(config, worldBody, level + 1))

