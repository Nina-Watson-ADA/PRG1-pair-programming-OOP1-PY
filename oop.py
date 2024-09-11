class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        self._name = name  
        self._date_of_birth = date_of_birth  
        self._place_of_birth = place_of_birth  

    @property
    def name(self):
        return self._name

    @property
    def date_of_birth(self):
        return self._date_of_birth  

    @name.setter
    def name(self, name):
        self._name = name

    def talk(self):
        return f"Hi, my name is {self._name} and I was born in {self._place_of_birth}."


# Define the AdaStaff class as a subclass of Person
class AdaStaff(Person):
    def __init__(self, name, date_of_birth, place_of_birth, role, base):
        super().__init__(name, date_of_birth, place_of_birth)
        self._role = role
        self._base = base

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    def talk(self):
        return f"Hi, my name is {self._name}. I work in {self._base} and my role is {self._role}."



# Creating two instances of the Person class
aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
steve = AdaStaff("Steve Rich", "01/01/1998", "Lincoln", "Lecturer", "Manchester");



# Printing instances and calling methods
print(steve.__dict__)  # Print attributes of Steve
print(aqil.__dict__)  # Print attributes of Aqil
print(steve.talk())  # Output 
print(aqil.talk())  # Output
steve.base = "London" # Using the setter method to change base to London
print(steve.talk())  # Output now base has been changed (to confirm)
print(steve.name)  # Output: Steve Rich
