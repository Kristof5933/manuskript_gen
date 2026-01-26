import random
from faker import Faker

class FakeService:        
    def __init__(self, locale='en_US', seed=None):
        self.faker = Faker(locale)
        if seed is not None:
            Faker.seed(seed)
            random.seed(seed)

    def int(self, min_val=0, max_val=100):
        return random.randint(min_val, max_val)

    def random_float(self, min_val=0.0, max_val=1.0):
        return random.uniform(min_val, max_val)
    
    def array_of_random_int(self, min_val=0, max_val=100, array_size=20):
        possible_values=list(range(min_val, max_val))
        final_values=list()

        for i in range(1, array_size):
            value = random.choice(possible_values) 
            possible_values.remove(value)
            final_values.append(value)

        return final_values

    def words(self, count=5):
        words = ' '.join(self.faker.words(nb=count))
        return words
    
    def paragraph(self, count=5):
        return self.faker.paragraph(nb_sentences=count)
    
    def paragraphs(self, count=5):
        paragraphs = '\n'.join(self.faker.paragraph(nb_sentences=count))
        return paragraphs
    
    def markdown(self, sections=2):
        content = ""
        for _ in range(sections):
            content += f"## {self.faker.sentence()}\n\n"
            content += f"### {self.faker.sentence()}\n\n"
            paragraphs = '\n'.join(self.faker.paragraphs(10))
            content += f"{paragraphs}\n\n"
        return content
    
    def __make_paragraph(self, sentences=5, words_per_sentence=12):
        return " ".join(self.faker.sentence(nb_words=words_per_sentence) for _ in range(sentences))
    
    def __make_paragraphs(self, number_of_paragraphs=5, sentences=5, words_per_sentence=12):
        return "\n\n".join(self.__make_paragraph(sentences, words_per_sentence) for _ in range(number_of_paragraphs))
    
    def novel_content(self, paragraphs=10):
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
    
    def boolean(self, chance_of_getting_true):
        return self.faker.boolean(chance_of_getting_true=chance_of_getting_true)
