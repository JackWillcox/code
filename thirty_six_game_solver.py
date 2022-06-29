from itertools import chain


# Use operations +,-,*,/, ^
# Use brute force
# Only use powers if nums less than 7
def tsg(lst):
    #hello
    pass


def operations(nums, operation):
    a, b = nums[0], nums[1]

    ops = {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b}

    return ops[operation]


def all_words():
    base = 16
    digits = 4

    lst = [1 for i in range(digits)]
    overall = []
    counting = True

    while counting:
        c_lst = sorted(lst.copy())

        if c_lst not in overall:
            overall.append(c_lst)
        pointer = digits - 1
        seeking = True
        while seeking and counting:
            lst[pointer] += 1
            if lst[pointer] == base:
                lst[pointer] = 1
                pointer -= 1
                if pointer < 0:
                    counting = False
            else:
                seeking = False

    print(overall)


lst = [4, 3, 7, 8]

all_words()
