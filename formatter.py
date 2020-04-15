import pandas as pd 

file = open("dummy.json", "r")

tag = 0
for each in file:
    if tag == 1 :
        data = each[:-1]
        break
    tag = tag + 1
file.close()

i = 0
columns = []
dataset = []
while i < len(data):
    if data[i] == ":":
        if data[i-1] == '"':
            name = ""
            j = -2
            while data[i+j] != '"':
                name = name + data[i+j]
                j = j - 1
            columns.append(name[::-1])
            aux = ""
            tag = 0
            while data[i] != "]":
                if data[i] == "[":
                    tag = 1
                    i = i + 1
                if tag == 1:
                    aux = aux + data[i]
                i = i + 1
            dataset.append(aux)
    i = i + 1

column_data = [[] for i in range(len(columns))]

tag = 0
for each in dataset:
    i = 0
    while i < len(each):
        if each[i] == '"':
            word = ""
            i = i + 1
            while each[i] != '"':
                word = word + each[i]
                i = i + 1
            column_data[tag].append(word)
        i = i + 1
    tag = tag + 1

dataset = [[] for i in range(len(column_data[0]))]
i = 0
while i < len(column_data[0]):
    dataset[i] = [column_data[0][i], column_data[1][i]]
    i = i + 1

df = pd.DataFrame(dataset, columns = columns)

df.to_csv("scrapped.tsv", sep = "\t", index = False)