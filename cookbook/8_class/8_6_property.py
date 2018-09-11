class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Delete fucntion(optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from exiting get/set methods
    name = property(get_first_name, set_first_name, del_first_name)

# 后续是测试部分代码
name = input('input first_name here: ')
#
person1 = Person(name)
print('name is :' + person1.name)
