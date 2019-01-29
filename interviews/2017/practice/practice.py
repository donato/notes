
"""
# Add based on tuning
EASY_POWERS_OF_3 = [1,8,27]
def is_power_3(n):
    if n <= EASY_POWERS_OF_3[-1]:
        return n in EASY_POWERS_OF_3:

    # Else do binary search for until you converge (ie delta is less than 1)
    # At this point, compare the 3 numbers to find a match


"""


"""
def encode(input):
    if not len(input):
        return input

    input = list(input)
    write_ptr = len(input) - 1
    read_ptr = find_end(input)

    print(read_ptr)
    while(write_ptr > read_ptr and read_ptr > 0 and write_ptr > 2):
        print("Read %s" % read_ptr)
        print("Write %s" % write_ptr)
        if input[read_ptr] == " ":
            input[write_ptr - 2]  = "%"
            input[write_ptr - 1]  = "2"
            input[write_ptr - 0]  = "0"
            write_ptr = write_ptr - 3
            read_ptr = read_ptr - 1
        else:
            input[write_ptr] = input[read_ptr]
            write_ptr = write_ptr - 1
            read_ptr = read_ptr - 1

    return input

def find_end(input):
    max_char = None

    for index, val in enumerate(input):
        if val != " ":
            max_char = index

    return max_char

str = "HI CAT  "
print(encode(str))
"""





