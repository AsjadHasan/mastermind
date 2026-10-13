def calculate_fine():
    number_of_books = int(input("Number of books: "))
    total_fine = 0
    for i in range(number_of_books):
        title = input("Book title: ")
        days_overdue = int(input("Days overdue: "))
        if days_overdue <= 7:
            fine = days_overdue * 5
        else:
            fine = (7 * 5) + ((days_overdue - 7) * 10)
        print(f"{title}: {fine} BDT")
        total_fine += fine
    print(f"Total fine: {total_fine} BDT")
calculate_fine()