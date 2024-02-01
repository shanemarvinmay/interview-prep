def rev_pos_int(num):
    rev = 0
    while num > 0:
        last_digit = num % 10
        rev *= 10
        rev += last_digit
        num //= 10
    return rev