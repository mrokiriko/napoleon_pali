
class Tenet(object):

    @staticmethod
    def is_palindrome(number):

        digits = 0
        p = number

        arr = []

        while p > 0:
            digits = digits + 1
            arr.append(p % 10)
            p = p // 10

        end = digits - 1
        start = 0
        while start < end:
            if arr[start] != arr[end]:
                return False
            start = start + 1
            end = end - 1

        return True


print("write in your favourite number for palindrome checking:")
line = input()

try:
    num = int(line)

    print(num, end='')

    if Tenet.is_palindrome(num):
        print(" is palindrome!")
    else:
        print(" is not a palindrome")

except ValueError:
    print('this is not a real number! think about what you just did')

