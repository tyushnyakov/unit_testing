import math

from functools import reduce
from itertools import zip_longest

from list_generator import Generator


class MathList:

    @staticmethod
    def check_correct(list_val):
        """

        :type list_val:
        :return:
        """
        for element in list_val:
            if not (isinstance(element, int) or
                    isinstance(element, float)):
                raise ValueError("Элементы списка должны"
                                 " быть числами")

    def __init__(self, list_val):
        MathList.check_correct(list_val)
        self.value = list_val.copy()

    def __str__(self):
        temp_str = ','.join([str(x) for x in self.value])
        return f"MathList({temp_str})"

    def __len__(self):
        return len(self.value)

    def __add__(self, other):
        if isinstance(other, MathList):
            result = []
            for index, element in enumerate(zip_longest(self.value,
                                                        other.value,
                                                        fillvalue=0)):
                result.append(element[0] + element[1])
            return MathList(result)
        else:
            raise NotImplementedError

    def __neg__(self):
        return MathList(
            [-elem for elem in self.value]
        )

    def __sub__(self, other):
        if isinstance(other, MathList):
            return self + (- other)
        else:
            raise NotImplementedError

    def __mul__(self, other):
        if isinstance(other, MathList):
            result = []
            for index, element in enumerate(zip_longest(self.value,
                                                        other.value,
                                                        fillvalue=1)):
                result.append(element[0] * element[1])

            return MathList(result)
        else:
            raise NotImplementedError

    def reverse(self):
        """ Переворачивает элементы нашей последовательности"""
        return MathList(
            [1 / elem for elem in self.value]
        )

    def __truediv__(self, other):
        if isinstance(other, MathList):
            return self * other.reverse()
        else:
            raise NotImplementedError

    def add(self, element):
        """добавление элемента в список"""
        if (isinstance(element, int) or
                isinstance(element, float)):
            self.value.append(element)
        else:
            raise ValueError("Элемент должен"
                             " быть числом")

    def remove(self, element):
        """удаление элемента из списка"""
        if element in self.value:
            self.value.remove(element)
        else:
            print("В последовательности нет"
                  f" элемента {element}")

    def update(self, new_list):
        """расширение списка элементами другого списка"""
        MathList.check_correct(new_list)
        self.value.extend(new_list)

    def distance(self, new_list):
        """расстояние между списками"""
        if (isinstance(new_list, MathList) and
                len(self) == len(new_list)):
            elem_summ = reduce(lambda x, y: x + y,
                               [(elemnt[0] - elemnt[1]) ** 2
                                for elemnt in zip(
                                   self.value,
                                   new_list.value
                               )
                                ])
            result = math.sqrt(elem_summ)
            return result
        else:
            raise NotImplementedError


# Проверка
generator = Generator()

# Создание объектов
test_list1, test_list2, test_list3 = generator.generate()

list1 = MathList(test_list1)
list2 = MathList(test_list2)
list3 = MathList(test_list3)

# Добавление, удаление, обновление элементов

# Вывод объектов
print("Список1", list1, "\n")
print("Список2", list2, "\n")
print("Список3", list3, "\n")

# Операции
print("Сумма:", list1 + list2, "\n")
print("Разность:", list1 - list2, "\n")
print("Умножение:", list1 * list2, "\n")
print("Деление:", list1 / list2, "\n")

print(list1.distance(list3))

try:
    print(list1.distance(list2))
except NotImplementedError:
    print("Расстояние между списками разной длины невычислимо!")
