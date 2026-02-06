#!/usr/bin/env python
# --!-- coding: utf8 --!--

from faker import Faker
from util.references import References

class Markdown:
    def __init__(self, faker: Faker, references: References, sections: int):
        self.sections = sections
        self.text = None
        self.faker = faker
        self.references = references

    @staticmethod
    def produceMarkdown(faker: Faker, sections: int, randomReferences: list[str] = []) -> str:
        content = ""
        addReferences = len(randomReferences) > 0
        for _ in range(sections):
            content += f"## {faker.sentence()}\n\n"
            content += f"### {faker.sentence()}\n\n"
            paragraphs = '\n'.join(faker.paragraphs(10))
            if addReferences:
                referencesItems: list[str] = []
                for reference in randomReferences:
                    referencesItems.append(f"{faker.word()}: {reference} ")
                paragraphs += '\n\n' + ", ".join(referencesItems)
            content += f"{paragraphs}\n\n"

        return content

    def __str__(self):
        randomReferences: list[str] = []
        for _ in range(5):
            newValue=self.references.randomValue()
            randomReferences.append(newValue)

        content = Markdown.produceMarkdown(self.faker, self.sections, randomReferences)
        return content

class MarkdownFactory:
    def __init__(self, faker: Faker, references: References):
        self.items: list[Markdown] = []
        self.references = references
        self.faker: Faker = faker

    def newItem(self, sections: int) -> Markdown:
        item = Markdown(self.faker, self.references, sections)
        self.items.append(item)
        return item