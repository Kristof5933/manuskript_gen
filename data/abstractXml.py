#!/usr/bin/env python
# --!-- coding: utf8 --!--

from __future__ import annotations
from dataclasses import dataclass, field, fields
from data.abstractData import AbstractData
import xml.etree.ElementTree as ET

@dataclass
class AbstractXml(AbstractData):
    nodeName: str = field(default_factory=str, metadata={"saved": False})

    def __init__(self, path: str | None = None):
        AbstractData.__init__(self, path)
        self.items: list[AbstractXml] = []

    def addChild(self, item: AbstractXml):
        self.items.append(item)

    def indent(self, elem, level=0):
        i = "\n" + level * "  "
        j = "\n" + (level + 1) * "  "

        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = j

            for child in elem:
                self.indent(child, level + 1)

            if not child.tail or not child.tail.strip():
                child.tail = i
        else:
            if not elem.tail or not elem.tail.strip():
                elem.tail = i

    def _toXml(self):
        element = ET.Element(self.nodeName)

        for key, value in self._serializableFields():
            if type(value) is list:
                element.set(key, ",".join(map(str, value)))
            else:
                element.set(key, str(value))

        for item in self.items:
            element.append(item._toXml())

        return element

    def save(self):
        root = self._toXml()

        self.indent(root)

        xmlBytes = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        xml = xmlBytes.decode("utf-8")
        xml = xml.replace("&amp;#10;", "&#10;")
        with open(self.dataPath, "w", encoding="utf-8") as f:
            f.write(xml)
