class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]
    
    def give_raise(self, percent):
        self.pay = int(self.pay * (1+percent))

    def __str__(self):
        return f"Person: {self.name}, {self.pay}"




if __name__ == "__main__":
    bob = Person('Bob Smith') # Test the class
    sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
    print(bob) # Fetch attached attributes
    print(sue)
    print(bob.last_name())
    sue.give_raise(.1)
    print(sue)
    