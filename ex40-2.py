# 2016 vistacourt software
# tom kelly

class Add(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def thing(self):
        return self.x * self.y


result = Add(2, 2)

print(result.thing())
