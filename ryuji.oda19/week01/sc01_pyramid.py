def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

x = (input("Enter the level: "))


if is_int(x) and int(x) != 0:
    print("ok")
else:
    print("Invalid")