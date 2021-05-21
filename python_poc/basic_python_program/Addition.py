

class addition_class:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.print_result()

    def addition(self):
        c = self.a +self. b
        return "Addition of {} and {} is :{}".format(self.a, self.b, c)

    def print_result(self):
        result =self.addition()
        print(result)


if __name__ == '__main__':
    addition_class_object = addition_class(123,456)


