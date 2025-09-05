def validate_name(name):
    """
    Перевіряє ім'я користувача: тільки літери, не менше 3 символів.
    """
    return name.isalpha() and len(name) >= 3

def validate_email(email):
    """
    Перевіряє email: повинен містити символ "@".
    """
    return "@" in email

def validate_phone(phone):
    """
    Перевіряє номер телефону: тільки цифри, рівно 12 цифр.
    """
    return phone.isdigit() and len(phone) == 12

def validate_subject(subject):
    """
    Перевіряє тему повідомлення: не більше 15 символів.
    """
    return len(subject) <= 15

def validate_message_text(text):
    """
    Перевіряє текст повідомлення: не більше 500 символів.
    """
    return len(text) <= 500

# Збір даних від користувача
name = input("Enter your name: ")
email = input("Enter an email: ")
phone = input("Enter your phone number (12 digits): ")
subject = input("Enter a message subject: ")
message_text = input("Enter your message: ")

# Валідація і виведення результатів
print("\n--- Validation Results ---")

if validate_name(name):
    print(f"Name '{name}' is valid. ✅")
else:
    print(f"Name '{name}' is invalid. ❌ (Must contain only letters and be at least 3 characters long)")

if validate_email(email):
    print(f"Email '{email}' is valid. ✅")
else:
    print(f"Email '{email}' is invalid. ❌ (Must contain '@' symbol)")

if validate_phone(phone):
    print(f"Phone number '{phone}' is valid. ✅")
else:
    print(f"Phone number '{phone}' is invalid. ❌ (Must contain only 12 digits)")

if validate_subject(subject):
    print(f"Subject '{subject}' is valid. ✅")
else:
    print(f"Subject '{subject}' is invalid. ❌ (Must be no more than 15 characters)")

if validate_message_text(message_text):
    print(f"Message is valid. ✅")
else:
    print(f"Message is invalid. ❌ (Must be no more than 500 characters)")