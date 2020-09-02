class Toy:
    def __init__(self,color,age):
        self.color = color
        self.age    = age

    def __str__(self):
        return "Hello World"

    def __sizeof__(self):
        return 10

    def __hash__(self):
        return "ABC"

    def __dir__(self):
        return "Current DIR"
action_figure = Toy('red',0)
print(action_figure.__str__())
print(action_figure.__sizeof__())
print(action_figure.__hash__())
print(action_figure.__dir__())
