# wargame : basic-mod1

- mod연산 문제인것같다.
- 문제를 보니 주어진 숫자들을 mod37연산하여 나온값으로 0~25는 알파벳으로, 26~35는 십진수로, 36은 언더바로 바꾸어 해독하는 문제였다.
- 급한대로 chatGPT에게 코드를 받았다.

```python
def mod37_conversion(number):
    result = number % 37
    if 0 <= result <= 25:
        return chr(ord('a') + result)
    elif 26 <= result <= 35:
        return str(result - 26)
    else:
        return '_'

def main():
    numbers = input("숫자들을 입력하세요(공백으로 구분): ").split()
    for number in numbers:
        try:
            number = int(number)
            print(mod37_conversion(number), end='')
        except ValueError:
            print("입력한 값 중 유효하지 않은 값이 있습니다.")
            continue

if __name__ == "__main__":
    main()
```