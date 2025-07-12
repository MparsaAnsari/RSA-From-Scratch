#code_by_mohammad_parsa_ansari981823010
import datetime
from time import sleep
from math import log

def random_odd_number():
    
    # stop kardan baraye gozare vaght!
    sleep(0.002)

    # gereftane zamane feeli be micro sanie
    time = datetime.datetime.now().microsecond
    a = ((time // 100) % 9) + 1
    b = ((time // 1000) % 100) + 1
    n = time % 20

    # tolide adade tasodafi
    for i in range(n):
        time = a * time + b
    
    time = int(time)
    # ezafe kardane raghame fard be akhare adad
    s = str(time)
    s = s + str(2 * (a // 2) + 1)
    time = int(s)
    
    return time

# mohasebeye (a ^ n) mod m

def expo_mod(a, n, m):

    digits = []
    while n > 1:
        digits.append(n % 2)
        n = n // 2
    digits.append(n)

    x = 1
    power = a % m
    for i in range(len(digits)):
        if digits[i] == 1: x = (x * power) % m
        power = (power * power) % m

    return x

# Miller Robin test

def is_prime(n):
    
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = d // 2
        r += 1
        
    for a in range(2, min(n - 2, int(2 * (log(n) ** 2))) + 1):
        x = expo_mod(a, d, n)
        if x == 1 or x == n - 1: continue

        continue_a = False
        for i in range(r - 1):
            x = expo_mod(x, 2, n)
            if x == n - 1:
                continue_a = True
                break
        if continue_a == True: continue

        return False

    return True

# tvabe komaki baraye tabe multiply

def equal_length(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if l1 > l2:
        for i in range(l1 - l2):
            str2 = '0' + str2
        return (str1, str2)
    elif l2 > l1:
        for i in range(l2 - l1):
            str1 = '0' + str1
    
    return (str1, str2)

def add(str1, str2):
    
    res = ""
    carry = 0

    (str1, str2) = equal_length(str1, str2)

    i = len(str1) - 1
    while i >= 0:
        num = int(str1[i]) + int(str2[i]) + carry
        digit = num % 2
        carry = (num - digit) // 2
        res = str(digit) + res

        i -= 1
    
    if carry == 1: res = '1' + res

    return res

def multiply_single_bit(num1, num2):
    return int(num1) * int(num2)

# algorithme karatsoba baraye zarbe do adad

def multiply_bainery(X, Y):
    
    (X, Y) = equal_length(X, Y)
    n = len(X)

    if n == 0: return 0
    if n == 1: return multiply_single_bit(X, Y)

    fh = n // 2
    sh = n - fh

    Xl = X[0 : fh]
    Xr = X[fh : ]

    Yl = Y[0 : fh]
    Yr = Y[fh : ]

    P1 = multiply_bainery(Xl, Yl); 
    P2 = multiply_bainery(Xr, Yr);
    P3 = multiply_bainery(add(Xl, Xr), add(Yl, Yr));

    return P1 * (1 << (2 * sh)) + (P3 - P1 - P2) * (1 << sh) + P2

def multiply(X, Y):

    is_neg = False
    if X < 0 and Y > 0:
        is_neg = True
        X = -1 * X
    if Y < 0 and X > 0:
        is_neg = True
        Y = -1 * Y
    if X < 0 and Y < 0:
        X = -1 * X
        Y = -1 * Y

    X_base2 = ""
    while X > 1:
        X_base2 = str(X % 2) + X_base2
        X = X // 2
    X_base2 = str(X) + X_base2
    
    Y_base2 = ""
    while Y > 1:
        Y_base2 = str(Y % 2) + Y_base2
        Y = Y // 2
    Y_base2 = str(Y) + Y_base2

    res = multiply_bainery(X_base2, Y_base2)
    if is_neg == True: return -1 * res
    return res

def get_private_key(e, phiN):
    lalastR = phiN
    lastR = e

    lalastD = 0
    lastD = 1

    r = -1

    # Extended Euclidean

    while expo_mod(lalastR, 1, lastR) != 0:
        q = lalastR // lastR
        
        d = lalastD - multiply(lastD, q)
        lalastD = lastD
        lastD = d

        r = expo_mod(lalastR, 1, lastR)
        lalastR = lastR
        lastR = r

    if(d < 0):
        d = d + phiN
    
    return d


if __name__ == '__main__':
    # random_odd_number()
    # expo_mod(a, n, m)
    # is_prime(n)
    # multiply(x, y)
    # get_private_key(e, phiN)
    
    p = 4
    while is_prime(p) == False:
        p = random_odd_number()
    
    q = 4
    while is_prime(q) == False:
        q = random_odd_number()
    
    n = multiply(p, q)
    phiN = multiply(p - 1, q - 1)
    e = 65537
    d = get_private_key(e, phiN)

    keys = open("keys.txt", "w")
    lines = []
    lines.append("p: " + str(p) + "\n")
    lines.append("q: " + str(q) + "\n")
    lines.append("n: " + str(n) + "\n")
    lines.append("phiN: " + str(phiN) + "\n")
    lines.append("public key: " + str(e) + "\n")
    lines.append("private key: " + str(d) + "\n")
    keys.writelines(lines)
    keys.close()

    text = open("text.txt", "r")
    result = open("result.txt", "w")
    lines = []
    for line in text:
        curr_line = ""
        for c in line:
            num_char = ord(c)
            enc = expo_mod(num_char, e, n)
            curr_line += (str(enc) + "/")
        lines.append(curr_line)
    
    result.writelines(lines)
    result.close()
