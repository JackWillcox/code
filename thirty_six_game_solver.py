import itertools


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
        return new_lst
    else:
        lst=[]
        for index in range(len(new_lst)):
            temp = new_lst[index]
            remaining_lst = new_lst[:index] + new_lst[index+1:]
            for j in permute(remaining_lst):
                lst.append([temp] + j)
        return lst



lst = [4, 3, 7, 8]
print(permute(lst))
