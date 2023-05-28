class IsDivisible:

    def __init__(self, divList):
        self.divisors = divList

    def byAll(self, inputInt):
        self.input = inputInt
        divisibleByAll = True
        for item in self.divisors:
            if self.input % item[0] == 0:
                continue
            else:
                divisibleByAll = False
                break
        if divisibleByAll:
            return "Testing"
        return None

    def byOne(self, inputInt):
        self.input = inputInt
        for item in self.divisors:
            if self.input % item[0] == 0:
                return item[1]
        return None
