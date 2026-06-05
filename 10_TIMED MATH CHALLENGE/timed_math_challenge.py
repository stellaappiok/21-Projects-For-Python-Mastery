import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = int(input("What is the minium operand? "))
MAX_OPERAND = int(input("What is the maximum operand? "))
TOTAL_PROBLEMS = int(input("What is the maximum number of questions? "))


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press 'ENTER' to start")
print("-----------------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break

        wrong += 1


end_time = time.time()
total_time = round(end_time - start_time)
print("-----------------------")
print(f"Time used: {total_time} seconds!")

if wrong == 0:
    print("Excellent work done!")
    print(f"You got {wrong} problems wrong")

elif wrong <= 3:
    print("Nice work done!")
    print(f"You got {wrong} problems wrong")

elif wrong <= 5:
    print("It's okay, bit could better!")
    print(f"You got {wrong} problems wrong")

else:
    print("Are you serious right now !")
    print(f"You got {wrong} problems wrong")
print("")
