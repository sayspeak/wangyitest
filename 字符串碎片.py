s = input()
length = len(s)
results = []
count = 1
for i in range(length - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        results.append(count)
        count = 1
results.append(count)

print("%.2f" % (sum(results) / len(results)))