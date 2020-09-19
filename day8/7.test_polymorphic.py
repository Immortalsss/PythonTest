class Dog(object):
    def work(self):
        print('指哪打哪。。。')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人。。。')


class DrugDog(Dog):
    def work(self):
        print('追击毒品。。。')


class Person(object):
    # 传入不同的对象dog
    def work_with_dog(self, dog):
        dog.work()


ad = ArmyDog()
dd = DrugDog()

test = Person()
test.work_with_dog(ad)
test.work_with_dog(dd)