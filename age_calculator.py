
from datetime import datetime, timedelta, date

def get_date():
    birth_date_str = input('Enter birthday (MM/DD/YY): ')
    birth_date = datetime.strptime(birth_date_str, '%m/%d/%y')
    return birth_date


def calculate_age(birthday):
    today = date.today()
    birthday = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return birthday

def get_days_until_birthday(birth_date: date, today: date) -> int:
    this_year = (date(today.year, birth_date.month, birth_date.day) - today).days
    if this_year >= 0:
        return this_year
    next_year = (date(today.year+1, birth_date.month, birth_date.day) - today).days
    return next_year


def main():
    print('Birthday Calculator')
    while True:
        today = date.today()
        name = input('Enter Name: ')
        birthday = get_date()
        age = calculate_age(birthday)
        days = get_days_until_birthday(birthday,today)
        print('Birthday:', birthday.strftime('%A, %B %d, %Y'))
        print('Today:\t ',today.strftime('%A, %B %d, %Y'))
        print(name,'is', age, 'years old.')
        if (today.month, today.day) == (birthday.month, birthday.day):
            print(name + '\'s birthday is today!')
        elif (today.month, today.day) == (birthday.month, birthday.day + 1):
            print(name + '\'s birthday was yesterday!')
        elif (today.month, today.day) == (birthday.month, birthday.day - 1):
            print(name + '\'s birthday is tomorrow!')
        else:
            print(name + '\'s birthday is in', days,'days.')
        print()
        result = input('Continue? (y/n): ')
        print()
        if result.lower() != 'y':
            print('Bye!')
            break



if __name__=='__main__':
    main()