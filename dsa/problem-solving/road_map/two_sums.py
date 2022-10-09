def find_the_pair(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if num in dic:
            return dic[num], i
        dic[target - num] = i


if __name__ == '__main__':
    print(find_the_pair([10, 15, 3, 7], 17))