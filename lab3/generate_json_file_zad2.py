import json
import random


def generate_books_data(liczba_ksiazek=10000):
    bibliografia = {
        "Adam Mickiewicz": ["Dziady", "Pan Tadeusz", "Sonety krymskie"],
        "Henryk Sienkiewicz": ["Quo Vadis", "Ogniem i mieczem", "Krzyżacy"],
        "Juliusz Słowacki": ["Balladyna", "Kordian"],
        "Stefan Żeromski": ["Przedwiośnie", "Ludzie bezdomni"],
        "Bolesław Prus": ["Lalka", "Faraon"]
    }

    ksiazki = []
    for _ in range(liczba_ksiazek):
        autor = random.choice(list(bibliografia.keys()))
        tytul = random.choice(bibliografia[autor])
        wydanie = random.randint(1, 3)
        ksiazki.append({
            "tytul": tytul,
            "autor": autor,
            "wydanie": wydanie
        })

    return ksiazki


def generate_json_file(filename="data_zad2.json"):
    books = generate_books_data()  # Assuming that you have a function called 'generate_books_data'
    data = {"books": books}
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    generate_json_file()
