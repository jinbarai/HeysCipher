cipher = open("/Users/jinbarai/Desktop/HeysCipher/a2q1ciphertext.txt", "r")
plain = open("/Users/jinbarai/Desktop/HeysCipher/a2q1plaintext.txt", "r")
# reading as a list of list
ciphertext = [list(line) for line in cipher.read().splitlines()[1:]]
plaintext = [list(line) for line in plain.read().splitlines()[1:]]

# Mapping the inverse values of S-Boxes for Heys Cipher
S = {14: 0, 4: 1, 13: 2, 1: 3, 2: 4, 15: 5, 11: 6, 8: 7, 3: 8, 10: 9, 6: 10, 12: 11, 5: 12, 9: 13, 0: 14, 7: 15}
K_8 = '01010110'
K = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001',
     10: '1010', 11: '1011', 12: '1100', 13: '1101', 14: '1110', 15: '1111'}


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


def main():
    bias = {}
    for i in range(16):
        for j in range(16):
            new_key = K[i] + K_8[:4] + K[j] + K_8[4:]
            key = [int(line) for line in new_key]
            val = return_bias(key)
            # print(val)
            bias[val] = key
    else:
        # print(len(bias))
        result = max(bias.keys())
        print(result)
        print(bias[result])


def return_bias(key):
    # Each element is an integer
    total = 0
    # 20000 times for each ciphertext and plaintext
    for i in range(len(ciphertext)):
        # dividing the cipher text into 2 lists of integers and plaintext into 1 list of integer
        c = [int(x) for x in ciphertext[i]]
        p = [int(x) for x in plaintext[i]]

        # XOR K with V
        v = get_xor(c, key)

        # Breaking up into 4 chunks
        v1 = v[:4]
        v2 = v[4:8]
        v3 = v[8:12]
        v4 = v[12:]

        # bin -> dec
        r1 = int(v1, 2)
        r2 = int(v2, 2)
        r3 = int(v3, 2)
        r4 = int(v4, 2)

        # Back to binary after using the look up table
        # S inverse box -> binary
        result1 = safe(format(S[r1], "b"))
        result2 = safe(format(S[r2], "b"))
        result3 = safe(format(S[r3], "b"))
        result4 = safe(format(S[r4], "b"))

        result = result1 + result2 + result3 + result4

        # Converting to int
        u = [int(x) for x in result]

        # Extracting only necessary values and storing in a list
        res = [u[1], u[5], u[9], u[13], p[0], p[3], p[8], p[11]]

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


main()

# Closing the file
cipher.close()
plain.close()
