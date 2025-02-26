def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("***Hi!! Welcome to the BMI Calculator!***")
    
    while True:
        try:
            weight = float(input("\nEnter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
            
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"Category: {category}")
            
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")

if __name__ == "__main__":
    main()