import random

def generate_pin(length=4):
    """Generates a random PIN code of the specified length."""
    return "".join(str(random.randint(0, 9)) for _ in range(length))

# Generate a 4-digit PIN
pin = generate_pin()
print(pin)
