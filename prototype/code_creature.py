import random

def random_mix_s(s1:str, s2:str)->str:
    # make two str can be blend into a new str
    if len(s1)<len(s2):
        s1+=s1
    elif len(s1)>len(s2):
        s2+=s2
    s1 = list(s1)
    s2 = list(s2)
    new_s = list()
    for i in zip(s1, s2):
        new_s.append(i[random.randint(0, 1)])
    return "".join(new_s)

class code_creature:
    # A code creature have first name(str), last name(str), genecode(str), life(int), generation(int)
    def __init__(self, first_name = '', last_name = '', genecode = "123456789", life = 3, generation = 0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.genecode = genecode
        self.life = life
        self.generation = generation
        self.childs = {}

    def breed(self, mate) -> None:
        # two creature make new creature and get new child
        if type(self) == type(mate):
            # it need to be two code creature to breed a new code creature
            if len(self.genecode) == len(mate.genecode):
                # it need to have same genecode len to get a right genecode to breed
                self.life -= 1
                mate.life -= 1
                # breed is danger so parents need to reduct their life
                
                new_first_name = random_mix_s(self.first_name, mate.first_name)
                # first name is blend with a and b
                new_last_name = self.last_name if random.randint(0, 1) else mate.laSst_name
                # first name is random from a or b
                new_genecode = random_mix_s(self.genecode, mate.genecode)
                # genecode is blend with a and b
                child = code_creature(new_first_name, new_last_name, new_genecode, self.life, self.generation+1)
                
                self.childs[child.get_full_name()]=child
                mate.childs[child.get_full_name()]=child
        return
    
    def get_full_name(self):
        return self.first_name + '_' + self.last_name
    
    def __str__(self):
        return f'The creature name is {self.get_full_name()} and genecode is {self.genecode}'

    def __repr__(self):
        return f'Creature(\'{self.get_full_name()}\', {self.genecode})'
    
if __name__ == "__main__":
    a = code_creature("adam", "apple", "111111111", 3, 0)
    b = code_creature("eve", "eva", "000000000", 3, 0)
    print(str(a))
    print(repr(a))
    print("")
    print(str(b))
    print(repr(b))
    print("")
    a.breed(b)
    print(str(a.childs))
    for child in a.childs.values():
        print(str(child))
        print("")
