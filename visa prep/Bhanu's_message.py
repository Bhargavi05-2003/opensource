import re
def validate_number(number):
    if len(number) == 10 and number.isdigit():
        return "Correct"
    match = re.match(r'^\+(\d{1,2}) (\d{10})$', number)
    
    if match:
        country_code = match.group(1)
        digits = match.group(2)
        if len(country_code) == 1:
            return "Incorrect"
        if sum(int(digit) for digit in digits) > 0:
            return "Correct"
    return "Incorrect"
number = input()
print(validate_number(number))
