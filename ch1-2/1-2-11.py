n = int(input())

is_div_4 = n % 4 == 0
is_div_100 = n % 100 == 0
is_div_400 = n % 400 == 0

is_bad_by_100_exception = (
    is_div_100
    and not is_div_400
)
is_leap_year = (
    is_div_4
    and not is_bad_by_100_exception
)
print(is_leap_year)