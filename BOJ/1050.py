import sys

input = sys.stdin.readline


class Item:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.ingre_units = []
        self.total = False
        self.subsum = 0

    def transform_equation_to_ingredients(self, equation):
        value = 0
        word = []
        for i in equation:
            asc = ord(i)
            if 49 <= asc <= 57:
                value = int(chr(asc))
            elif 65 <= asc <= 90:
                word.append(i)
            elif asc == 43:
                word = "".join(word)
                try:
                    idx = self.ingredients.index(word)
                    self.ingre_units[idx] += value
                except ValueError:
                    self.ingredients.append(word)
                    self.ingre_units.append(value)
                value = 0
                word = []
        word = "".join(word)
        try:
            idx = self.ingredients.index(word)
            self.ingre_units[idx] += value
        except ValueError:
            self.ingredients.append(word)
            self.ingre_units.append(value)

    def get_total(self, ingredients, ingre_values):
        del_list = []
        item_idx = 0
        for item in self.ingredients:
            try:
                idx = ingredients.index(item)
                self.subsum += ingre_values[idx] * self.ingre_units[item_idx]
                del_list.append(item)
            except ValueError:
                pass
            item_idx += 1
        for del_item in del_list:
            idx = self.ingredients.index(del_item)
            del self.ingredients[idx]
            del self.ingre_units[idx]
        if not self.ingredients:
            self.total = self.subsum
        return self.total

    def item_to_ingredient(self, ingredients, ingre_values):
        if self.total:
            ingredients.append(self.name)
            ingre_values.append(self.total)

    def __repr__(self):
        return self.name


def main():
    N, M = map(int, input().split())
    ingredients = []
    ingre_values = []
    not_yet_ingre = []
    for n in range(N):
        ingre, unit = input().split()
        try:
            index = ingredients.index(ingre)
            ingredients[index] += int(unit)
        except ValueError:
            ingredients.append(ingre)
            ingre_values.append((int(unit)))

    for m in range(M):
        input_equation = input()
        name = []
        i = 0
        for ch in input_equation:
            word = ord(ch)
            if 65 <= word <= 90:
                name.append(ch)
            elif word == 61:
                name = "".join(name)
                equation = input_equation[i + 1:]
                new_item = Item(name)
                new_item.transform_equation_to_ingredients(equation)
                if new_item.get_total(ingredients, ingre_values):
                    new_item.item_to_ingredient(ingredients, ingre_values)
                else:
                    not_yet_ingre.append(new_item)
                break
            i += 1
    while not_yet_ingre:
        try:
            ingredients.index("LOVE")
            break
        except ValueError:
            del_list = []
            for item in not_yet_ingre:
                if item.get_total(ingredients, ingre_values):
                    item.item_to_ingredient(ingredients, ingre_values)
                    del_list.append(item)
            for item in del_list:
                not_yet_ingre.remove(item)
    ans = ingre_values[ingredients.index("LOVE")]
    print(1000000001 if ans > 1000000000 else ans)


main()
