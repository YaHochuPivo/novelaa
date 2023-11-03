import json
import csv
import os



def year_namer(age):
    str_age = str(age)
    end_num = int(str_age[len(str_age)-1])
    if end_num == 1:
        return "год"
    elif 1 < end_num < 5:
        return "года"
    else:
        return "лет"
def verb_choicer():
    global verbs_num
    verbs_num += 1
    if gender == "муж":
        return verbs_male[verbs_num]
    else:
        return verbs_female[verbs_num]
things = []

print("Привет! Это консольная новелла!")

choice = None

print("""
1. Начало истории
2. Конец игры
""")
while choice != 3:
    choice = input("Выберите номер пункта: ")
    if choice == "1":
        print("Вы выбрали историю!")
        break
    elif choice == "2":
        print("Конец игры!")
        exit()
    else:
        print("Некорректный ввод!")
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
gender = input("Введите ваш пол(муж/жен): ")
verbs_num = -1
verbs_male = [" не заметил","подумал", "направился", "приехал", "подумал", "обернулся", "обратил", "подумал", "слышал", "прошептал","взял","набрал","подошёл", "Сам","просунул", "заслонял", "достал"]
verbs_female = [" не заметила", "подумала", "направилась", "приехала", "подумала", "обернулась","обратила", "подумала", "слышала","прошептала","взяла","набрала","подошла","Сама","просунула", "заслоняла", "достала"]
output = f"Ваше имя: {name}. Возраст: {age}. Пол: {gender}. Начинаем...."
print(output)
print("❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆")
print("Глава 1. Первый снег.")
print(input())
print("Первого снега")
print(input())
print("Горсть не сумеет")
print(input())
print("Склонить лист гладиолуса...\n~ Мацуо Басё ~")
print("❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆")
print(input())
print("Триста четырнадцатая осень эпохи Ириса в империи Нойрё выдалась холодной.\nНебо над постоялым двором 'Белая цапля' быстро темнело.")
print(input())
print(f"{name}{verb_choicer()} как холодный ветер шевельнул волосы, забрался под воротник. Стало неуютно и тревожно.")
print(input())
print(f"'Проверить багаж и скорее вернуться к госпоже Сумико...', --- {verb_choicer()} {name}.")
print(input())
print(f"Зябко поёжившись, {name} быстро {verb_choicer()} к повозке, на которой {verb_choicer()} со своей наставницей.")
print(input())
print("Во дворе оказалось ещё несколько крытых телег, видимо, прибывших позже.\nРядом был разложен костёр, вокруг сидели воины. Вечерние сумерки бросили тени на лица, сделав их неприятными и грубыми.")
print(input())
print(f"'У того, что слева, два меча. Самурай.', --- {verb_choicer()} {name}")
print(input())
print("Пройти мимо воинов незаметно не получилось. Окликнули...")
print(input())
print("'Постой.', --- сказал Самурай")
print(input())
print(f"{name} {verb_choicer()}, склонившись в почтительном поклоне.")
print(input())
print("'Возьми флягу, напои его', --- приказал Самурая, отводя руку в сторону. Куда-то за себя.")
print(input())
print(f"Только теперь {name} {verb_choicer()} внимание - за кругом света, на одной из повозок, стояла клетка, в которой находился скованный человек.\nСлишком лёгкая для этой погоды одежда была грязной и кое-где порвалась.\nИзраненные кандалами руки покрывала корка запёкшейся крови. Но на бледном лице живо горели злые глаза.")
print("Словно иглой кольнул цепкий взгляд пленника...")
print(input())
print(f"'Надменная гордость, будто он не в клетке сидит... Вдруг убийца?', --- {verb_choicer()} {name}")
print(input())
print(f"'Эй, не {verb_choicer()} что я велел?', --- недовольным голосом произнёс Самурай")

