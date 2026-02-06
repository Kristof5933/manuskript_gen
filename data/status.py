#!/usr/bin/env python
# --!-- coding: utf8 --!--

import os
from dataclasses import dataclass, field, fields
from data.abstractData import AbstractData
from config import Config
from util.fakeService import FakeService
import collections

class Status(AbstractData):
    statuses: list[str]

    def __init__(self, path: str, config: Config):
        AbstractData.__init__(self,  os.path.join(path , "status.txt"))
        self.statuses = [
            'Idea Seeded',
            'Brainstorming',
            'Researching',
            'Outlining',
            'Worldbuilding / Character Development',
            'Drafting',
            'Drafting Started',
            'Partial Draft',
            'First Draft Complete',
            'Expanded Draft / Developmental Draft',
            'Revisions',
            'Developmental Editing',
            'Rewriting',
            'Line Editing',
            'Copyediting',
            'Beta Reading / Peer Review',
            'Revised Draft Complete',
            'Finalization',
            'Proofreading',
            'Final Manuscript Ready',
            'Format & Layout',
            'Publication or Submission',
            'Submitted',
            'Under Review',
            'Accepted / Approved',
            'Rejected (Revision Possible)',
            'Published / Finalized',
        ]

    def save(self):
        with open(self.dataPath, 'wt', encoding='utf-8') as file:
            for status in self.statuses:
                file.write(f"{status}\n")

    def getRandomStatusID(self):
        fakeService = FakeService()
        return fakeService.indexOfElement(self.statuses)
