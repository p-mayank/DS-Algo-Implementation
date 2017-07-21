import math

#Recursion
# def CUT(price_arr, length):
#     if(length==0):
#         return 0
#
#     op_cost = -(math.inf)
#     for cut in range(1,length+1):
#         op_cost = max(op_cost, price_arr[cut-1]+CUT(price_arr, length-cut))
#
#     return op_cost
#
#


def CUT(price_length, length):
    r=[None]*(length+1)
    s=[None]*(length+1)

    r[0]=0
    for i in range(1, length+1):
        q=-(math.inf)
        for j in range(1, i+1):
            if(q < price_length[j-1]+r[i-j]):
                q = price_length[j-1]+r[i-j]
                s[i]=j
        r[i]=q

    print(s)
    print(r)
length = input()
length=int(length)
print(type(length))
price_arr = input().split()
price_arr = [int(x) for x in price_arr]
CUT(price_arr, length)
