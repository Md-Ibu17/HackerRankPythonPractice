import textwrap
def merge_the_tools(string, k):
    sub_string = textwrap.fill(string, k)
    res = sub_string.split()
    for i in res:
        a = ''.join(list(set(i)))
        print(a)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
