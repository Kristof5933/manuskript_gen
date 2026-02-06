#!/usr/bin/env python
# --!-- coding: utf8 --!--

from enum import Enum
from collections import defaultdict
import random

class ReferenceType(Enum):
    OUTLINE = (1, "O")
    WORLD = (2, "W")
    CHARACTER = (3, "C")
    PLOT = (4, "P")

    def __init__(self, _: int, tag: str):
        self.tag = tag

    @classmethod
    def randomValue(cls) -> "ReferenceType":
        return random.choice(list(cls))

class References:
    referenceIds: list[str]

    def __init__(self):
        self.referenceIds: list[str] = []

    def _addReference(self, referenceType: ReferenceType, ID: int, name: str):
        self.referenceIds.append(f"{{{referenceType.tag}:{ID}:{name}}}")

    def addWorldItem(self, ID: int, name: str):
        self._addReference(ReferenceType.WORLD, ID, name)

    def addOutlineItem(self, ID: int, name: str):
        self._addReference(ReferenceType.OUTLINE, ID, name)

    def addCharacterItem(self, ID: int, name: str):
        self._addReference(ReferenceType.CHARACTER, ID, name)

    def addPlotItem(self, ID: int, name: str):
        self._addReference(ReferenceType.PLOT, ID, name)

    def randomValue(self) -> str:
        if len(self.referenceIds) > 0:
            return random.choice(self.referenceIds)
        else:
            return None


