fibonacci = [1, 2]
ans = 2

while 1:
    new = fibonacci[0]+fibonacci[1]

    if new > 4000000:
        break

    fibonacci.append(new)
    if new % 2 == 0:
        ans += new
    fibonacci.pop(0)

print(ans)