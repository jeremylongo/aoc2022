from __future__ import annotations


class Monkey:
    idx = 0
    starting_items = []
    operation = None
    divider = 0
    predivider = 1
    target_true = None
    target_false = None
    inspect_items_count = 0

    def __init__(self, idx, starting_items: list, operation, divider: int):
        self.idx = idx
        self.starting_items = starting_items
        self.operation = operation
        self.divider = divider

    def set_targets(self, target_true: Monkey, target_false: Monkey):
        self.target_true = target_true
        self.target_false = target_false

    def add_item(self, item: int):
        self.starting_items.append(item)

    def print_score(self):
        print("Monkey ", self.idx, ": ", self.starting_items)
        print("Monkey ", self.idx, ": ", self.inspect_items_count)

    def get_score(self):
        return self.inspect_items_count

    def set_predivider(self, divider):
        self.predivider = divider

    def process(self):
        for i in range(len(self.starting_items)):
            self.inspect_items_count += 1
            item = self.starting_items[i]
            # print("  Monkey inspects an item with a worry level of ", item, ".")
            v = self.operation(item)
            v = v % self.predivider
            # print("     New worry level of item : ", v)
            if v % self.divider == 0:
                # print("     Throw to monkey true")
                self.target_true.add_item(v)
            else:
                # print("     Throw to monkey false")
                self.target_false.add_item(v)
        self.starting_items = []

def build_common_divider(monkeys):
    i = 1
    for monkey in monkeys:
        i = i * monkey.divider
    for monkey in monkeys:
        monkey.set_predivider(i)
    print("predivider = ", i)

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

build_common_divider(monkeys)

for i in range(1, 10001):
    if i % 1000 == 0:
        print("Round ", i)
    for monkey in monkeys:
        monkey.process()

    if i % 1000 == 0:
        for monkey in monkeys:
            monkey.print_score()

monkeys.sort(key=lambda m: m.get_score(), reverse=True)

monkey_business = monkeys[0].get_score() * monkeys[1].get_score()
print(monkey_business)