
import math

#1 Завдання
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def term(k,x,a):
    if a+x == 0 and k > 0:
        print("Error: Division by zero")
    result = pow(a+x, -k) / (pow(a, 2*k+1) + fact(k**2))
    return result

def calculate_sum(M, x, a):
    total_sum = 0
    for k in range(M):
        total_sum += term(k, x, a)
    return total_sum

def task1():
    a = float(input("Enter a: "))
    x = float(input("Enter x: "))
    eps = float(input("Enter accuracy: "))
    N = int(input("Enter number of terms: "))
    s1 = calculate_sum(N, x, a)
    N *= 2
    s2 = calculate_sum(N, x, a)
    while abs(s2-s1) > eps:
        s1 = s2
        N *= 2
        s2 = calculate_sum(N, x, a) 
    print(f"Result: {s2}, Number of terms: {N}")

# 2 Завдання      
def task2():
    x = float(input("Input starting (x): "))
    eps = float(input("Enter accuracy: "))
    a_0 = x
    for i in range(1, 101):
        a_curr = 1/5 * (a_0 + (3*x/a_0))
        if abs(a_curr - a_0) < eps:
            print(f"Result: {a_curr}, Number of iterations: {i}")
            break
        a_0 = a_curr
    else:
        print("Did not converge within 100 iterations.")

# 3 Завдання
def clean_text(text):
    cleaned = ""
    for char in text:
        if char.isalnum():
            cleaned += char
        else:
            cleaned += " "
    return cleaned

def task3():
    words3 =  []
    text1 = input("Enter first text: ")
    text2 = input("Enter second text: ")
    clean_text1 = clean_text(text1)
    clean_text2 = clean_text(text2)
    words1 = clean_text1.lower().split()
    words2 = clean_text2.lower().split()
    for word in words1:
        if word not in words2 and word not in words3:
            words3.append(word)
    text3 = " ".join(words3)
    print(f"Result: {text3}")

# 4 Завдання
def task4():
        digits = "0123456789ABCDEF"
        def dec_to_hex(n):
            if n < 16:
                return digits[n]
            else:
                return dec_to_hex(n // 16) + digits[n % 16]
        num = int(input("Enter a decimal number: "))
        if num < 0:
            hex_value = "-" + dec_to_hex(abs(num))
        else:
            hex_value = dec_to_hex(num)
        print(f"Hexadecimal representation: {hex_value}")

while True:
    print("\n ГОЛОВНЕ МЕНЮ ")
    print("1 Завдання")
    print("2 Завдання ")
    print("3 Завдання ")
    print("4 Завдання ")
    print("0. Вийти з програми")
    
    choice = input("Оберіть пункт меню: ")
    
    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        task4()
    elif choice == "0":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2, 3, 4 або 0.")