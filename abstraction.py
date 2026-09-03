from abc import ABC, abstractmethod

class ABSCLASS(ABC):
    def print (self, x):
        print("LE PASED VALU :",x)
    @abstractmethod
    def task(self):
        print("oooh we ar insid absclass taisk")
class test_class(ABSCLASS):
    def task(self):
        print("We are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)