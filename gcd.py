
#최대공약수 구하는 알고리즘

def gcb_sub(num1, num2) :
    while num1 != 0 and num2 != 0 :
        if num1 > num2 : num1 = num1-num2
        else : num2 = num2-num1
    print(num1+num2)


def gcb_mod(num1, num2) :
    while num1 != 0 and num2 != 0 :
        if num1 > num2 : num1 = num1%num2
        else : num2 = num2%num1
    print(num1+num2)


# 유클리드 호제법 (재귀)
def gcb_rec(num1, num2) :
    if num1%num2 == 0 :
        return num2
    return(gcb_rec(num2, num1%num2))
        


num1 = int(input());
num2 = int(input());

gcb_sub(num1, num2)
gcb_mod(num1, num2)
print(gcb_rec(num1, num2))
