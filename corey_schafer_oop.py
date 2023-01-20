# Python OOP

import datetime


class Employee:
    """This is the name of the class. By convention, a class name begins with 
    a capital letter
    """

    """Below are class variables. 
    A class variable in Python is a type of variable that is shared among all
    instances of a particular class. These variables are defined at the class
    level, rather than within individual methods or instances. This means that
    any changes made to a class variable will be reflected in all instances of
    that class. Class variables are typically used to store information that is
    common to all instances of a class, such as configuration settings or
    constant values.
    """
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        """The __init__ method is used to initialise an object in python when
        it is created and is similar to a constructor in other programming
        languages.

        The `self` parameter is the first argument and refers to the current
        instance of the object.
        """

        # Assigning attributes to the instance of the class
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = f"{first}.{last}@company.com"
        # Email changed to a @property at the end of the class

        """Incrementing the class variable `num_of_employees` by 1 each time a 
        new Employee class is initialised. This 
        """
        Employee.num_of_employees += 1

    def fullname(self):
        """A "regular method" for a class. These ALWAYS take the instance as
        the first argument, in this case that is `self`. These methods are
        used to access or modify the data or attributes for an instance of
        a class.
        """
        return f"{self.first} {self.last}"

    def apply_raise(self):
        """A "regular method" using a class variable to modify an attribute.
        """
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        """A class method in Python is a method that is bound to the class,
        rather than to an instance of the object. It is defined using the
        @classmethod decorator and takes the cls parameter as the first
        argument, which refers to the class itself. Class methods are typically
        used to define methods that operate on the class, such as factory
        methods that create new instances of the class, or to change the class
        level attributes or return class level information. They can be called
        on both the class and its instances, but when called on an instance,
        the instance is ignored and the class level attribute is used.
        """
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_string):
        """A class method can also be used to create an alternative
        constructor. In this example, the instance attributes are separated
        by a hyphen instead of being separate variables. This alternative
        constructor will split the employee details into separate variables and
        return a newly created instance of the class.
        """
        first, last, pay = employee_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """A static method is a method that has a logical connection to the
        class but does not depend on either an instance or class variable.
        If you aren't using `self` or `cls` then the method should be a static
        method.

        In this example, using the datetime package to determine if a date is
        a workday (Mon-Fri).
        """
        if day.weekday() == 5 or day.weekday() == 6:  # 5 is Sat, 6 is Sun
            return False
        return True

    """Below are examples of Special/Magic/Dunder methods. All different names
    for the same thing. These methods are used to define how built-in Python 
    functions or operators should behave when applied to an instance of a 
    user-defined class. These two dunder methods, along with __init__ are the 
    most common to be implemented. Others can be found in the documentation
    https://docs.python.org/3/reference/datamodel.html#special-method-names
    """

    def __repr__(self):
        """The __repr__ method is meant to be an unambiguous representation of
        the object. This should be used for tasks like debugging and logging,
        and should be seen by developers. You should aim to have the output
        display as something you could copy and paste into a terminal and have
        it should evaluate as a valid line of code.

        This example in particular will return a line of code to instantiate
        an Employee class and recreate the object.
        """
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        """The __str__ method is meant to be used as a display for the end user
        and is therefore a little more arbitrary.

        This particular example will return readable information about the
        employee.
        """
        return f"{self.fullname()} - {self.email}"

    @property
    def email(self):
        """The @property decorator allows us to define email in the class like
        it is a method, but we can access email like it is an attribute (ie
        no parenthesis at the of the call). Changing email from an attribute
        to a method with a @property decorator allows us to change the first
        or last variables and the email will be updated AND the code won't
        require changing.

        If a method was created without the @property decorator, then you would
        have to put parenthesis at the end of each call in the code which would
        be prone to errors, simply missing one.
        """
        return f"{self.first}.{self.last}@company.com"

    @property
    def name_change(self):
        """The original tutorial stripped down a lot of code and changed the
        fullname method to include a @property decorator. I didn't want to
        do that because I wanted to preserve the original , so I have created a new method.
        """
        return f"{self.first} {self.last}"

    @name_change.setter
    def name_change(self, name):
        """A method with the @setter decorator must have the same name as the
        method with the @property decorator. This method is used to "set" the
        attributes in the @property decorator.
        """
        first, last = name.split(" ")
        self.first = first
        self.last = last


