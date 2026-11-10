

def a(x):
    if x.isdigit():
        print("این کاراکتر عدد است.")
    elif x.islower():
        print("این کاراکتر حرف کوچک است.")
    elif x.isupper():
        print("این کاراکتر حرف بزرگ است.")
    else:
        print("این کاراکتر نماد یا علامت خاص است.")

x = input('یک کاراکتر وارد کنید: ')
a(x)
