def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

ans = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        
        if is_palindrome(product) and product > ans:
            ans = product
print(ans)