class IsDivisible:

    def __init__(self, inputInt, divList):
        self.input = inputInt
        self.divisors = divList

    def byAll(self):
        divisibleByAll = True
        for item in self.divisors:
            if self.input % item[0] == 0:
                continue
            else:
                divisibleByAll = False
        if divisibleByAll:
            return "Testing"
        return None

    def byOne(self):
        for item in self.divisors:
            if self.input % item[0] == 0:
                return item[1]
        return None
