def sum_number(start, end):
    if start > end:
        start = end
        return start + end
    else:
        return start + end

print(sum_number(12, 15))


def time_input(second):
    try:
        second = int(second)
    except ValueError:
        return "Error. It's not number!"


    if second < 0:
        return "Error. Your number < 0"

    days = second // (24 * 3600)
    second %= (24 * 3600)
    hours = second // 3600
    second %= 3600
    minutes = second // 60
    second %= 60

    return print(f'{days}:{hours:02d}:{minutes:02d}:{second:02d}')

time_input(1234567)

def sum_for(start: list):
    counter = 0

    for i in start:
        counter += i
    return counter

def sum_while(start: list):
    total = 0
    index = 0

    while index < len(start):
        total += start[index]
        index += 1

    return total

print(sum_for([1, 2, 3, 4, 5, 6]))
print(sum_while([1, 2, 3, 4, 5, 6]))
