#!/usr/bin/env python
# --!-- coding: utf8 --!--

import random
from util.markdown import MarkdownFactory, Markdown
from util.references import References
from faker import Faker

class FakeService:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, references: References | None = None, locale: str = "en_US", seed: int | None =None):
        if self._initialized:
            return
        
        if references is None:
            raise ValueError("Initial call must define references")
        
        self.faker: Faker = Faker(locale)
        self.markdownFactory = MarkdownFactory(self.faker, references)
        self.references = references

        if seed is not None:
            Faker.seed(seed)
            random.seed(seed)

        self._initialized = True

    def int(self, min_val: int=0, max_val: int=100):
        return random.randint(min_val, max_val)
    
    def indexOfElement(self, elements: list):
        return random.randint(0, len(elements))

    def random_float(self, min_val: float=0.0, max_val: float =1.0):
        return random.uniform(min_val, max_val)
    
    def array_of_random_int(self, min_val: int=0, max_val: int=100, array_size: int=20):
        possible_values=list(range(min_val, max_val))
        final_values=list()

        for i in range(1, array_size):
            value = random.choice(possible_values) 
            possible_values.remove(value)
            final_values.append(value)

        return final_values

    def words(self, count: int=5):
        words = ' '.join(self.faker.words(nb=count))
        return words
    
    def paragraph(self, count: int=5):
        return self.faker.paragraph(nb_sentences=count)
    
    def paragraphs(self, count:int =5):
        paragraphs = '\n'.join(self.faker.paragraph(nb_sentences=count))
        return paragraphs
    
    def markdown(self, sections: int, withReferences:bool = True) -> str | Markdown:
        if not withReferences:
            return Markdown.produceMarkdown(self.faker, sections)
        else:
            return self.markdownFactory.newItem(sections)
    
    def __make_paragraph(self, sentences: int=5, words_per_sentence: int=12):
        return " ".join(self.faker.sentence(nb_words=words_per_sentence) for _ in range(sentences))
    
    def __make_paragraphs(self, number_of_paragraphs: int=5, sentences: int=5, words_per_sentence: int=12):
        return "\n\n".join(self.__make_paragraph(sentences, words_per_sentence) for _ in range(number_of_paragraphs))
    
    def novel_content(self, paragraphs: int=10):
        content = f"# {self.chapter_num}\n\n"
        content += f"{self.__make_paragraphs(paragraphs, sentences=7, words_per_sentence=17)}\n\n"
        self.chapter_num += 1

        return content

    def color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    def name(self):
        return self.faker.name()

    def email(self):
        return self.faker.email()
    
    def boolean(self, chance_of_getting_true: int):
        return self.faker.boolean(chance_of_getting_true=chance_of_getting_true)
