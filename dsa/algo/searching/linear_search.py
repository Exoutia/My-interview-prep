def linear_search(arr: list, tar: int):
    for i in arr:
        if i == tar:
            return True
    return False

if __name__ == "__main__":
    print(linear_search([1,3,2,98,54,3,45], 98))
