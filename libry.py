

books = ['matilda', 'gruflo', 'pottie', 'indajungledimightijungel', 'bigmac']
copy_counts = [4,0,6,3,2]
library = {book: count for book, count in zip(books,copy_counts)}
print("Full library stock:",library)
availbooks = [book for book in books if library[book] > 0]
print("Books to your avail:",availbooks)
chosenbokbokbakaak = input("WOT BOK YU WAN 2 BOROW : ")
if chosenbokbokbakaak not in library or library[chosenbokbokbakaak] == 0:
    print(chosenbokbokbakaak,'IS NUT AVAIL PLS COM BAK LATIR STOPING LE SCHEKER')
    exit()
latefee = [5,8,4,6,7]
extrafee = int(input("Entir da extri librari fe to ad to ebry bok: "))
updatedfee = list(map(lambda fee: fee + extrafee, latefee))
print("Updat lat fii :",updatedfee)
book_index = books.index(chosenbokbokbakaak)
chosen_fee = updatedfee[book_index]
print("Lat fii fur ",chosenbokbokbakaak,'after updat:',chosen_fee)
library[chosenbokbokbakaak] = library[chosenbokbokbakaak] - 1
print(chosenbokbokbakaak, 'now browed remanin copye:',library[chosenbokbokbakaak])
print('')
print('LIBRARI BOOK AVAILBILIT CHICKIR')
print("BOK BOROWd:",chosenbokbokbakaak)
print("Lat fii:",chosen_fee)
print("Update librari stuck:",library)