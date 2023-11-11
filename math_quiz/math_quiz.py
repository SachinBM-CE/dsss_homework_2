import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).

    :param min_value: The minimum value of the range.
    :param max_value: The maximum value of the range.
    :return: A random integer.
    """
    return random.randint(min_value, max_value)

def generate_operator():
    """
    Generate a random arithmetic operator (+, -, or *).

    :return: A random operator.
    """
    return random.choice(['+', '-', '*'])

def perform_arithmetic_operation(number1, number2, operator):
    """
    Perform an arithmetic operation on two numbers based on the given operator.

    :param number1: The first number.
    :param number2: The second number.
    :param operator: The arithmetic operator (+, -, or *).
    :return: A tuple containing the problem and its answer.
    """
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    problem = f"{number1} {operator} {number2}"
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_operator()

        problem, answer = perform_arithmetic_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
