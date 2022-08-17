

weight = float(input("What is your weight in kilograms? ") )
height = float(input("What is your height in meters? "))

bmi = round(weight / (height**2),1)

print(f"Your BMI is {bmi}.")

print("""
      BMI Scale:
      Underweight = < 18.5
      Normal weight = 18.5 - 24.9
      Overweight = 25 - 29.9
      Obese = 30+
      """)
if bmi <= 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
    
weight_goal = float(input("What is your target weight in kilograms? "))

print(f"You are {weight - weight_goal}kg away from target. This means you need to shed {7700 * (weight - weight_goal)} calories net of daily intake.")

print("Let's calculate your base metabolic rate (BMR).")
age = int(input("What is your age? "))
gender = input("What is your gender? M/F ")

if gender == "F":
    bmr = 447.593 + (9.247*weight) + (3.098*height*100) - (4.330*age)
    print(f"Your BMR is {bmr}.")
else:
    bmr = 88.362 + (13.397*weight) + (4.799*height*100) - (5.677*age)
    print(f"Your BMR is {bmr}.")