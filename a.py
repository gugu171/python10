def find_squares_and_filter(start_num, end_num):
    for num in range(start_num, end_num + 1):
        square_value = num ** 2
        
        if square_value % 2 == 0:
            print(f"{square_value} is an even square.")
        else:
            print(f"{square_value} is an odd square.")

start_num_from_user = int(input("Enter the starting number: "))
end_num_from_user = int(input("Enter the ending number: "))

find_squares_and_filter(start_num_from_user, end_num_from_user)