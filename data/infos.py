#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
from config import Config
from util import safeFilename, FakeService
from dataclasses import dataclass, field, fields
from data.abstractMmd import AbstractMmd

@dataclass
class Infos(AbstractMmd):
    Title: str = None
    Subtitle: str = None
    Serie: str = None
    Volume: int = None
    Genre: str = None
    License: str = None
    Author: str = None
    Email: str = None

    def __init__(self, dataPath: str, config: Config):
        AbstractMmd.__init__(self, os.path.join(dataPath, safeFilename(f"infos", "txt")))
        fakeService = FakeService()
        self.metaSpacing = 16

        self.Title = fakeService.words(4)
        self.Subtitle = fakeService.words(4)
        self.Serie = fakeService.words(4)
        self.Volume = fakeService.int(1, 10)
        self.Genre = fakeService.words(2)
        self.License = fakeService.words(2)
        self.Author = fakeService.name()
        self.Email = fakeService.email()