import time
name = input("Enter your name:  ")
weight  = float(input("Enter your weight in pounds:  "))
height = float(input("Enter your height in inches:  "))
bmi = (weight * 703) / pow(height, 2)


if bmi < 18.5 :
    category = "Underweight"
    health_risk = "Minimal"
    time.sleep(3)
    print(f"Your BMI is {bmi:.2f}")
    time.sleep(3)
    print(f"{name}, you are {category} and you have a {health_risk} health risk")
elif bmi >= 18.5 and bmi <= 24.9 :
    category = "Normal Weight"
    health_risk = "Minimal"
    time.sleep(3)
    print(f"Your BMI is {bmi:.2f}")
    time.sleep(3)
    print(f"{name}, you are {category} and you have a {health_risk} health risk")
elif bmi >= 25 and bmi <= 29.9 :
    category = "Overweight"
    health_risk = "Increased"
    time.sleep(3)
    print(f"Your BMI is {bmi:.2f}")
    time.sleep(3)
    print(f"{name}, you are {category} and you have an {health_risk} health risk")
elif bmi >= 30 and bmi <= 34.9 :
    category = "Obese"
    health_risk = "High"
    time.sleep(3)
    print(f"Your BMI is {bmi:.2f}")
    time.sleep(3)
    print(f"{name}, you are {category} and you have a {health_risk} health risk")
elif bmi >= 35 and bmi <= 39.9 :
    category = "Severely Obese"
    health_risk = "Very High"
    time.sleep(3)
    print(f"Your BMI is {bmi:.2f}")
    time.sleep(3)
    print(f"{name}, you are {category} and you have a {health_risk} health risk")
elif bmi >= 40 :
    category = "Morbidly Obese"
    health_risk = "Extremely High"
    time.sleep(3)
    print(f"Your BMI is {bmi:.2f}")
    time.sleep(3)
    print(f"{name}, you are {category} and you have a {health_risk} health risk")
# Made by ~tobi_adabs