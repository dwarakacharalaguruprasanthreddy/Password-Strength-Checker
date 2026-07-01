password = input("Enter your password: ")

upper = False
lower = False
digit = False
special = False

special_chars = "@#$%&*!"

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch in special_chars:
        special = True

if len(password) < 8:
    print(" ❌ Weak Password")
    print("Reason: Password must contain at least 8 characters.")
elif upper and lower and digit and special:
    print("✅ Strong Password")
elif (upper and lower and digit) or (upper and lower and special) or (lower and digit and special):
    print("⚠️ Medium Password")
else:
    print("❌ Weak Password")
