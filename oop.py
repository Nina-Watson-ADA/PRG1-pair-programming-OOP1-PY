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
nina = Person("Nina Watson", "10/09/2004", "London")
steve = AdaStaff("Steve Rich", "01/01/1998", "Lincoln", "Lecturer", "Manchester");



# Printing instances and calling methods
print(steve.__dict__)  # Print attributes of Steve
print(aqil.__dict__)  # Print attributes of Aqil
print(nina.__dict__)
print(steve.talk())  # Output 
print(aqil.talk())  # Output
print(nina.talk())
steve.base = "London" # Using the setter method to change base to London
print(steve.talk())  # Output now base has been changed (to confirm)
print(steve.name)  # Output: Steve Rich
class Person:
    def __init__(self, name, date_of_birth, place_of_birth):
        print("Constructing Person: ", name, date_of_birth, place_of_birth)
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


class AdaStudent(Person):
    def __init__(self, name, date_of_birth, place_of_birth, company, pathway, startyear):
        print(name, date_of_birth, place_of_birth, company, pathway, startyear)
        super().__init__(name, date_of_birth, place_of_birth)
        self._company = company
        self._pathway = pathway
        self._startyear = startyear

    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, company):
        self._company = company

    @property
    def pathway(self):
        return self._pathway
    
    @pathway.setter
    def pathway(self, pathway):
        self._pathway = pathway

    def talk(self, orignal = False):
        if orignal:
            return super().talk()
        return f"Hello my name {self._name}, I work for {self._company} and started in {self._startyear}"   


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

class Cohort:
    def __init__(self, cohort_code):
        self._cohort_code = cohort_code
        self._cohort = []
    
    @property
    def cohort_code(self):
        return self._cohort_code

    def add_student(self, student):
        print("Adding Student", student.name)
        self._cohort.append(student)
        pass

    def remove_student(self, student):
        print("Removing Student", student.name)
        self._cohort.remove(student)
        pass

    def list(self):
        for student in spring2025._cohort:
            print(student.name)





# Creating two instances of the Person class
# aqil = Person("Aqil Hussain", "01/01/2000", "Manchester")
# steve = AdaStaff("Steve Rich", "01/01/1998", "Lincoln", "Lecturer", "Manchester");
dan = AdaStudent("Dan F", "01/01/1999", "London", "Ada", "SE", "2025")
paul = AdaStudent("Paul O", "01/01/1999", "London", "Ada", "SE", "2025")
nina = AdaStudent("Nina W", "01/01/1999", "London", "Ada", "DA", "2025")
muhammed = AdaStudent("Muhammed D", "01/01/1999", "London", "Ada", "SE", "2025")
print(dan.talk())
print(dan.talk(True))

spring2025 = Cohort("04-25-CBD")
print(spring2025.cohort_code)
spring2025.add_student(dan)
spring2025.add_student(paul)
spring2025.add_student(nina)
spring2025.add_student(muhammed)

# print(spring2025.__dict__)

print("\n------------------\n")

spring2025.list()

spring2025.remove_student(dan)
print("\n------------------\n")
spring2025.list()


# Printing instances and calling methods
# print(steve.__dict__)  # Print attributes of Steve
# print(aqil.__dict__)  # Print attributes of Aqil
# print(steve.talk())  # Output 
# print(aqil.talk())  # Output
# steve.base = "London" # Using the setter method to change base to London
# print(steve.talk())  # Output now base has been changed (to confirm)
# print(steve.name)  # Output: Steve Rich