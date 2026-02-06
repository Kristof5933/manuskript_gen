#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
from config import Config
from util import safeFilename
from util.fakeService import FakeService
from dataclasses import dataclass, field, fields
from data.abstractMmd import AbstractMmd

@dataclass
class Labels(AbstractMmd):
    def __init__(self, dataPath: str, config: Config):
        AbstractMmd.__init__(self, os.path.join(dataPath, safeFilename(f"labels", "txt")))
        fakeService = FakeService()
        self.metaSpacing = 21

        for i in range(config.labelsQuantity):
            self.additionalProperties[fakeService.words(3)] = fakeService.color()

    def getRandomLabelById(self):
        fakeService = FakeService()
        keys = list(self.additionalProperties.keys())

        return fakeService.indexOfElement(keys)





