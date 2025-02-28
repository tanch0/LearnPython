# from datetime import datetime


# class Dog:
#     """
#     A class that represents a dog, which has attributes like name, breed, and owner.
#     It also has a method to make the dog bark, providing details of the dog.
#     """

#     def __init__(self, name: str, breed: str, owner: object):
#         """
#         The constructor method that initializes the class with the provided values
#         when a new Dog object is created.
#         self help to point the attributes of the class from wehere it is instantiated
#         """
#         self.name = name  # Instance attribute: name of the dog
#         self.breed = breed  # Instance attribute: breed of the dog
#         self.owner = owner  # Instance attribute: reference to the owner's object

#     def intro(self):
#         """
#         A method that allows the dog to bark, printing its name and breed.
#         This method is an example of behavior (barking) associated with the dog object.
#         """
#         print(f"Dog name is {self.name} and its breed is {self.breed}")


# class Owner:
#     def __init__(self, name, age):
#         """
#         The constructor for creating an Owner object with attributes: name and age.
#         """
#         self.age = age  # Instance attribute: age of the owner
#         self.name = name  # Instance attribute: name of the owner

#     def intro(self):
#         """
#         A method that prints the introduction of the owner, providing their name and age.
#         """
#         print(f"Hey, my name is {self.name} and my age is {self.age}")


# owner1 = Owner("Tancho", 21)  # Instantiate an Owner object
# dog = Dog(
#     "Lucy", "Japanese Speetch", owner1
# )  # Instantiate a Dog object and assign owner1 as the dog owner

# print(
#     dog.owner.age
# )  # Accesses the 'owner' attribute of the 'dog' object, then accesses 'age' from 'owner1'

# dog.intro()


# # --------------------------------------------------------------------------------------------------------------------------------


# # getter and setter method
# # _ indicates protected and __ indicates private - variables, "Consenting adults philosophy"
# # protected can still be accessed outside the class, just follow the convention as a good developer unless it is necessary
# class User:
#     def __init__(self, name, address, age):
#         self.name = name
#         self.__address = address  # Making address private by using double underscores
#         self.age = age

#     def say_hi_to(self, user):
#         print(
#             f"Hey {user.name} this is me {self.name} I'm from {self.__address} are you from {user.__address}"
#         )

#     # Getter method for the private attribute
#     def get_address(self):
#         print(f"Address accessed at {datetime.now()}")
#         return self.__address

#     # Setter method for the private attribute (if you want to allow modification safely)
#     def set_address(self, new_address):
#         if len(new_address) > 2:
#             self.__address = new_address
#         print("Lenght of address should be greater than 2")


# user1 = User("Ram", "Kathmandu", 22)
# user2 = User("Laxman", "Jhapa", 24)

# user1.say_hi_to(user2)

# # Trying to directly modify the private attribute (this will raise an error)
# # user2.__address = "Ilam"  # This will raise an AttributeError

# # Use the setter method to modify the private attribute instead
# user2.set_address("I")

# user1.say_hi_to(user2)

# # To access the private attribute, we need to use the getter method:
# print(user2.get_address())


# # --------------------------------------------------------------------------------------------------------------------------------
# # Properties


# class Customer:
#     def __init__(self, email, password):
#         self._email = email
#         self.password = password

#     @property
#     def email(self):
#         print(f"email have been accessed")
#         return self._email

#     @email.setter
#     def email(self, new_email):
#         if "@" in new_email:
#             self._email = new_email


# customer1 = Customer("customer@gmail.com", "123456")
# print(customer1.email)
# customer1.email = "updated@gmail.com"
# print(customer1._email)


# # --------------------------------------------------------------------------------------------------------------------------------
# # Static attributes: static attributes are alse called class attributes which is directly accessible from class level
# # Eg: ClassName.attr_name


# class Vehicle:
#     vechicle_count = 0

#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#         Vehicle.vechicle_count += 1

#     def model_info(self):
#         print(f"Car name is {self.name} and its model is: {self.model}")


# vehicle1 = Vehicle("volvo", "volvo-xyz")
# vehicle2 = Vehicle("Ferrati", "ferari-452")

# print(Vehicle.vechicle_count)
# print(vehicle1.vechicle_count)


# --------------------------------------------------------------------------------------------------------------------------------
# Static method


class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            print(
                f"Previous balace was {self.__balance - amount} and new balace is {self.__balance} for customer: {self.name}"
            )
        else:
            print(f"INVALID AMOUNT: {amount}")

    @staticmethod
    def is_valid_interest(rate):
        return 0 <= rate <= 5


customer1 = BankAccount("Ram", 500)
customer1.deposit_balance(100)
print(customer1.is_valid_interest(5))
print(BankAccount.is_valid_interest(7))
print(BankAccount.is_valid_interest(5))
