from dataclasses import dataclass

# ref Example_Class_Channel_Time.py for a usage of @dataclass & @classmethod
"""
The @dataclass decorator is used to automatically generate 
special methods, such as __init__, __repr__, __eq__, and others, 
for a class. It simplifies the process of creating classes 
that are primarily used for storing data.
"""

@dataclass
class MyClass:
    class_attr: int = 0
    instance_attr: int = 0

    def instance_method(self):
        print("Instance method called.")
        print("Instance attribute:", self.instance_attr)
        print("Class attribute:", self.class_attr)

    '''
    The purpose of using the class decorator @classmethod in the 
    previous code is to define a method that operates on the class 
    itself rather than on an instance of the class. When a method 
    is decorated with @classmethod, it receives the class itself 
    as the first argument instead of an instance (usually named 
    cls conventionally). This allows the method to access and 
    modify class-level attributes or perform operations related 
    to the class.
    '''
    @classmethod
    def class_method(cls):
        print("Class method called.")
        print("Class attribute:", cls.class_attr)

# Regular instance method requires an instance of the class to call.
obj = MyClass(42,2)
obj.instance_method()

# Class method can be called on the class itself, without creating an instance.
MyClass.class_method()


