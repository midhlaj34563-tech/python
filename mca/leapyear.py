

final_year = int(input("Enter the final year: "))

print(f"\nLeap years from 2025 to {final_year}:")

# Loop through each year in the range
for year in range(2025, final_year + 1):
    # Check leap year condition
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)

print("\nProgram finished!")


# Program to display future leap years from the current year to a user-entered final year


