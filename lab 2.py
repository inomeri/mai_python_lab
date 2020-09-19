#lab 2
def sign_num(x):
    x = int(x)
    if x > 0:
        return '1'
    elif x < 0:
        return '-1'
    elif x == 0:
        return '0'


num = input()
print(sign_num(num))
