import sys

def main():
    if len(sys.argv)!=3 or len(sys.argv[1])!=len(sys.argv[2]):
        print(False)
        return
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(encoding(str1)==encoding(str2))

def encoding(str1):
    enc = {}
    encode = []
    for x,y in enumerate(str1):
        if y not in enc:
            enc[y]= x
        encode.append(enc[y])
    return "".join(str(encode))

if __name__ == "__main__":
    main()
