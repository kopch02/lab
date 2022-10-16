class mylist(list):

    def __init__(self, standart):
        super().__init__(self)
        self.standart = standart

    def __getitem__(self, a):
        try:
            return super().__getitem__(a)
        except IndexError:
            return self.standart


test = mylist("standart")
test.append(10)
test.append(11)
test.append(12)
test.append(13)

print(test[10])
print(test[0])
print(test[3])
