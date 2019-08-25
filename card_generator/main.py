import file_operations
from random import randint, sample
from faker import Faker

number_of_cards = 10


def generate_template():
    fake = Faker("ru_RU")
    skills = ["Стремительный прыжок",
              "Электрический выстрел",
              "Ледяной удар",
              "Стремительный удар",
              "Кислотный взгляд",
              "Тайный побег",
              "Ледяной выстрел",
              "Огненный заряд"]

    unit_skills = sample(skills, 3)
    runic_skills = []

    for skill in unit_skills:
        runic_skills.append(convert_prase_to_runic(skill))

    context = {
        "first_name": fake.first_name().replace("е", "е͠"),
        "last_name": fake.last_name(),
        "town": fake.city(),
        "job": fake.job(),
        "strength": randint(8, 14),
        "agility": randint(8, 14),
        "endurance": randint(8, 14),
        "intelligence": randint(8, 14),
        "luck": randint(8, 14),
        "skill_1": runic_skills[0],
        "skill_2": runic_skills[1],
        "skill_3": runic_skills[2]
    }

    return context


def convert_phrase_to_runic(phrase):
    runic_letters = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }

    for letter in phrase:
        phrase = phrase.replace(letter, runic_letters[letter])

    return phrase


for card in range(number_of_cards):
    file_operations.render_template("charsheet.svg", "charsheets/charsheet-{}.svg".format(card), generate_template())
