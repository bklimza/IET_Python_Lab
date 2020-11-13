def calculate_gcd(a, b):
    if b > 0:
        return calculate_gcd(b, a % b)
    else:
        return a


def check_numbers(number):
    float_number = float(number)
    int_number = int(number)
    if float_number != int_number:
        raise TypeError('Incorrect type')
    else:
        if int_number < 1:
            raise ValueError('Number isn\'t a positive integer')
        return int_number


def validate_entities(numbers, validation, expected_len=None):
    if expected_len is not None:
        if expected_len != len(numbers):
            raise ValueError('Incorrect quantity of numbers')
    return [validation(number) for number in numbers]


def get_valid_input(message_to_user, validation, expected_len=None, sep=' '):
    return validate_entities(input(message_to_user).split(sep), validation, expected_len)


def execute_gcd():
    while True:
        try:
            a, b = get_valid_input('Type numbers separated by space: ', check_numbers, 2, ' ')
            return calculate_gcd(a, b)
        except (ValueError, TypeError) as error:
            print(error)


print(execute_gcd())
