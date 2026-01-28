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
                
    def save(self):
        pass

