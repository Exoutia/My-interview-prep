from timeit import timeit
if __name__ == "__main__":
    L =[i for i in range(100000)]
    print(timeit("L[1:]",  setup="from __main__ import L", number=10000))
    L =[i for i in range(100000)]
    print(timeit("L.pop(-1)", setup="from __main__ import L", number=10000))