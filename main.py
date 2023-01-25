from random import randint

class Animal:
    def __init__(self, name, exp ):
        self.name = name
        self.exp = exp

    def __str__(self):
        return f"{self.name} с него можно получить {self.exp} опыта"

class Hunter:
    def __init__(self, name , exp, ):
        self.name = name
        self.exp = exp

    def __str__(self):
       return f"Мой любимый {self.name} имееи {self.exp} опыта "

    # def __add__(self, target): # повышение уровня за счсет опыта
    #     self.exp += target.exp
    #     print(f"Теперча  {self.name} имееи {self.exp} опыта")
    #     if self.exp >= 15:
    #         print(f"{self.name} перешел на новый уровень 2")

    shoot=0
    def shooting(self,target):
        shoot= int(input("     Вы прицеливаетесь: \n"
                        "1- выстрелиnm  2- идти дальше :"))
        if shoot == 1:
            good_shoot = randint(1,3)
            if good_shoot % 2==0:
                self.exp += target.exp
                print(f"      Попали и ваш опыт сейчас - {self.exp}")
            else:
                print(f"           Промах")
        elif shoot == 2:
            location()
        else:
            print(f'Зверь скрылся')
        return shoot

hunter = Hunter("Dimka", 0  ) # name , exp,
wolf = Animal("Wolf",5 )
bear = Animal("Bear", 9)
fox = Animal("Fox",4 )

animal_lokation = ["За деревом", "В кустах ", 'НА горе']
all_animals = [wolf,bear,fox]

def location():
    any_animanl = all_animals[randint(0,2)]
    print( f'                            ОХОТА НАЧАЛАСЬ')
    print( f'Вдруг ВЫ видите {(animal_lokation[randint(0,2)])} затаился {any_animanl}')
    hunter.shooting(any_animanl)


while hunter.exp <= 20:
    location()
print(f"Да Вы весь лес истрибили идити в другой")




























# print(hunter)


