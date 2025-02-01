def format(number):
    new = f'R${number:.2f}'.replace(".", ",")
    return new

def half(number, format_option = True):
    half = number / 2
    if format_option == True:
        return format(half)
    else:
        return half

def times2(number, format_option = True):
    times2 = number * 2
    if format_option == True:
        return format(times2)
    else:
        return times2

def raise_tenpercent(number, format_option = True):
    raise_tenpercent = number * 1.1
    if format_option == True:
        return format(raise_tenpercent)
    else:
        return raise_tenpercent
