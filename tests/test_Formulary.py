class class_test:
    def __init__(self, value):
        self.value = value

    def class_method(self, arg=None):
        if arg is None:
             arg = self.value
        return arg

a_class = class_test(5)

default_value = a_class.class_method()
print(default_value)