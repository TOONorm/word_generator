
from random import *

#генератор словарей
def dict_gen(spisok,move=0):
    keys = list(spisok)
    k=0
    values = []
    for i in range(len(spisok)):
        values.append(spisok[k-move])
        k += 1
    return dict(zip(keys,values))

#генератор слов
class Words_generator:
    def __init__(self,list_1,list_2,prefix=[],suffix=[],end=[],):
        self.list_1 = list_1
        self.list_2 = list_2
        self.prefix = prefix
        self.suffix = suffix
        self.end = end

    def gen(self,quantity=1,len_word=1,pref=1,suff=1,end=1,mod=1, smb='. '):
        cp_end = []
        self.len_word = len_word
        try:
            for j in range(quantity):
                enter = []
                if pref == 1:
                    enter.append((choice(self.prefix)))
                for i in range(self.len_word):
                    enter.append(choice(self.list_1))
                    enter.append(choice(self.list_2))
                if suff == 1:
                    enter.append(choice(self.suffix))
                if end == 1:
                    enter.append(choice(self.end))
            if mod:
                print("".join(enter))
            cp_end.append(smb.join(enter),)
        except IndexError:
            print("У вас не заполнены какие-то из полей.")
        return "".join(cp_end)

