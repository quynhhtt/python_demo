# This is a sample Python script.
from typing import List


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


def play_keo_bua_bao_with_p1_win(p1: str, p2: str) -> bool:
    if p1 == p2:
        return False
    elif p1 == 'keo' and p2 == 'bao':
        return True
    elif p1 == 'bua' and p2 == 'keo':
        return True
    elif p1 == 'bao' and p2 == 'bua':
        return True
    else:
        return False


def while_loop():
    a = int(input('Enter a number:'))
    while a < 100:
        print(a)
        a = int(input('Enter a number:'))


def keo_bua_bao_loop():
    p1 = str(input('Enter player 1''s choice: '))
    p2 = str(input('Enter player 2''s choice: '))
    while play_keo_bua_bao_with_p1_win(p1=p1, p2=p2):
        print('player 1 wins')
        p1 = str(input('Enter player 1''s choice: '))
        p2 = str(input('Enter player 2''s choice: '))


def swap_dau_cuoi(num_list: List) -> list:
    temp = num_list[0]
    num_list[0] = num_list[-1]
    num_list[-1] = temp
    return num_list


def find_max_number_in_list(list1: List) -> int:
    max_num = 0
    for i in list1:
        if i > max_num:
            max_num = i
    return max_num


def find_second_max_number_in_list(list1: List) -> int:
    max_num = 0
    max_2nd_num = 0
    for i in list1:
        if i > max_num:
            max_2nd_num = max_num
            max_num = i
        elif i != max_num and i > max_2nd_num:
            max_2nd_num = i
    return max_2nd_num


def find_min_number_in_list(list1: List) -> int:
    min_num = 0
    for i in list1:
        if i < min_num:
            min_num = i
    return min_num


def find_second_min_number_in_list(list1: List) -> int:
    min_num = 99
    min_2nd_num = 99
    for i in list1:
        if i < min_num:
            min_2nd_num = min_num
            min_num = i
        elif i != min_num and i < min_2nd_num:
            min_2nd_num = i
    return min_2nd_num


if __name__ == "__main__":
    # p1 = str(input('Enter player 1''s choice: '))
    # p2 = str(input('Enter player 2''s choice: '))
    # play_keo_bua_bao(p1=p1, p2=p2)

    list_of_number = [1, 5, 2, 6, 9, 8, 7, 4, 5, 9, 9, 1, 2, 4]
    # total = 0
    # for number in list_of_number:
    #     if number % 2 != 0:
    #         total = number + total
    # print(total)


    num_list = [1, 2, 3, 4, 5, 6]
    # new_list = swap_dau_cuoi(num_list=num_list)
    # print(new_list)

    print(find_second_min_number_in_list(list1=list_of_number))


# numlist = [1, 2, 3, 4, 5, 6]
# p1 = int(input('Position 1: '))
# p2 = int(input('Position 2: '))
# temp = numlist[p1]
# numlist[p1] = numlist[p2]
# numlist[p2] = temp
# print(numlist)
