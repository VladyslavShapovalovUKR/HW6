password = input()
count = 0
has_digit = False
has_lower = False
has_upper = False

for i in password:
    if i.isupper():
        has_upper = True
        break
if has_upper:
    count += 1
else:
    print('Добавьте букву верхнего регистра')

for i in password:
    if i.islower():
        has_lower = True
        break
if has_lower:
    count += 1
else:
    print('Добавьте букву нижнего регистра')

for i in password:
    if i.isdigit():
        has_digit = True
        break
if has_digit:
    count += 1
else:
    print('Добавьте цифру в Ваш пароль')

for i in password:
    if i in '!@#$%^&*()_+?><|"':
        has_special = True
        break
if has_special:
    count += 1
else:
    print('Добавьте спец символ в Ваш пароль')

if len(password) >= 8:
    count += 1
else:
    print('Длина Вашего пароля менее 8 исмволов')

print(f'Ваш пароль получил {count} балов из 5')
