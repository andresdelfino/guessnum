class InvalidAnswers(Exception):
    pass


class NumberGuesser:
    def __init__(self, min_n, max_n):
        self.min_n = min_n
        self.max_n = max_n

        self.max_n_bin_len = len(bin(self.max_n)) - 2

        self.bin_list = []
        for n in range(self.min_n, self.max_n + 1):
            self.bin_list.append(bin(n)[2:].rjust(self.max_n_bin_len, '0'))

        self.guess = []

    def get_tables(self):
        for position in range(self.max_n_bin_len - 1, -1, -1):
            table = []
            for n in self.bin_list:
                if n[position] == '1':
                    table.append(int(n, 2))
            yield table

    def store_response(self, response):
        if response:
            self.guess.append('1')
        else:
            self.guess.append('0')

    def guess_number(self):
        guess = int(''.join(reversed(self.guess)), 2)

        if not (self.min_n <= guess <= self.max_n):
            raise InvalidAnswers

        return guess
