def validate_age(age):
    if age<0:
        raise ValueError('Age should not be less than 0')