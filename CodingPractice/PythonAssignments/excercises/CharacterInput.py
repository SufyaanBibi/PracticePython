def centenary_calculator(user_age, current_year):
    if user_age == 0:
        date_of_birth = current_year - user_age
        x = date_of_birth + 100
    elif user_age > 0:
        date_of_birth = current_year - user_age - 1
        x = date_of_birth + 100
    return x
