
def is_letter(user_letter):
    ascii_value = ord(user_letter)
    if ascii_value >= 65 and ascii_value <=90:
        return True
    else:
        return False


