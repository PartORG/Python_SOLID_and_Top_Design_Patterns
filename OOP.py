from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def description(self):
        print(f"{self.__class__.__name__} says: {self.sound()}")


class Dog(Animal):
    def sound(self):
        return "Woof!"

    def description(self):
        super().description()


class Cat(Animal):
    def sound(self):
        return "Meow!"

    def description(self):
        super().description()


if __name__ == '__main__':
    dog = Dog()
    dog.description()
    cat = Cat()
    cat.description()