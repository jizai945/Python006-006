
# 动物类
class Animal(object):
    # def __new__(self):
    #     raise Exception('不能实例化这个类')

    def __init__(self, type, size, character):
        self.type = type
        self.size = size
        self.character = character
        if (self.size == '中' or self.size == '大') and self.type == '食肉' and self.character == '凶猛':
            self.danger = True
        else:
            self.danger = False


# 猫类
class Cat(Animal):
    # 类属性
    cry = True

    def __init__(self, name, type, size, character):
        super().__init__(type, size, character)
        self.name = name
        self.pet = (True if (self.danger == False) else False)


# 狗类
class Dog(Animal):
    # 类属性
    cry = True

    def __init__(self, name, type, size, character):
        super().__init__(type, size, character)
        self.name = name
        self.pet = (True if (self.danger == False) else False)


# 动物园类
class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animal_dict = {}

    def add_animal(self, animal):
        if id(animal) not in self.animal_dict:
            print('add animal sucess')
            self.animal_dict[id(animal)] = True
        else:
            print('add animal fail')

        # 根据类名字符串初始化变量
        exec('self.'+type(animal).__name__+'=True')


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)

    have_dog = hasattr(z, 'Dog')
    print(have_dog)

    dog1 = Dog('哈士奇 1', '食肉', '小', '温顺')
    z.add_animal(dog1)
    have_dog = hasattr(z, 'Dog')
    print(have_dog)
