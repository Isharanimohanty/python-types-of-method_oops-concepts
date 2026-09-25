
# How can we create a empty class

#class A:
    #def __init__(self):   # default constructor
        # age=25
        # print(age)
#obj=A()
#obj2=A()


#class A:
    #"satya loves isha"
    #love=8
    #print(love)
#obj=A()
#print(obj.love)
#print(A.__doc__)



#class A:
    #def __init__(self,love,age,address):
        #print(love," ",age," ",address)
#obj=A("gunu",25,"srirampur")

#class A:
    #"Gunu i love you loo"
    #age = 24
    #print(age)
#obj=A()
#print(obj.age)
#print(A.age)
#print(obj.__doc__)

#class A:
    #pass----------------empty class
#obj=A()

"""class A:
    def __init__(self,name,age,address):
        print("name"," ",age," ","address")

obj=A("gugu",22,"Srirampur")"""

"""class student:
    def display(self):
        name="i love loo mo dhana"
        print(name)
obj=student()
obj.display()"""

"""This above code is of this below question 
Create a class Student
Create a method display()
Inside it, print "My name is Rahul"
Create an object and call the method."""


"""class employee:
    def __init__(self,name):
        self.name=name
obj=employee("satyajit")
print(obj.name

This above code is of this question
Create a class Employee
Create a constructor that accepts name
Store it in an instance variable.
Create an object with "Satyajit"
Print the employee's name."""

"""class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
obj=Car("Toyota","fortuner")
print(obj.brand,obj.model)"""



"""class Calculator:
        def add(self,num1,num2):
            return num1+num2
        def sub(self,num1,num2):
            return num1-num2
        def mul(self,num1,num2):
            return num1*num2
obj=Calculator()
obj.add(num1=1,num2=2)
obj.sub(num1=2,num2=3)
obj.mul(num1=2,num2=3)
print(obj.add(num1=2,num2=3))
print(obj.sub(num1=2,num2=3))
print(obj.mul(num1=2,num2=3))"""


"""class Calculator:
    def add(self, num1, num2):
        return (num1 + num2)
    def sub(self, num1, num2):
        return (num1 - num2)
    def mul(self, num1, num2):
        return (num1 * num2)
obj=Calculator()
print(obj.add(num1=1, num2=2),(obj.sub(num1=1, num2=2)),(obj.mul(num1=1, num2=2)),sep=",")"""
"""The above code is of this question
Create a class Calculator
Create three methods:
add()
subtract()
multiply()
Each method should accept two numbers and return the result.
Create an object and test all three methods."""


"""class Login:
    def __init__(self, username, password):
        self.username=username
        self.password=password

    def login(self):
            print("isha",self.username)
            print("isha@12345",self.password)

obj=Login("isha","isha@12345")
obj.login()"""

"""This above code is of this question
Create a class Login
Constructor should accept:
username
password
Create a method:
login()
It should print:
Username: <username>
Password: <password>
Create an object and call login()."""

"""class BankAccount:
    "This class represents a bank account"
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display_balance(self):
        print("name",self.name,"balance",self.balance)
obj=BankAccount("isha",450000)
print(BankAccount.__doc__)
obj.display_balance()"""
"""This above code is of this question
Create a class BankAccount
Add a class docstring explaining what the class does.
Create:
Constructor with name and balance
Method display_balance()
Then use:
print(BankAccount.__doc__)
to display the docstring."""

"""class Employee:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
    def display_details(self):
        print("name",self.name,"age",self.age,"role",self.role)
obj1=Employee("gugu",26,"pulmber")
obj2=Employee("Alen",45,"HR")
obj1.display_details()
obj2.display_details()"""


"""class Calculator:
    def add(self,num1,num2):
        return(num1+num2)
    def sub(self,num1,num2):
        return(num1-num2)
    def mul(self,num1,num2):
        return(num1*num2)
obj=Calculator()
print(obj.add(num1=1,num2=2),obj.sub(num1=3,num2=2),obj.mul(num1=2,num2=3),sep=",")"""

"""class login():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self):
        print("username",self.username)
        print("password",self.password)
obj=login("isha","isha@12345")
obj.login()"""

"""class BankAccount:
    "This class represents a bank details"
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display_balance(self):
        print("name",self.name,"balance",self.balance)
obj=BankAccount("isha",4500)
print(BankAccount.__doc__)
obj.display_balance()"""

"""class Employee:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
    def display_details(self):
        print("name",self.name,"age",self.age,"role",self.role)
obj1=Employee("gugu",26,"pulmber",)
obj2=Employee("Alen",45,"HR")
obj1.display_details(),obj2.display_details()"""

"""class student:
    def __init__(self,name):
        self.name=name
obj1=student("isha")
obj2=student("satya")
print(obj1.name,obj2.name)"""

"""class employee:
    def __init__(self,name,company):
        self.name=name
        self.company=company
obj1=employee("gugu","indium")
obj2=employee("satya","Sila")
print(obj1.name,obj1.company,obj2.name,obj2.company)"""

"""class car:
    company="Toyata"
    def __init__(self,model,price):
        self.model=model
        self.price=price
obj1=car("fortuner",1000000)
obj2=car("Suzuki","5000000")
print(obj1.model,obj1.price,obj2.model,obj2.price)"""

"""class Mobile:
    brand="Vivo"
    def __init__(self,model,price):
        self.model=model
        self.price=price
mobile1=Mobile("y31pro",50000)
mobile2=Mobile("s24",60000)
print(mobile1.brand,mobile1.model,mobile1.price)
print(mobile2.brand,mobile2.model,mobile2.price)"""

"""class Employee:
    company="Indium software"
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
obj=Employee()
obj.change_company("Google")
print(Employee.company)"""

"""class Employee:
    def __init__(self,name):
        self.name=name
obj=Employee("gugu")
print(obj.name)"""

"""class Employee:
    company="Indium software"
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
emp=Employee()
emp.change_company("Google")
print(emp.company)

class Employee:
    company="Indium software"
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
isha=Employee()
isha.change_company("Microsoft")
print(isha.company)"""

"""class Employee:
    company="Indium software"
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
isha=Employee()
isha.change_company("Microsoft")
print(isha.company)"""

"""class Mobile:
    brand="Vivo"
    @classmethod
    def change_brand(cls,new_brand):
        cls.brand=new_brand
gunu=Mobile()
gunu.change_brand("Apple")
print(gunu.brand)"""

"""class Employee:
    company="Indium software"
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
dungu=Employee()
dungu.change_company("Microsoft")
print(dungu.company)
dungu.change_company("Apple")
print(dungu.company)"""


"""class Employee:
    company="Indium Software"
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def display_details(self):
        print(self.name,self.role,self.company)
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company
emp1=Employee("satyajit","developer")
emp2=Employee("isha","Tester")
Employee.change_company("Google")
emp1.display_details()
emp2.display_details()"""

"""class Employee:
    salary=27000
    @classmethod
    def increase_salary(cls,new_salary):
        cls.salary=new_salary

Employee.increase_salary(28000)
print(Employee.salary)"""


"""class Employee:
    @staticmethod
    def calculate_bonus(salary):
        return salary*10/100
print(Employee.calculate_bonus(40000))"""


"""class Employee:
    @staticmethod
    def check_salary(salary):
        if salary >=30000:
            return "Good salary"
        else:
            return "needs to improvement"
print(Employee.check_salary(29000))"""










    



























































































































































































