# Question 1:

def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")

# hello_name('bjmiller96')

# Question 2: 

def first_odds():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)

# first_odds()


# Question 3:

def max_num_in_list(a_list):
    for num in a_list:
        return max(a_list)
    
# numbers = [1000, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# max_number = max_num_in_list(numbers)
# print(max_number)

# Question 4:

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 != 0 or a_year % 400 == 0:
            return f"{a_year} is a leap year."
    else:
        return f"{a_year} is NOT a leap year."    
        
# leap_year = is_leap_year(1996)
# print(leap_year)

# Question 5: 

