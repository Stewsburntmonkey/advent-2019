""" Password Utilities """


def is_valid(password: int) -> bool:
    return all([
        len(str(password)) == 6,
        has_repeated_digits(password),
        monotonicly_increasing(password),
    ])


def has_repeated_digits(password: int) -> bool:
    password = str(password)
    for i in range(0,len(password)-1):
        if password[i] == password[i+1]:
            return True
    
    return False


def monotonicly_increasing(password: int) -> bool:
    password = str(password)
    for i in range(1,len(password)):
        if password[i] < password[i-1]:
            return False
    
    return True


def has_digit_pair(password: int) -> bool:
    password = str(password)
    previous = password[0]
    streak = 1
    for i in range(1,len(password)):
        if password[i] == previous:
            streak += 1
        else:
            if streak == 2:
                return True
            streak = 1
        previous = password[i]
    
    return streak == 2