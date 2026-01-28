#!/usr/bin/env python
# --!-- coding: utf8 --!--

from dataclasses import dataclass, field, fields
from data.abstractData import AbstractData
import collections

@dataclass
class AbstractMmd(AbstractData):
    additionalProperties: dict[str, str] = field(default_factory=dict, metadata={"saved": False})
    metaSpacing: int = field(default=16, repr=False, metadata={"saved": False})

    def __init__(self, path: str | None = None):
        AbstractData.__init__(self, path)
        self.additionalProperties = {}

    def _serializableFields(self):
        for f in fields(self):
            if f.metadata.get("saved", True):
                yield f.name, getattr(self, f.name)

    def save(self):
        metadata = collections.OrderedDict()

        # TODO: add "body" 
        for key, value in self._serializableFields():
            if key != "additionalProperties":
                metadata[key] = value

        for key, value in self.additionalProperties.items():
            metadata[key] = value

        metaSpacing = self.metaSpacing

        for (key, value) in metadata.items():
            if value is None:
                continue

            metaSpacing = max(metaSpacing, len(key) + 2)

        with open(self.dataPath, 'wt', encoding='utf-8') as file:
            for (key, value) in metadata.items():
                if value is None:
                    continue

                spacing = metaSpacing - (len(key) + 2)
                lines = str(value).split("\n")

                file.write(key + ": " + spacing * " " + lines[0] + "\n")

                for line in lines[1:]:
                    file.write(metaSpacing * " " + line + "\n")