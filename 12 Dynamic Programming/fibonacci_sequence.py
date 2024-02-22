def fib_seq(n, dic = {}):
    if n == 0 or n == 1:
        return n
    if not n in dic.keys():
        dic[n] = fib_seq(n - 1 , dic) + fib_seq(n - 2 , dic)
    return dic[n]


print(fib_seq(20))
