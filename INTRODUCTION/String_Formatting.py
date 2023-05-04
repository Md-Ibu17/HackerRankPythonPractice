def print_formatted(number):
    width = len(bin(n)[2:])
    for i in range(1,n+1):
        l=str(i)
        l1=oct(i)[2:]
        l2=hex(i)[2:].upper()
        l3=bin(i)[2:]
        result = print(l.rjust(width),l1.rjust(width),l2.rjust(width),l3.rjust(width))
    return result

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
