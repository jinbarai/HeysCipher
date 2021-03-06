cipher = open("a2q1ciphertext.txt", "r")
plain = open("a2q1plaintext.txt", "r")
# reading as a list of list
ciphertext = [list(line) for line in cipher.read().splitlines()[1:]]
plaintext = [list(line) for line in plain.read().splitlines()[1:]]

# For Question 1a
K = [0, 1, 1, 1, 0, 1, 1, 0]

# Mapping the inverse values of S-Boxes for Heys Cipher
S = {14: 0, 4: 1, 13: 2, 1: 3, 2: 4, 15: 5, 11: 6, 8: 7, 3: 8, 10: 9, 6: 10, 12: 11, 5: 12, 9: 13, 0: 14, 7: 15}


# Return the XOR value between C & K as str
def get_xor(c, k):
    result = []
    for i in range(len(c)):
        result.append(c[i] ^ k[i])
    st = ""
    for i in result:
        st = st + str(i)
    else:
        return st


# Ensuring the bin num has 4 bits
def safe(num):
    st = str(num)
    if len(st) == 4:
        return num
    else:
        places = 4 - len(st)
        for i in range(places):
            st = '0' + st
    return st


# def generate_key():


def main():
    # Each element is an integer
    total = 0
    # 20000 times for each ciphertext and plaintext
    for i in range(len(ciphertext)):
        # dividing the cipher text into 2 lists of integers and plaintext into 1 list of integer
        c = [int(x) for x in ciphertext[i][4:8]]
        c2 = [int(x) for x in ciphertext[i][12:]]
        p = [int(x) for x in plaintext[i]]

        # Extracting K
        k = K[0:4]
        k2 = K[4:]

        # XOR K with V
        v = get_xor(c, k)
        v2 = get_xor(c2, k2)

        # bin -> dec
        r1 = int(v, 2)
        r2 = int(v2, 2)

        # Back to binary after using the look up table
        # S inverse box -> binary
        result1 = safe(format(S[r1], "b"))
        result2 = safe(format(S[r2], "b"))
        # Converting to int
        l = [int(x) for x in result1]
        l2 = [int(x) for x in result2]
        # Extracting only necessary values and storing in a list
        res = [l[1], l[3], l2[1], l2[3], p[4], p[6], p[7]]
        # XOR all the values in the above list to check if it satisfies the condition
        if check_xor(res):
            total += 1
    # Bias: (Total number of true values / 20000) - 0.5
    return abs((total / len(ciphertext)) - 0.5)


# checking if xor = 0
def check_xor(values):
    i = 1
    result = values[0]
    while i < len(values):
        val = values[i]
        result = result ^ val
        i += 1
    if result == 0:
        return True
    return False


print(main())

# Closing the file
cipher.close()
plain.close()
