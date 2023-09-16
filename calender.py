def print_calendar(Total, starting):
    print("Sun Mon Tue Wed Thu Fri Sat")
    print(" " * starting * 4, end="")
    day = 1
    while day <= Total:
        print(f"{day:2}", end="  ")
        if (day + starting) % 7 == 0:
            print()
        day += 1

    print()
Total = int(input("Enter the number of days in the month: "))
starting = int(input(
"""
Please Select a day from which mounth is start
Monday      - 1      
Tueday      - 2
Wednesday   - 3
Thursday    - 4
Friday      - 5
Saturday    - 6
Sunday      - 0 
"""))
print_calendar(Total, starting)
