# PART 1: Create the library's book names and available copy counts
books = ["mapilta", "bo'oh of wa'er", "andiwonderifyouknowwhatitmeanss", "grupalo", "bobby"]
copy_counts = [4, 0, 6, 3, 2]


library = {book: count for book, count in zip(books, copy_counts)}
print("Full Library Stock:", library)

available_books = [book for book in books if library[book] > 0]
print("Books Available:", available_books)

chosen_book = input("WOT BOK YOU WANT BORO ")

if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, "DIS ONE NOT THERE I STOP CHECK NOW.")
    exit()

late_fees = [5, 8, 4, 6, 7]
extra_fee = int(input("ENTIR EXTR LIBRY FEE FOR AL BOKS "))


updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("UPDAT LAT FEE: ", updated_fees)


book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]
print("LAT FEE POUR", chosen_book, "AFTIR UPDAT", chosen_fee)

library[chosen_book] = library[chosen_book] - 1
print(chosen_book, "GOOD BOY YOU BOROWS", library[chosen_book])


print("")
print("===== LIBRY BOK AVAILITY CHEKER =====")
print("BOK BOROW:", chosen_book)
print("LAT FEE:", chosen_fee)
print("UPDAT LIBRY FEE:", library)
print("=====================================")