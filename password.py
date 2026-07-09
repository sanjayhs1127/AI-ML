# Generate all possible 4-digit PINs

even_digits = [0, 2, 4, 6, 8]
passwords = []

for d1 in even_digits:
    for d2 in even_digits:
        for d3 in even_digits:
            for d4 in even_digits:
                if d1 + d2 + d3 + d4 == 16:
                    pin = f"{d1}{d2}{d3}{d4}"
                    passwords.append(pin)

print("All Possible Passwords:\n")

for pin in passwords:
    print(pin)

print("\nTotal Number of Possible Passwords:", len(passwords))