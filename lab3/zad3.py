from itertools import islice
from datetime import datetime

def octoberFilter(el):
    return el.split("-")[1] == "10"

def readFromFile(filterFunction):
    sumOfTransactions = 0
    recent_transactions = []
    with open("transactions.csv") as file:
        for line in file:
            sliced = line.split(",")
            dateFormated = datetime.strptime(sliced[0].split(" ")[0], "%Y-%m-%d").strftime('%d-%m-%Y')
            if filterFunction(dateFormated):
                sumOfTransactions += int(sliced[1])
                recent_transactions.append(int(sliced[1]))
                if len(recent_transactions) > 10:
                    recent_transactions.pop()
                avg = sum(recent_transactions) / len(recent_transactions)
                yield [dateFormated, sumOfTransactions, avg]
            
items = readFromFile(octoberFilter)
print(list(islice(items, 20)))