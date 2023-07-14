class EncryptData:
    alphabet = [sym for sym in """АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя
                                  AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz
                                  .,?!:;-'"()[]{}<>
                                  01 23456789"""]
    magic_square = [[15, 2, 1, 12],
                    [4, 9, 10, 7],
                    [8, 5, 6, 11],
                    [3, 14, 13, 0]]

    def __init__(self, data):
        self._data: str = data

    async def port_encrypt(self):
        source = [self._data[i:i + 2] for i in range(0, len(self._data), 2)]
        if len(source[-1]) == 1:
            source[-1] += "Я"
        self._data = ""
        for letterPair in source:
            ind = self.alphabet.index(letterPair[0]) * len(self.alphabet)
            ind += self.alphabet.index(letterPair[1])
            self._data += str(ind) + ' '
        self._data.rstrip()

    async def port_decrypt(self):
        data = [int(el) for el in self._data.split()]
        self._data = ""
        for num in data:
            self._data += str(self.alphabet[num // len(self.alphabet)])
            self._data += str(self.alphabet[num % len(self.alphabet)])

    async def magic_square_enc_dec(self):
        data = ""
        for i in range(len(self.magic_square)):
            for j in range(len(self.magic_square[i])):
                try:
                    data += self._data[self.magic_square[i][j]]
                except IndexError:
                    data += "."
        self._data = data

    @property
    def data(self):
        return self._data