class Developer(Employee):
    """This is a subclass of the Employee class. Employee is a superclass of
    Developer. his means that the Developer class inherits all the attributes
    and methods of the Employee class and can also define its own attributes
    and methods.
    """

    """Below is an example of attribute overriding. Developer inherits the
    value from Employee, but uses its own class variable instead because
    the subclass's attributes and variables have precedence in the method
    resolution order.
    """
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        """Creating an __init__ method for the subclass. In this example the
        __init__ method is the same as the superclass but with the added
        attribute prog_lang. So we don't have to repeat ourselves, we can call
        the superclass' __init__ method to handle first, last and pay. We then
        handle prog_lang the same as we normally would.
        """
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    """Another example of a subclass"""

    def __init__(self, first, last, pay, employees=None):
        """This __init__ method passes in a list, the contents are unimportant.
        What is important is a list is a mutable object, and in this particular
        case has a default value of None. This needs to be checked and an
        empty list created each time a new Manager class is instantiated.
        """
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        """Method to add an employee to a supervisor."""
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        """Method to remove an employee to a supervisor."""
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        """Method to print the supervisor's employees"""
        for employee in self.employees:
            print(f"--> {employee.fullname()}")


"""Creating two instances of the Employee class"""
emp_1 = Employee("Adam", "Wicks", 50000)
emp_2 = Employee("Test", "User", 60000)

"""Printing the the raise amounts in different ways"""
print("Printing the raise amounts")
print(Employee.raise_amount)  # Using the Class to access a class variable
print(emp_1.raise_amount)  # Accessing the class variable from the instance
print(emp_2.raise_amount)

"""Modifying a class variable using a class method"""
print("\nModifying the raise_amount class variable and printing to see the "
      "results")
Employee.set_raise_amount(1.05)  # Changing the raise amount to 5%
# Printing in different ways to show the change
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""Using the alternative constructor to create a new instance of the Employee 
class"""
print("\nUsing the alternative constructor to create new employees")
# Creating some employee details, separated by hyphens
emp_string_3 = "John-Doe-70000"
emp_string_4 = "Steve-Smith-30000"
emp_string_5 = "Jane-Doe-90000"

# Using the alternative constructor to create Employee classes
emp_3 = Employee.from_string(emp_string_3)
emp_4 = Employee.from_string(emp_string_4)
emp_5 = Employee.from_string(emp_string_5)

# Printing details
print(emp_3.email)
print(emp_3.pay)

"""Using the static method to check if the provided date is a workday"""
example_date_1 = datetime.date(2022, 12, 7)  # Wednesday
example_date_2 = datetime.date(2022, 10, 15)  # Saturday

print("\nUsing the static method to check workdays")
print(f"7/12/2022 (Wednesday): {Employee.is_workday(example_date_1)}")
print(f"15/10/2022 (Saturday): {Employee.is_workday(example_date_2)}")

"""Demonstrating the use of subclasses"""
# Creating an instance of the Developer class
dev_1 = Developer("Alan", "Turing", 100000, "Machine Language")
print("\nCreating a Developer subclass and demonstrating inheritance")
print(f"Email: {dev_1.email}")
print(f"Programming Language: {dev_1.prog_lang}")

# Using the subclass's attribute override, but using an inherited method
print("\nRaising pay using attribute override and method inheritance")
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

# Creating an instance of the Manager class
mgr_1 = Manager("Sue", "Smith", 90000, [emp_1, emp_2, emp_3])
print("\nCreating a Manager subclass and demonstrating inheritance")
print(f"Email: {mgr_1.email}")

# Testing the Manager class methods
print(f"\nTesting the class methods")
mgr_1.print_employees()
mgr_1.add_employee(dev_1)
print("\nAdd a Developer to the team")
mgr_1.print_employees()
print("\nRemove an employee from the team")
mgr_1.remove_employee(emp_1)
mgr_1.print_employees()

# Using the insintance() function
print("\nUsing the isinstance() function")
print(f"Is mgr_1 an employee: {isinstance(mgr_1, Employee)}")
print(f"Is mgr_1 a manager: {isinstance(mgr_1, Manager)}")
print(f"Is mgr_1 a developer: {isinstance(mgr_1, Developer)}")

# Using the issubclass() function
print("\nUsing the issubclass() function")
print(f"Employee, Employee: {issubclass(Employee, Employee)}")
print(f"Manager, Employee: {issubclass(Manager, Employee)}")
print(f"Manager, Manager: {issubclass(Manager, Manager)}")
print(f"Manager, Developer: {issubclass(Manager, Developer)}")
print(f"Employee, Manager: {issubclass(Employee, Manager)}")

# Using the special methods in the Employee class
print("\nUsing the special methods of the Employee class")
print(f"__repr__ output: {repr(emp_1)}")
print(f"__str__ output: {emp_1}")  # Output is the same as str(emp_1)

# Using the class decorators to change emp_3's details
print("\nJohn Doe's details")
print(f"First: {emp_3.first}")
print(f"Email: {emp_3.email}")
print(f"Fullname: {emp_3.fullname()}")
print("\nJohn Doe has decided to change his name.")
emp_3.name_change = "Joe Bloggs"
print(f"First: {emp_3.first}")
print(f"Email: {emp_3.email}")
print(f"Fullname: {emp_3.fullname()}")

