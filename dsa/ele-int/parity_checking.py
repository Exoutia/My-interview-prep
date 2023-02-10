# Brute force
# Time complexity: O(n) n is the word length
def parity1(x):
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res

# Time complexity: O(k) number of set bit inw word
def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # This will set the lowest set bit (1) to reset (0) in binary word.
    return result

def parity2(x):
    MASK_SIZE = 16
    BIT_MASK = 0xffff
    return (pre)
if __name__ == "__main__":
    print(parity(0b10010001))
