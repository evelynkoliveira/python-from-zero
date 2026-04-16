def calculate_bmi (weight, height):
    return weight / (height ** 2)
    
def classify_bmi (bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"
    
print("BMI Calculator")
print("-" * 20)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
classification = classify_bmi(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {classification}")
