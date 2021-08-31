from random import randint, choice, uniform


class Generator:
    def __init__(self, count=3, same_len=1, min_len=10, max_len=30):
        """

        :type count: int

        :param same_len: count of sequences with repeated length

        :type same_len: int

        :type min_len: int

        :type max_len: int
        """
        if same_len > count:
            raise Exception("Количество списков с одинаковой длиной"
                            " не может быть больше обшего количества")
        self.__count = count
        self.__same_len = same_len
        self.__lists = list()
        self.__max_seq_len = max_len
        self.__min_seq_len = min_len

    def fill_list(self, source_list):
        """заполняет список случайными значениями"""
        for counter in range(randint(self.__min_seq_len,
                                     self.__max_seq_len)):
            value = choice([
                randint(1, 100) * choice((1, -1)),
                round(uniform(1, 100), 2) * choice((1, -1))
            ])
            source_list.append(value)

    @staticmethod
    def randomize_values(source_list):
        """заменяет элементы списка на случайные"""
        for index, _ in enumerate(source_list):
            source_list[index] = choice([
                randint(1, 100) * choice((1, -1)),
                round(uniform(1, 100), 2) * choice((1, -1))
            ])

    def generate(self):
        """ Генерирует список списков"""
        # сначала случайная длина
        for ind in range(self.__count - self.__same_len):
            new_list = []
            self.fill_list(new_list)
            self.__lists.append(new_list)

        counter = 0
        # затем с той же длиной что и у первых случайных (повторение по очереди)
        for ind in range(self.__count - self.__same_len, self.__count):
            new_list = [0] * len(self.__lists[counter])
            Generator.randomize_values(new_list)
            self.__lists.append(new_list)
            counter = (counter + 1) % len(self.__lists)

        return self.__lists
