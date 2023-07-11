class Monkey:
    idx = 0
    starting_items = []
    operation = None
    divider = 0
    target_true = None
    target_false = None
    inspect_items_count = 0

    def __init__(self, idx, starting_items, operation, divider):
        self.idx = idx
        self.starting_items = starting_items
        self.operation = operation
        self.divider = divider

    def set_targets(self, target_true, target_false):
        self.target_true = target_true
        self.target_false = target_false

    def add_item(self, item):
        self.starting_items.append(item)

    def print_item(self):
        print("Monkey ", self.idx, ": ", self.starting_items)

    def get_score(self):
        return self.inspect_items_count

    def process(self):
        while len(self.starting_items) > 0:
            self.inspect_items_count += 1
            item = self.starting_items[0]
            print("  Monkey inspects an item with a worry level of ", item, ".")
            v = self.operation(item)
            print("     New worry level of item : ", v)
            v = v // 3
            print("     Divided worry level of item : ", v)
            if v % self.divider == 0:
                print("     Throw to monkey true")
                self.target_true.add_item(v)
            else:
                print("     Throw to monkey false")
                self.target_false.add_item(v)
            del (self.starting_items[0])


monkeys = []
# monkeys.append(Monkey(0, [79, 98], lambda a: a * 19, 23))
# monkeys.append(Monkey(1, [54, 65, 75, 74], lambda a: a + 6, 19))
# monkeys.append(Monkey(2, [79, 60, 97], lambda a: a * a, 13))
# monkeys.append(Monkey(3, [74], lambda a: a + 3, 17))
#
# monkeys[0].set_targets(monkeys[2], monkeys[3])
# monkeys[1].set_targets(monkeys[2], monkeys[0])
# monkeys[2].set_targets(monkeys[1], monkeys[3])
# monkeys[3].set_targets(monkeys[0], monkeys[1])

monkeys.append(Monkey(0, [99, 63, 76, 93, 54, 73], lambda a: a * 11, 2))
monkeys.append(Monkey(1, [91, 60, 97, 54], lambda a: a + 1, 17))
monkeys.append(Monkey(2, [65], lambda a: a + 7, 7))
monkeys.append(Monkey(3, [84, 55], lambda a: a + 3, 11))
monkeys.append(Monkey(4, [86, 63, 79, 54, 83], lambda a: a * a, 19))
monkeys.append(Monkey(5, [96, 67, 56, 95, 64, 69, 96], lambda a: a + 4, 5))
monkeys.append(Monkey(6, [66, 94, 70, 93, 72, 67, 88, 51], lambda a: a * 5, 13))
monkeys.append(Monkey(7, [59, 59, 74], lambda a: a + 8, 3))

monkeys[0].set_targets(monkeys[7], monkeys[1])
monkeys[1].set_targets(monkeys[3], monkeys[2])
monkeys[2].set_targets(monkeys[6], monkeys[5])
monkeys[3].set_targets(monkeys[2], monkeys[6])
monkeys[4].set_targets(monkeys[7], monkeys[0])
monkeys[5].set_targets(monkeys[4], monkeys[0])
monkeys[6].set_targets(monkeys[4], monkeys[5])
monkeys[7].set_targets(monkeys[1], monkeys[3])


for i in range(1, 21):
    print("Round ", i)
    for monkey in monkeys:
        monkey.process()

    for monkey in monkeys:
        monkey.print_item()

monkeys.sort(key=lambda m: m.get_score(), reverse=True)

monkey_business = monkeys[0].get_score() * monkeys[1].get_score()
print(monkey_business)