while True:


    print("❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆")
    print("'Простите, господин...'")
    print(" 1. Я боюсь")
    print(" 2. Я сейчас")
    print("❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆❆")
    vibor = input()
    if vibor == "":
        continue
    if int(vibor) == 1:

        print(f"'Простите, господин, я боюсь', --- {verb_choicer()} {name}\n'Ишь какие робкие пошли... Он в клетке и кандалах - не укусит', --- прыснул Самурай'");
        break
    if int(vibor) == 2:
        print(f"'Простите, господин, я сейчас.', --- {verb_choicer()} {name}");
        break


print("Один из воинов протянул флягу.")
print(input())
print("'Глупо перечить самураю...'")
print(input())
print(F"{name} {verb_choicer()},{verb_choicer()} воды из бочки, стоявшей у конюшни. Затем медленно {verb_choicer()} к преступнику.")
print(input())
print("'Не бойся, не съем.', --- внезапно произнёс пленник.\nОн прислонился к решётке. Голос оказался шершавым, будто галька перекатывается.")
print(input())
print(f"'Ближе.{verb_choicer()} напои, у меня пальцы затекли.', --- попросил пленник")
print(input())
print(f"{name} {verb_choicer()} осторожно флягу между прутьями. Разбитые губы мягко прижались к горлышку.")
print(input())
print("Рука дрогнула. По подбородку пленника пробежала капля. Он неожиданно улыбнулся.")
print(input())
print("'Не бойся меня. Та женщина твоя наставница?', --- спросил пленник, указывая головой в сторону повозки, возле которой стояла изящная женщина средних лет -- гейша")
print(input())
print("'Да...', --- прозвучал робкий ответ.")
print(input())
print("'Эй! Что ты там бормочешь?', --- крикнул Самурай.")
print(input())
print(f"Преступник подмигнул. Насколько позволяла клетка, сдвинулся так, чтобы {name} не {verb_choicer()} от него самурая.")
print("'Говорю, позор мне. Меня поймали убогие слепцы.', --- внезапно съязвил пленник.")
print(input())
print("'Попридержи язык, если хочешь прожить ещё несколько дней.', --- ответил Самурай")
print(input())
print("'Ничего ты мне не сделаешь. Ты должен отвезти меня в город живым.', --- с насмешкой ответил преступник")
print(input())
print("'На казнь можно доставить и без языка!', --- воскрикнул Самурай")
print(input())
print("В презрительном взгляде пленника не было и тени страха.")
print(input())
print("'А ты чего здесь так долго стоишь? Возвращайся к своей повозке.', --- переведя взгляд на меня сказал Самурай")
print(input())
print("'Лучше пойду, дабы проблем не нахватать.... Нужно ещё багаж проверить.'")
print(input())
print(f"Подойдя к своей повозке {name} {verb_choicer()} красивый синий сундук с золотыми вставками.Что же там было?")
while True:

    thing = input("Какую ещё вещь вы видите в сундуке?(Если не видите больше вещей, напишите 'нет')")
    if thing == "нет":
        break
    things.append(thing)

for thing in things:
    print(thing)

haracteristica_person = [{"Имя":name, "Возраст":age, "Пол":gender}]

if os.path.exists('data.json'):
   with open('data.json', 'r') as file:
      data = json.load(file)
      data["haracteristica_person"].append((haracteristica_person))

else:
    data = {"haracteristica_person": []}
    data["haracteristica_person"].append((haracteristica_person))

with open('data.json', 'w') as file:
    json.dump(data, file)

with open('output.csv', 'a', newline='', encoding='cp1251') as file:
   fieldnames = ['Возраст', 'Пол', 'Имя']
   writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
   writer.writeheader()
   writer.writerows(haracteristica_person)


print("Хотите удалить сохранения?")
print("1. Да")
print("2. Нет")

vibor2 = input()
if int(vibor2) == 1:
    print("Вы удалили сохранение")
    os.remove("C:\\Users\\eliza\\PycharmProjects\\pythonProject4\\output.csv")
    os.remove("C:\\Users\\eliza\\PycharmProjects\\pythonProject4\\data.json")
else:
    pass
