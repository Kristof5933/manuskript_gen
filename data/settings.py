#!/usr/bin/env python
# --!-- coding: utf8 --!--

from config import ConfigLoader, Config
import os
import json

class Settings:
    def __init__(self, dataPath: str, config: Config):
        self.dataPath = dataPath
        self.config = config

    def save(self):
        settings = {
            "autoSave": False,
            "autoSaveDelay": 1,
            "autoSaveNoChanges": False,
            "autoSaveNoChangesDelay": 5,
            "corkBackground": {
                "color": "#926239",
                "image": "writingdesk"
            },
            "corkSizeFactor": 100,
            "corkStyle": "new",
            "countSpaces": True,
            "defaultTextType": "md",
            "dict": None,
            "dontShowDeleteWarning": False,
            "folderView": "outline",
            "frequencyAnalyzer": {
                "phraseMax": 5,
                "phraseMin": 2,
                "wordExclude": "a, and, or",
                "wordMin": 1
            },
            "fullScreenTheme": "spacedreams",
            "fullscreenSettings": {
                "autohide-bottom": True,
                "autohide-left": True,
                "autohide-top": True
            },
            "lastTab": 0,
            "openIndexes": [
                ""
            ],
            "outlineViewColumns": [
                0,
                5,
                8,
                9,
                11,
                12,
                13,
                7
            ],
            "progressChars": False,
            "revisions": {
                "keep": self.config.sectionsRevisions,
                "rules": {
                    "2592000": 86400,
                    "3600": 600,
                    "600": 60,
                    "86400": 3600,
                    "null": 604800
                },
                "smartremove": False
            },
            "saveOnQuit": True,
            "saveToZip": False,
            "spellcheck": False,
            "textEditor": {
                "alwaysCenter": False,
                "background": "#ffffff",
                "backgroundTransparent": False,
                "cursorNotBlinking": False,
                "cursorWidth": 1,
                "focusMode": False,
                "font": "Sans Serif,9,-1,5,50,0,0,0,0,0",
                "fontColor": "#000000",
                "indent": False,
                "lineSpacing": 100,
                "marginsLR": 0,
                "marginsTB": 20,
                "maxWidth": 600,
                "misspelled": "#F00",
                "spacingAbove": 5,
                "spacingBelow": 5,
                "tabWidth": 20,
                "textAlignment": 0
            },
            "tooltipStyle": {
                "backgroundColor": "#ffffdc",
                "borderColor": "#767676",
                "textColor": "#000000",
                "useSystemDefaultsForTooltips": True
            },
            "viewMode": "fiction",
            "viewSettings": {
                "Cork": {
                    "Background": "Nothing",
                    "Border": "Nothing",
                    "Corner": "Label",
                    "Icon": "Nothing",
                    "Text": "Nothing"
                },
                "Outline": {
                    "Background": "Nothing",
                    "Icon": "Nothing",
                    "Text": "Compile"
                },
                "Tree": {
                    "Background": "Nothing",
                    "Icon": "Nothing",
                    "InfoFolder": "Nothing",
                    "InfoText": "Nothing",
                    "Text": "Compile",
                    "iconSize": 24
                }
            }
        }

        with open(os.path.join(self.dataPath, "settings.txt"), "w") as f:
            json.dump(settings, f, indent=4)
