
class Riven:
    camp = 'Noxus'

    def __init__(self, nickname, aggressivity=54, life_value=414, money=1001, armor=3):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value
        self.money = money
        self.armor = armor

    def attack(self, enemy):
        damage_value = self.aggressivity - enemy.armor
        enemy.life_value = damage_value


class Garen:
    camp = 'Demacia'

    def __init__(
            self,
            nickname,
            aggressivity=58,
            life_value=454,
            money=100,
            armor=10):
        self.nickname = nickname
        self.aggressivity = aggressivity
        self.life_value = life_value
        self.money = money
        self.armor = armor

    def attack(self, enemy):
        damage_value = self.aggressivity - enemy.armor
        enemy.life_value -= damage_value


class BlackCleaver:
    def __init__(self, price=475, aggrev=9, life_value=100):
        self.price = price
        self.aggrev = aggrev
        self.life_value = life_value

    def update(self, obj):
        obj.money -= self.price  # 减钱
        obj.aggressivity += self.aggrev  # 加攻击
        obj.life_value += self.life_value  # 加生命值

    def fire(self, obj):
        obj.life_value -= 1000  # 假设火烧的攻击力是1000


class Employee:
    # '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary=1000):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


r1 = Riven('草丛伦')
g1 = Garen('盖文')
b1 = BlackCleaver()
emp1 = Employee('hupc', 1000)

print('r1的攻击力：%d，生命值：%d，金钱：%d' % (r1.aggressivity, r1.life_value, r1.money))

# 购买装备
if r1.money > b1.price:
    r1.b1 = b1
    b1.update(r1)

# print(r1)

print('r1的攻击力：%d，生命值：%d，金钱：%d' % (r1.aggressivity, r1.life_value, r1.money))
