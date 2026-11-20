marks = int(input("Enter your test marks: "))

if marks < 0 or marks > 40:
    print("invalid marks")
elif marks >= 32:
    print("distinction")
elif marks >= 20:
    print("pass")
else:
    print("fail")