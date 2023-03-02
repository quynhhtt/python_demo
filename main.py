# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def cal_income_tax(income: int, npt: int) -> float:
    fam_deduction = 11000000
    dependant_deduction = 2000000
    tax_interest = 0.1
    tax = (income - fam_deduction - dependant_deduction * npt) * tax_interest
    return tax

def cal_ielts_grade(reading:float, listening:float, speaking:float, writing:float) -> float:
    grade = round((reading + listening + speaking + writing)/4, 1)
    return grade

if __name__ == "__main__":
    reading = float(input('Enter reading score: '))
    listening = float(input('Enter listening score: '))
    speaking = float(input('Enter speaking score: '))
    writing = float(input('Enter writing score: '))
    print(cal_ielts_grade(reading=reading, listening=listening, speaking=speaking, writing=writing))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
