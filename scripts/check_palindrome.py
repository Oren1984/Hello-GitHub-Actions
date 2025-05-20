def is_palindrome(num):
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    number = 12321  # אפשר לשנות למספר אחר או לקבל קלט
    if is_palindrome(number):
        print(f"{number} is a palindrome")
    else:
        print(f"{number} is not a palindrome")
