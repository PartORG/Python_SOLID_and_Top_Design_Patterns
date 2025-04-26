# BAD CLASS - violates LisKov Substitution Principle:
class Bird:
    def fly(self):
        print("I can fly")

# we will not get an expected behaviour if we use this class
class Penguin(Bird):
    def fly(self):
        print("I can't fly")

# GOOD CLASS:
class Bird:
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")

# propper brake down of our classes
class Penguin(NonFlyingBird):
    pass