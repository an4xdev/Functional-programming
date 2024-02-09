from itertools import islice
import ijson
import pprint

def streamGenerator():
    with open("data_zad2.json", 'r', encoding='utf-8') as file:
        books = ijson.items(file, 'books.item')
        for book in books:
            yield book
            
items = filter(lambda b: b["wydanie"] == 1 and b["autor"] == "Adam Mickiewicz",streamGenerator())


def streamGeneratorWithPages(streamGenerator):
    l = []
    for i in streamGenerator:
        if len(l) > 10:
            yield l
            l = []
        else:
                l.append(i)
            
something = streamGeneratorWithPages(items)

pprint.pprint(list(islice(something, 3)))