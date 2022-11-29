import random

class Ess():
    #Класс описывает существо
    max_hp = 30
    def __init__(self,name, attack, defense):
        self.name = name
        self.attack = self.set_val(attack)
        self.defense = self.set_val(defense)
        self.hp = self.max_hp
        self.damage = [1,2,3,4,5,6]
        self.is_live = True

    def set_val(self, val):
        #Проверяем корректность значений
        #атаки и защиты при инициализации
        if type(val) is int and 0 < val < 21:
            return val
        else:
            raise Exception('Недопустимое значение')

    def set_hp(self, val):
        #Метод установки корректного
        #значения здоровья
        if type(val) is int:
            if val <= self.max_hp:
                self.hp = val
            else:
                self.hp = self.max_hp
        else:
            raise Exception('Недопустимое значение')
    
    def check_hp(self):
        #Метод проверки здоровья
        if self.hp <= 0:
            self.is_live = False
            print(f'Существо {self.name} умерло')
        else:
            print(f'{self.name} HP: {self.hp}\n')

    def get_info(self):
        print(f'Имя: {self.name}\tАтака: {self.attack}\tЗащита: {self.defense}\tHP: {self.hp}')
    
    def at_to(self, ob):
        #Метод атаки, принимает атакуемый объект
        # print (ob.is_live, self.is_live)
        if not (ob.is_live and self.is_live):
            raise Exception('В поединке не может учавствовать мертвое существо')
        elif ob == self:
            raise Exception('Существо не может атаковать себя')
        else:
            print(f'{self.name} атакует {ob.name}')
            N = self.attack - (ob.defense + 1)
            if N < 1: 
                N = 1
            # print (f'Всего будет попыток: {N}')
            for i in range(N):
                cube = random.randint(1, 6)
                if cube == 5 or cube == 6:
                    print ('Атака успешная')
                    rnd_index = random.randint(0,len(self.damage)-1)
                    ob.hp -= self.damage[rnd_index]
                    ob.check_hp()
                    break
            else:
                print('Атака завершилась неудачей\n')
class Player(Ess):
    #Класс описывает игрока, наследник Ess()
    rec_count = 3
    def __init__(self, name, attack, defense):
        super().__init__(name, attack, defense)

    def recovery(self):
        #Метод исцеления
        if self.rec_count > 0:
            super().set_hp(int(self.hp+self.max_hp//0.5))
            self.rec_count -= 1
            print(f'{self.name} - исцеление. HP: {self.hp}')
            print(f'Исцелений осталось: {self.rec_count}')
        else:
            print('Исцеления закончились')




p_1 = Ess('Monster', 20,10)
p_2 = Player('Player', 15, 12)

p_1.get_info()
p_2.get_info()

p_1.at_to(p_2)
p_2.at_to(p_1)

p_1.get_info()
p_2.get_info()
    
