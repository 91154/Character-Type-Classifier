
def func(ch):
    if 48 <= ord(ch) <= 57:
        print("کارکتر شما عدد است ")
    elif 67 <= ord(ch) <= 90:
        print("کارکتر شما حرف بزرگ است ")
    elif 97 <= ord(ch) <= 122:
        print("کارکتر شما حرف کوچک است  ")
    else:
        print("کارکتر شما نماد علمی است ")

c = input("یک کارکتر وارد کنید:   ")
func(c)
