from lib import reader 

template = """{w} ({pos})\n\n{pronunciation}\n\n{definition}"""

class Definition(dict):
    def __init__(self, word:str, data:dict):
        super().__init__(data)
        self.word = word
        self.pos = reader.get_pos(self)

    def short_print(self) -> str:
        short_def = self['shortdef'][0]
        return "{w} ({pos}): {d}".format(w=self.word, pos=self.pos, d=short_def)

    def show(self) -> str:
        pos = reader.get_pos(self)
        pron = reader.get_pronunciations(self)
        definition = reader.get_shortdef(self)
        return template.format(w=self.word, 
                               pos=pos, 
                               pronunciation=pron, 
                               definition=definition)