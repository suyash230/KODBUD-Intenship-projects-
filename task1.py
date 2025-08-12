print("Simple Calculator (CLI) :-")
n = int(input("how many numbers do you want to operate :- "))

li = []

for i in range(n):
    k = int(input(f"enter your {i+1}th number :- "))
    li.append(k)

operater = input("enter your operator (+ , * , - , /) :- ")
result = li[0]

if operater == "+":
    for num in li[1:]:
        result += num
elif operater == "-":
    for num in li[1:]:
        result -= num
elif operater == "*":
    for num in li[1:]:
        result *= num
elif operater == "/":
    for num in li[1:]:
        if num != 0:
            result /= num
        else:
            result = "Error Division by zero."
            break
else:
    result = "Invalid operator."

print("Result:", result)
