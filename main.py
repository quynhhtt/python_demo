# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def cal_income_tax(income: int, npt: int) -> float:
    fam_deduction = 11000000
    dependant_deduction = 2000000
    tax_interest = 0.1
    tax = (income - fam_deduction - dependant_deduction * npt) * tax_interest
    return tax


def cal_ielts_grade(reading: float, listening: float, speaking: float, writing: float) -> float:
    grade = round((reading + listening + speaking + writing) / 4, 1)
    return grade


def play_keo_bua_bao(p1: str, p2: str):
    if p1 == p2:
        print('Draw')
    elif p1 == 'keo' and p2 == 'bao':
        print('player 1 wins')
    elif p1 == 'bua' and p2 == 'keo':
        print('player 1 wins')
    elif p1 == 'bao' and p2 == 'bua':
        print('player 1 wins')
    else:
        print('player 2 wins')


def while_loop():
    a = int(input('Enter a number:'))
    while a < 100:
        print(a)
        a = int(input('Enter a number:'))


def keobuabao_loop():
    p1 = str(input('Enter player 1''s choice: '))
    p2 = str(input('Enter player 2''s choice: '))
    while (p1 == 'keo' and p2 == 'bao') or (p1 == 'bua' and p2 == 'keo') or (p1 == 'bao' and p2 == 'bua'):
        print('player 1 wins')
        p1 = str(input('Enter player 1''s choice: '))
        p2 = str(input('Enter player 2''s choice: '))


if __name__ == "__main__":
    # p1 = str(input('Enter player 1''s choice: '))
    # p2 = str(input('Enter player 2''s choice: '))
    # play_keo_bua_bao(p1=p1, p2=p2)

    keobuabao_loop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
