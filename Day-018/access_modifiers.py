class Demo:

    def __init__(self):

        self.public = "Public Variable"

        self._protected = "Protected Variable"

        self.__private = "Private Variable"

obj = Demo()

print(obj.public)

print(obj._protected)

# print(obj.__private)   # Error