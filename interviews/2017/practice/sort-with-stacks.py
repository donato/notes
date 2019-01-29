def isEmpty(stack):
    return len(stack) == 0

def even_odd(src, dest, op):
    change_occurred = False
    hold = src.pop()
    while not isEmpty(src):
        temp = src.pop()

        if op(hold, temp): # EVEN hold > temp, ODD hold < temp
            change_occurred = True
            dest.append(temp)
        else:
            dest.append(hold)
            hold = temp

    dest.append(hold)

    return change_occurred

def odd(main, buffer):
    print("Odd phase")
    print(main)
    print(buffer)
    return even_odd(main, buffer, lambda x, y: x < y)

def even(main, buffer):
    print("Even phase")
    print(main)
    print(buffer)
    return even_odd(buffer, main, lambda x, y: x > y)

def algo(s1, s2):
    if not s1:
        return

    while True:
        odd(s1, s2)
        if not even(s1, s2):
            return



algo([1,999,2,3,4,0,3], [])
algo([], [])
algo([1], [])


