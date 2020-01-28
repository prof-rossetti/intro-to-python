# custom-functions/my_functions.py

def celsius_to_fahrenheit(temp):
    """
    Converts a Celsius temperature to a Fahrenheit temperature, using the standard conversion formula.

    Param: temp (float) like 0

    Returns: the corresponding temp (float), like 32.0
    """
    return (temp * 9 / 5) + 32

def numeric_to_letter_grade(numeric_score):
    """
    Converts a numeric score to a letter grade, using the standard grading scale.

    Param: numeric_score (float) from 0 to 100, like 87.5

    Returns: the corresponding letter grade (str), like "B+"
    """
    if numeric_score >= 97.0:
        letter_grade = "A+"
    elif numeric_score >= 93.0:
        letter_grade = "A"
    elif numeric_score >= 90.0:
        letter_grade = "A-"
    elif numeric_score >= 87.0:
        letter_grade = "B+"
    # etc...
    else:
        letter_grade = "F"

    return letter_grade

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = input("PLEASE INPUT A CELSIUS TEMP: ")
    c = float(c) # convert str to float
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

    print("--------------------")
    score = input("PLEASE INPUT A NUMERIC GRADE: ")
    score = float(score) # convert str to float
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)
