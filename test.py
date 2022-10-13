class Test():
    def __init__(self, t) -> None:
        self.t = t

    def update(self):
        self.t.append("b")


a = ["a"]
test = Test(a)
print(a)
test.update()
print(a)