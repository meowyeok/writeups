# wargame : basic-mod2

- 모듈러 연산을 활용한다. 이번에는 mod41 연산 수행후 나온 값의 modular inverse를 구한 후에 1~26은 알파벳으로, 27~36은 십진수로, 37은 언더바로 바꾸면 답이 나오는 문제였다.

```python
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def mod41_inverse_conversion(number):
    result = number % 41
    inverse = mod_inverse(result, 41)
    if inverse is None:
        return '_'
    if 1 <= inverse <= 26:
        return chr(ord('a') + inverse - 1)
    elif 27 <= inverse <= 36:
        return str(inverse - 27)
    else:
        return '_'

def main():
    numbers = input("숫자들을 입력하세요(공백으로 구분): ").split()
    for number in numbers:
        try:
            number = int(number)
            print(mod41_inverse_conversion(number), end='')
        except ValueError:
            print("입력한 값 중 유효하지 않은 값이 있습니다.")
            continue

if __name__ == "__main__":
    main()
```