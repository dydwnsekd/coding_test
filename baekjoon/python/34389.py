"""
import sys

n = int(sys.stdin.readline())
plan_dict = {"Marble": [19, 200], "Marble+": [19, 350], "Quartz": [14, 200], "Quartz+": [14, 350]}

for _ in range(n):
    name, plan, meal_count, money = sys.stdin.readline().strip().split()
    meal_count = int(meal_count)
    money = float(money)

    plan_meal_count = plan_dict[plan][0]
    plan_money = plan_dict[plan][1]

    '''
    Use meal swipe or munch money --- the student has meal swipes left and munch money left,
    Use munch money --- the student has no meal swipes left, but has munch money,
    Use meal swipe --- the student has no munch money left, but has meal swipes remaining,
    Go to Downtown Golden! --- the student has no munch money and no meal swipes remaining.
    '''

    if meal_count < plan_meal_count and money < plan_money:
        # Ethan 2 24.33 Use meal swipe or munch money
        print(f"{name} {plan_meal_count - meal_count} {plan_money - money:.2f} Use meal swipe or munch money")
    elif meal_count == plan_meal_count and money < plan_money:
        print(f"{name} {plan_meal_count - meal_count} {plan_money - money:.2f} Use munch money")
    elif meal_count < plan_meal_count and money == plan_money:
        print(f"{name} {plan_meal_count - meal_count} {plan_money - money:.2f} Use meal swipe")
    elif meal_count == plan_meal_count and money == plan_money:
        print(f"{name} {plan_meal_count - meal_count} {plan_money - money:.2f} Go to Downtown Golden!")
"""


import sys

plan_info = {
    "Marble":  (19, 200.0),
    "Marble+": (19, 350.0),
    "Quartz":  (14, 200.0),
    "Quartz+": (14, 350.0),
}

ACTION = {
    (True,  True):  "Use meal swipe or munch money",
    (False, True):  "Use munch money",
    (True,  False): "Use meal swipe",
    (False, False): "Go to Downtown Golden!",
}

n = int(sys.stdin.readline().strip())

for _ in range(n):
    name, plan, used_meals_str, used_money_str = sys.stdin.readline().strip().split()
    used_meals = int(used_meals_str)
    used_money = float(used_money_str)

    total_meals, total_money = plan_info[plan]
    left_meals = total_meals - used_meals
    left_money = total_money - used_money

    action = ACTION[(left_meals > 0, left_money > 0)]
    print(f"{name} {left_meals} {left_money:.2f} {action}")

