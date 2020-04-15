import sys 
import pandas as pd 

""" The script takes the input in the following format :
   -> python formatter.py <path for the json file obtained through scrapper>
and the script produces the output in a file named scrapped_data.tsv """

# the following piece checks for the availability of the input
if len(sys.argv) == 1:
    print("Need Filename!")
    sys.exit(-1)
else:
    path = sys.argv[1]

# opening the file in read_only mode
try :
    file = open(path, "r")
except :
    print("File failed to open! Please verify if the path-name is correctly specified")
    quit()

# the input is expected as a json file and hence, the following piece of code is to extract all the relevant data from a json file
tag = 0
for each in file:
    if tag == 1 :
        data = each[:-1]
        break
    tag = tag + 1
file.close()

# formatting the data
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


# encoding the data into a pandas data_frame
dataset = [[] for i in range(len(column_data[0]))]
i = 0
while i < len(column_data[0]):
    j = 0
    aux = []
    while j < len(columns):
        aux.append(column_data[j][i])
        j = j + 1
    dataset[i] = aux
    i = i + 1

# saving the data as a tab-seperated file using pandas
df = pd.DataFrame(dataset, columns = columns)
df.to_csv("scrapped_data.tsv", sep = "\t", index = False)

print(df.head())