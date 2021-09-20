import random

class human:
    #static poles
    default_name='no_name'
    default_age=0

    def __init__(self,name=default_name, age=default_age):
        #public
        self.name = name
        self.age = age

        #private
        self.__money=0
        self.__house=0

    def info(self):
        print(f"Name {self.name}")
        print(f"age {self.age}")
        print(f"money {self.__money}")
        print(f"house {self.__house}")

    @staticmethod
    def default_info():
        print(f"default name {human.default_name}")
        print(f"default age {human.default_age}")

    #private_method
    def __make_deal(self,home,price):
        self.__money=price
        self.__house=house

    def earn_money(self, salary):
        self.__money+=salary
        print(f'You earned {salary} dollars, now u have {self.__money}')

    def buy_house(self,house,price):
        house_price=house.final_price(price)
        if self.__money>= house_price:
            self.__make_deal(house,house_price)
        else:
            print("Деняк нет, idi rabotai bomjara")

class house:
    #security
    def __init__(self,area, price):
        self._area = area
        self._price = price

    #regular_method
    def final_price(self,discount):
        final_price = self._price * (100 - discount) / 100
        print(f"price with discount  {final_price}")
        return final_price

class smallhouse(house):
    default_area= 40

    def __init__(self,price):
        super().__init__(smallhouse.default_area,price)


#if __name__=='__main__':
 #   dastan= human('dastan', 19)
  #  dastan.info()


class soldier:
    bullets= 8

    def fire(self):
        self.bullets= 0
        print("tigi-tigitishh")

    def reload(self):
        self.bullets+=8

class shooting(soldier):
    def act_of_shooting(self):
        self.fire()
        self.reload()
        self.fire()

#ryan=shooting()
#ryan.act_of_shooting()


class household:
    default_area= 40
    bed = "bed"
    wardrobe = "wardrobe"
    table = "table"
    beda = 4
    wardrobea = 2
    tablea = 1.5

    def place(self):
        print(f"Whole area is : {self.default_area}")
        available_area= self.default_area - (self.beda+self.wardrobea+self.tablea)
        print(f"available area {available_area}")
        print("furniture : {bed, wardrobe , table}")

#dom= household()
#dom.place()

class Student:

    def __init__(self, name, age , major):
        self.name = name
        self.age= age
        self.major= major


    def pr(self):
        print(f"Name: {self.name}, age: {self.age}, major: {self.major}")

Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
#Steve.pr()

def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)


class moneyfmt:

    def __init__(self, amount):
        self.amount= amount

    def dollarize(self):
        print(as_currency(self.amount))

#cash=moneyfmt(444.66)
#cash.dollarize()


#zadanie 10
olimp=[]
nomad=[]
x=0

def create_soldiers(number):
    x=0
    for i in range(0,number):
        f=random.randint(0,3)
        if f==1:
            olimp.append( x)
            x=x+1
        else:
            nomad.append(x)
            x+=1
    print("Воители Олимпа: " , olimp)
    print("Nomad army: ", nomad)


def fight(hero_1, hero_2):
    check1=len(olimp)
    check2=len(nomad)
    if check1>check2:
        zeus.lvl_up()
        print("Олимпийцы выиграли!")
        zeus.info()
    else:
        attila.lvl_up()
        print("Кочевники разгромили Олимпийцев!")
        attila.info()
    print("Битва окончена!")




class hero:
    lvl=0

    def __init__(self, country):
        self.country = country

    def lvl_up(self):
        self.lvl+=1

    def info(self):
        print(self.country)
        print(self.lvl)

class soldier:

    def __init__(self,role_model):
        self.role_model=role_model

    def idti(self):
        print(f'idet za {self.role_model}')

zeus=hero('olimp')
attila=hero('nomad')
create_soldiers(100)
fight(zeus,attila)

create_soldiers(100)
fight(zeus,attila)

create_soldiers(100)
fight(zeus,attila)
create_soldiers(100)
fight(zeus,attila)
create_soldiers(100)
fight(zeus,attila)











































































































