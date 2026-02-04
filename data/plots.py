#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
from config import Config
from util import safeFilename, FakeService
from dataclasses import dataclass, field, fields
from data.abstractXml import AbstractXml
from data.characters import Characters

@dataclass
class Plots(AbstractXml):

    def __init__(self, dataPath: str, config: Config, characters: Characters):
        AbstractXml.__init__(self)
        self.dataPath = os.path.join(dataPath, "plots.xml")
        self.config = config
        self.characters = characters
        self.nodeName = "root"
        self.ID=0
        self.fakeService = FakeService()

        for i in range(config.plotsQuantity):
            self.addChild(Plot(config, self))

    def save(self):
        AbstractXml.save(self)

@dataclass
class Plot(AbstractXml):
    name: str = None
    ID: int = None
    importance: int = None
    characters: list[int] = None
    description: str = None
    result: str = None
    steps: str = None

    def __init__(self, config: Config, plots: Plots):
        AbstractXml.__init__(self)
        self.nodeName = "plot"
        self.name = plots.fakeService.words(5)
        self.ID = plots.ID
        plots.ID+=1
        self.importance = plots.fakeService.int(0, 2)
        self.description = plots.fakeService.markdown(1)
        self.result = plots.fakeService.markdown(1)
        self.steps = plots.fakeService.markdown(1)

        for _ in range(10):
            self.characters = plots.characters.getRandomCharactersId()

        for i in range(10):
            self.addChild(Step(plots, i))

@dataclass
class Step(AbstractXml):
    name: str = None
    ID: int = None
    meta: str = None
    summary: str = None

    def __init__(self, plots: Plots, ID: int):
        AbstractXml.__init__(self)
        self.nodeName = "step"
        self.ID = ID
        self.name = plots.fakeService.words(5)
        self.meta = plots.fakeService.words(10)
        self.summary = plots.fakeService.markdown(1)


