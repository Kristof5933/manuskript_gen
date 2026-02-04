#!/usr/bin/env python
# --!-- coding: utf8 --!--

from dataclasses import dataclass, field, fields

@dataclass
class AbstractData:
    dataPath: str = field(default_factory=str, repr=False, metadata={"saved": False})

    def __init__(self, path: str | None = None):
        self.dataPath = path

    def _changePath(self, path: str):
        self.dataPath = path

    def _serializableFields(self):
        for f in fields(self):
            if f.metadata.get("saved", True):
                yield f.name, getattr(self, f.name)

    def save(self):
        pass

