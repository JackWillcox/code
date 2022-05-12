import itertools

# todo
# Use operations +,-,*,/, ^
# Use brute force
# Only use powers if nums less than 7
def tsg(lst):
    for i in itertools.permutations(lst, 4):
        for j in i:
            pass






def operations(nums, operation):
    a, b = nums[0], nums[1]

    ops = {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b}

    return ops[operation]

def permute(new_lst):
    if len(new_lst) < 2:
        return [new_lst]
    else:
        first_char = new_lst[0]
        the_rest = new_lst[1:]
        permute_the_rest = permute(the_rest)
        result = []
        for index, value in enumerate(permute_the_rest):
            pass


lst = [4, 4, 7, 8]
