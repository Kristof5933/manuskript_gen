#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
from config import Config
from util import safeFilename
from util.fakeService import FakeService
from dataclasses import dataclass, field, fields
from data.abstractMmd import AbstractMmd

@dataclass
class Summary(AbstractMmd):
    Situation: str = None
    Sentence: str = None
    Paragraph: str = None
    Page: str = None
    Full: str= None

    def __init__(self, dataPath: str, config: Config):
        AbstractMmd.__init__(self, os.path.join(dataPath, safeFilename(f"summary", "txt")))
        fakeService = FakeService()
        self.metaSpacing = 13

        self.Situation = fakeService.words(10)
        self.Sentence = fakeService.words(10)
        self.Paragraph = fakeService.paragraph(10)
        self.Page = fakeService.markdown(1)
        self.Full = fakeService.markdown(10)
