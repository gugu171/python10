class KOMPUTER:
    def __init__(self):
        self.__maxprice = 24000
    def sell(self):
        print("LE SELING PREYECE IS {}".format(self.__maxprice))
    
    def setleMAXPRICEGUYS(self, price):
        self.__maxprice = price

K = KOMPUTER()
K.sell()

K.__maxprice = 48000
K.sell()

K.setleMAXPRICEGUYS(48000)
K.sell
