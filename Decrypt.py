#code_by_mohammad_parsa_ansari981823010
from RSA import expo_mod

if __name__ == '__main__':
    d = int(input("Enter private key: "))
    n = int(input("Enter n: "))

    text = open("text.txt", "r")
    result = open("result.txt", "w")
    nums = []
    result_str = ""
    for line in text:
        nums = line.split('/')
        for c in nums:
            try: num = int(c)
            except: continue
            dec = expo_mod(num, d, n)
            result_str += chr(dec)
    
    result.write(result_str)
    result.close()
