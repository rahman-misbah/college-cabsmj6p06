# Write a program to print number of days in a month using if-elif-else statement.
def days_in_month(month: int, year: int) -> int | str:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "Invalid month"

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

result = days_in_month(month, year)
print(f"Number of days: {result}")