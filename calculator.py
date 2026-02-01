def add(numbers):
    return sum(numbers)


def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result


def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            return "Error: Division by zero ❌"
        result /= n
    return result


def get_numbers():
    while True:
        user_input = input("Enter numbers separated by spaces: ")
        parts = user_input.split()

        try:
            numbers = [float(n) for n in parts]
            if len(numbers) < 2:
                print("Please enter at least two numbers.")
                continue
            return numbers
        except ValueError:
            print("❌ Invalid input. Please enter only numbers.")


while True:
    print("\n--- MULTI-NUMBER CALCULATOR ---")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")
    print("6 - Show history")

    choice = input("Choose an option (1-6): ")

    if choice == "5":
          confirm = input("Are you sure you want to exit? (y/n): ").lower()

          if confirm == "y":
            print("Goodbye 👋")
            break
          else:
            print("Exit canceled.")
            continue

    if choice == "6":
        print("\n--- CALCULATION HISTORY ---")
        try:
            with open("calculations.txt", "r") as file:
                history = file.read()
                if history.strip() == "":
                    print("No history yet.")
                else:
                    print(history)
        except FileNotFoundError:
            print("No history file found yet.")
        continue

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid option, try again.")
        continue

    numbers = get_numbers()

    if choice == "1":
        result = add(numbers)
        operation = "ADD"
    elif choice == "2":
        result = subtract(numbers)
        operation = "SUBTRACT"
    elif choice == "3":
        result = multiply(numbers)
        operation = "MULTIPLY"
    elif choice == "4":
        result = divide(numbers)
        operation = "DIVIDE"

    print("Result:", result)

    with open("calculations.txt", "a") as file:
        numbers_text = " ".join(str(n) for n in numbers)
        if isinstance(result, str):
            file.write(f"{operation}: {numbers_text} = ERROR\n")
        else:
            file.write(f"{operation}: {numbers_text} = {result}\n")
