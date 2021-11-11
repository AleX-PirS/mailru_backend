class ModifiedList(list):
    """Модифицированный список"""
    # Перегрузка оператора +
    def __add__(self, other):
        new_mod_lst = ModifiedList([])
        min_len = min(len(self), len(other))
        new_mod_lst.extend([x + y for x, y in zip(self[:min_len], other[:min_len])])
        new_mod_lst.extend(self[min_len:])
        new_mod_lst.extend(other[min_len:])
        return new_mod_lst

    # Перегрузка отраженного оператора +
    def __radd__(self, other):
        return self + ModifiedList(other)

    # Перегрузка оператора -
    def __sub__(self, other):
        new_mod_lst = ModifiedList([])
        min_len = min(len(self), len(other))
        new_mod_lst.extend([x - y for x, y in zip(self[:min_len], other[:min_len])])
        new_mod_lst.extend(self[min_len:])
        new_mod_lst.extend([x - y for x, y in zip([0] * len(other[min_len:]), other[min_len:])])
        return new_mod_lst

    # Перегрузка отраженного оператора -
    def __rsub__(self, other):
        return ModifiedList(other) - self

    # Перегрузка оператора ==
    def __eq__(self, other):
        return sum(self) == sum(other)

    # Перегрузка оператора <=
    def __le__(self, other):
        return sum(self) <= sum(other)

    # Перегрузка оператора >=
    def __ge__(self, other):
        return sum(self) >= sum(other)

    # Перегрузка оператора !=
    def __ne__(self, other):
        return sum(self) != sum(other)

    # Перегрузка оператора <
    def __lt__(self, other):
        return sum(self) < sum(other)

    # Перегрузка оператора >
    def __gt__(self, other):
        return sum(self) > sum(other)
