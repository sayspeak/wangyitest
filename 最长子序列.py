def isl(t1):
    length = len(t1)
    temp = 0
    for i in range(length):
        if t1[i] == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            return 0
    return 1


def main(t):
    length = len(t)
    count = set()
    for i in range(length):
        temp1 = t[:i] + t[i + 1:]
        for j in range(length):
            if i == j:
                continue
            temp2 = temp1[:j] + t[i] + temp1[j:]
            if isl(temp2):
                if temp2 != t:
                    count.add(temp2)
    print(len(count))


if __name__ == "__main__":
    string = input()
    main(string)