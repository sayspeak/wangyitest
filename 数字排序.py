def test():
    a = int(input())
    n = int(input())
    result=[]
    for i in range(a,n+1):
        val=''
        for j in range(1,i+1):
            val+=str(j)
        result.append(val)
    num = [int(i)for i in result]
    number = [x for x in num if x % 3 == 0]
    print(len(number))
    return number
if __name__ == "__main__":
    test()