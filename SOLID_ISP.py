# BAD CODE - violates Interface Segregation Principle
class IMultiFunctionalDevice:
    def print(self):
        pass

    def scan(self):
        pass

    def copy(self):
        pass

    def fax(self):
        pass

# here these subclasses must also implement the other interface methods that they don't use
class Printer(IMultiFunctionalDevice):
    def print(self):
        print("Printing...")

class Scanner(IMultiFunctionalDevice):
    def scan(self):
        print("Printing...")

class Copier(IMultiFunctionalDevice):
    def copy(self):
        print("Printing...")

class Fax(IMultiFunctionalDevice):
    def fax(self):
        print("Printing...")


# GOOD CLASSES - more maintainable:
class IPrinter:
    def print(self):
        pass

class IScanner:
    def scan(self):
        pass

class ICopier:
    def copy(self):
        pass

class IFax:
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing...")

class Scanner(IScanner):
    def scan(self):
        print("Printing...")

class Copier(ICopier):
    def copy(self):
        print("Printing...")

class Fax(IFax):
    def fax(self):
        print("Printing...")