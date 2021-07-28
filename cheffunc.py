import copy

vegetables = ["Артишок", "Кукуруза", "Капуста", "Помидор", "Огурец", "Свекла",
              "Картофель", "Перец", "Морковь", "Горох", "Баклажан", "Укроп",
              "Лук"]
salad = {}
vegetables_calorie = {
    "Артишок": 29,
    "Кукуруза": 97,
    "Капуста": 28,
    "Помидор": 20,
    "Огурец": 15,
    "Свекла": 48,
    "Картофель": 83,
    "Перец": 27,
    "Морковь": 33,
    "Горох": 72,
    "Баклажан": 24,
    "Укроп": 32,
    "Лук": 34
}
vegetables_cost = {
    "Артишок": 1.5,
    "Кукуруза": 0.5,
    "Капуста": 0.4,
    "Помидор": 1.1,
    "Огурец": 1,
    "Свекла": 0.9,
    "Картофель": 0.7,
    "Перец": 2.2,
    "Морковь": 0.8,
    "Горох": 0.95,
    "Баклажан": 1.2,
    "Укроп": 0.3,
    "Лук": 0.45
}
count = 0
flag = True
salad_call = {}
cost_salad = {}
def welcom():
    print("Приветствуем в нашем ресторане! Ознакомьтесь с нашим ассортиметом:")
def sorted_cost():
    print("\nСписок овщей согласно стоимости:\n")
    copy_vegetables = copy.deepcopy(vegetables)
    for value in sorted(vegetables_cost.values()):
        for key in copy_vegetables:
            if vegetables_cost[key] == value:
                copy_vegetables.remove(key)
                print(key, "-", value)
def sortded_calorie():
    print("\nСписок овщей согласно калорийности:\n")
    copy_vegetables = copy.deepcopy(vegetables)
    for value in sorted(vegetables_calorie.values()):
        for key in copy_vegetables:
            if vegetables_calorie[key] == value:
                copy_vegetables.remove(key)
                print(key, "-", value)
def yes_or_no(text):
    step = input(text)
    if step.lower() != "да" and step.lower() != "нет":
        return step

welcom()
sorted_cost()
sortded_calorie()
our_answer = input("Хотите сделать салат(да/нет): ")
while True:
    if our_answer.lower() == "да":
        print("Сделайте свой салат из овощей, находящихся в списке!")
        while True:
            our_vegetable = yes_or_no("Введите название овоща или закончите делать салат('для завершения нажми' /готово): ")
            if our_vegetable.lower() != "готово":
                if our_vegetable in vegetables_calorie:
                    if our_vegetable not in salad:
                        salad[our_vegetable] = vegetables_calorie[our_vegetable]
                    elif our_vegetable in salad:
                        print("Этот овощ уже в салате, добавьте другой овощ!")
                else:
                    print("Такого овоща нет в списке!")
            elif our_vegetable.lower() == "готово":
                if len(salad) > 0:
                    print("Вот какой салат у тебя получился:")
                    for key in salad:
                        print(key)
                    print("Сортировка овощей в салате на основе калорийности:")
                    copy_vegetables = copy.deepcopy(vegetables)
                    for value in sorted(salad.values()):
                        for key in copy_vegetables:
                            if key in salad:
                                if salad[key] == value:
                                    copy_vegetables.remove(key)
                                    print(key, "-", value)
                    break
                elif len(salad) == 0:
                    print("Ты не сделал свой салат. Увидимя в другой раз!")
                    break
        break
    else:
        print("Было приятно помочь вам! До скорой встречи! Спасибо что выбрали наше приложение!")
        break
if len(salad) != 0:
    while True:
        my_answer = input("Хочешь найти овощи в салате, соответствующие заданному диапазону калорийности(да/нет)?")
        if my_answer.lower() == "да":
            print("Овощи в салате из какого диапазона вам интересны")
            my_calorie_content_1 = input("Нижний диапазон:")
            my_calorie_content_2 = input("Верхнийний диапазон:")
            count = 0
            for value_calorie in salad.values():
                if int(my_calorie_content_1) <= value_calorie <= int(my_calorie_content_2):
                    for key in salad:
                        if salad[key] == value_calorie:
                            print("Овощ", key, ", содержащий", salad[key], "каллорий, "
                                  "лежит в вашем диапазоне от", my_calorie_content_1, "до", my_calorie_content_2)
                            count += 1
            if count == 0:
                print("Овощ, содержащий колличество каллорий "
                      "в вашем диапазоне от", my_calorie_content_1, "до",my_calorie_content_2,
                      "отсутствует в салате!")
        if my_answer.lower() == "нет":
            print("До скорой встречи, спасибо что выбрали наше приложение!")
        break
if len(salad) != 0:
    sum_salad = sum(salad.values())
    print('Ваш салат получает: '+str(sum_salad)+' ккал.')
print("До скорой встречи, спасибо что выбрали наше приложение!")



