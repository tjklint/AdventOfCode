def main():
    initial_secret_numbers = [int(line.strip()) for line in open("../input.txt")]
    secret_numbers = [generate_secret_numbers(initial, 2000) for initial in initial_secret_numbers]
    total = sum(secret_numbers)
    print("Sum of 2000th secret numbers:", total)

def mix_and_prune(secret_number, value):
    mixed = secret_number ^ value
    return mixed % 16777216

def generate_secret_numbers(initial_secret_number, num_secret_numbers):
    secret_number = initial_secret_number
    for _ in range(num_secret_numbers):
        secret_number = mix_and_prune(secret_number * 64, secret_number)
        secret_number = mix_and_prune(secret_number // 32, secret_number)
        secret_number = mix_and_prune(secret_number * 2048, secret_number)
    return secret_number


if __name__ == "__main__":
    main()