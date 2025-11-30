n = 125 + 25**3 + 5**9

digits = []

while n > 0 :
    remainder = n % 5
    digits.append(remainder)
    n //= 5
sum_of_digits = sum(digits)

# Вывод результата
print(f"Пятеричная запись числа: ", ''.join(str(d) for d in reversed(digits)))
print(f"Cумма цифр: {sum_of_digits}")
