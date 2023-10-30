import json
import csv

class SaveManager:
    def init(self, save_file, csv_file):
        self.save_file = save_file
        self.csv_file = csv_file

    def save_data(self, user_data):

        if self.save_file.exists():
            with open(self.save_file, 'r') as file:
                data = json.load(file)
        else:
            data = {}


        data[user_data.name] = user_data.to_dict()


        with open(self.save_file, 'w') as file:
            json.dump(data, file)


        self.update_csv_file(data)

    def delete_data(self, user_name):

        if self.save_file.exists():
            with open(self.save_file, 'r') as file:
                data = json.load(file)
        else:
            data = {}


        if user_name in data:
            del data[user_name]


        with open(self.save_file, 'w') as file:
            json.dump(data, file)


        self.update_csv_file(data)

    def update_csv_file(self, data):

        csv_data = [["name", "age", "iq"]]
        for user_data in data.values():
            csv_data.append([user_data["name"], user_data["age"], user_data["iq"]])


        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        save_manager = SaveManager(save_file="save_data.json", csv_file="game_data.csv")


        user_data = {
            "name": "Rustam",
            "age": 100,
            "iq": 5
        }
        save_manager.save_data(user_data)


        user_name = "Rustam"
        save_manager.delete_data(user_name)
import random



def generate_random_number():
    return random.randint(1, 10)



def get_player_name():
    name = input("Введите ваше имя: ")
    return name



def print_greeting(name):
    print("Привет, " + name + "! Добро пожаловать в игру не на жизнь, а на смерть!!!!")
    print("Вы очутились в тёмной комнате и видите перед собой Страшное существо")
    print("Вы решаете позвать его")
    print("Тут он резко оборачивается и предлагает игру, в случае победы которой, он вас отпустит")
    print("Он решает задать вам три вопроса")

def play_game():
    player_name = get_player_name()
    print_greeting(player_name)


    questions = [
        "Как зовут самого лучшего преподавателя?)",
        "Сколько пар у нас с ней в неделю?",
        "Сколько бы пар вы хотели с ней?"
    ]


    answers = {
        "Как зовут самого лучшего преподавателя?)": "Татьяна Артамонова",
        "Сколько пар у нас с ней в неделю?": "одна, а хотелось бы больше)",
        "Сколько бы пар вы хотели с ней?": "десять"
    }


    correct_answers = set()

    for question in questions:
        print(question)
        user_answer = input("Введите ответ: ")


        if user_answer.lower() == answers[question].lower():
            print("Правильный ответ, да вы гений!")
            correct_answers.add(question)
        else:
            print("Неправильный ответ, учи уроки, неуч!")

    print("Вы ответили правильно на следующие вопросы:")
    for answer in correct_answers:
        print("- " + answer)



play_game()
