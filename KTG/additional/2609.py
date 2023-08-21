a, b = map(int, input().split())


def pf(num):
    result = []
    i = 2
    j = 0
    while num != 1:
        if num % i == 0:
            num = num // i
            result.append((i, j))
            j += 1
        else:
            i += 1
            j = 0
    return result


alst = pf(a)
blst = pf(b)

lcm = 1
for i in alst:
    if i in blst:
        lcm *= i[0]
mul = 1
for i in alst:
    mul *= i[0]
for i in blst:
    mul *= i[0]
gcm = mul // lcm

print(lcm)
print(gcm)
