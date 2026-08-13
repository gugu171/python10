class DAILIMASSAGE:
    def __init__(self):
        self.message = ''

    def get_message(self):
        self.message = input('WHAT DO YOU WANT TO TYPE IN FOR YOUR MESSAGE D:< : ')

    def print_message(self):
        print("LEMESSAGEINUPPERCASEIS:",self.message.upper())


dailytext = DAILIMASSAGE()
dailytext.get_message()
dailytext.print_message()

class OHLOOKAHELPER:
    def __init__(self):
        print("DAILYDATAHELPERHASBEENCREATED")
    def __del__(self):
        print("IDESTROYEDTHEDAILYDATAHELPERMUAHAHAHAAHAHAHA")

def create_seeesion():
    print("MAKINGHELPER")
    session = OHLOOKAHELPER()
    print("HELPERISREDY")
    return session

print("")
print("EVERYONEBEQUIETIMCALLINGTHECREATORFUNCTIONORWHATEVER")
session_obj = create_seeesion()
print("OMLWHYISTHEPROGRAMSTILLRUNNING?")

class IMGONNAPAIRYOUYOUBETTERFINDSOMETHING:
    def find_pair(self, numbers, target):
        lookup = {}
        for index,number in enumerate(numbers):
            needed_number = target - number
            if needed_number in lookup:
                return (lookup[needed_number], index)
            lookup[number] = index
        return None

numbers = (10,20,30,40,50,60,70)
target_value = int(input("ENTERDASUMYOUWANTTOSEARCH : "))
result = IMGONNAPAIRYOUYOUBETTERFINDSOMETHING().find_pair(numbers,target_value)
if result is not None:
    print("index1 = %d, index2=%d" % result)
else:
    print("OINOMATCHINGPAIRISFOUNDNOWSHOO")

del session_obj
print("PROGRAMSENDEDBYEBYE")