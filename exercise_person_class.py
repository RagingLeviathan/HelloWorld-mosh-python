class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hello there, {self.name}')


nicole = Person('Nicole Graham')
nicole.talk()

gene = Person("Bob Genie")
gene.talk()
