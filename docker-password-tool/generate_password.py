import random
import string
import datetime
import os

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    length = int(os.environ.get('PASSWORD_LENGTH', 12))
    password = generate_password(length)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"[{timestamp}] Generated password (length {length}): {password}\n"

    log_path = '/data/password_log.txt'
    with open(log_path, 'a') as f:
        f.write(log_entry)

    print(f"Password generated: {password}")
    print(f"Logged to {log_path}")

if __name__ == '__main__':
    main()
