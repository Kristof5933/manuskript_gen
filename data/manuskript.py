#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
import shutil
from config import ConfigLoader, Config
# TODO: I'd like to have from data import A, B
from data.characters import Characters
from data.summary import Summary
from data.labels import Labels
from data.infos import Infos
from data.outline import Outline
from data.status import Status

class Manuskript:
    def __init__(self, path: str, profileName: str):
        self.basePath = path
        self.manuskriptName = profileName # TODO : maybe add a specific output name instead of the profile name
        self.profileName = profileName 
        self.config: Config = ConfigLoader().loadConfig(profileName)

        self.dataPath = os.path.join(path, self.manuskriptName)
        self.createAndCleanOutputFolder(self.dataPath)

        self.characters = Characters(self.dataPath, self.config)
        self.summary = Summary(self.dataPath, self.config)
        self.labels = Labels(self.dataPath, self.config)
        self.infos = Infos(self.dataPath, self.config)
        self.status = Status(self.dataPath, self.config)

        self.outline = Outline(self.dataPath, self.config, self.status, self.characters, self.labels)

    def createAndCleanOutputFolder(self, outputFolder: str):
        os.makedirs(outputFolder, exist_ok=True)

        for filename in os.listdir(outputFolder):
            file_path = os.path.join(outputFolder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def save(self):

        self.summary.save()
        self.characters.save()
        self.labels.save()
        self.infos.save()
        self.status.save()
        self.outline.save()

        # TODO: handle zip version
        mskFile = os.path.join(self.basePath, f"{self.manuskriptName}.msk")
        with open(mskFile, "w") as f:
            f.write("1")


