
import csv
import json

def count_word(path):
    file = open(path, encoding="utf8")
    content = file.read()
    count = content.split()
    print(f'the count if word is {len(count)}')
    file.close()

def writeToCsvFile(list):
    with open("data.csv", "w", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(list)
        file.close()
    with open("data.csv", "r", encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

def writeToJSONFile(dict):
    with open("data.json", "w", encoding="utf8") as file:
        json.dump(dict, file)
        file.close()
    with open("data.json", "r", encoding="utf8") as file:
        reader = json.load(file)
        for row in reader:
            print(f'{row} : {dict[row]}')
        file.close()


list = [
    {'firstName': 'shira', 'lastName': 'shemesh','age':20 ,'address':'Haritva'},
    {'firstName': 'noa', 'lastName': 'choen', 'age': 5, 'address': 'Avi-Ezri'},
    {'firstName': 'Michal', 'lastName': 'Levi', 'age': 10, 'address': 'Avnei_nezer'},
    {'firstName': 'Chaia', 'lastName': 'Chazan', 'age': 15, 'address': 'Rashba'},
]

dict = {'firstName': 'shira', 'lastName': 'shemesh','age':20 ,'address':'Haritva'}
# count_word('hello.txt')

writeToCsvFile(list)

writeToJSONFile(dict)
=======
import csv
import json

def count_word(path):
    file = open(path, encoding="utf8")
    content = file.read()
    count = content.split()
    print(f'the count if word is {len(count)}')
    file.close()

def writeToCsvFile(list):
    with open("data.csv", "w", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(list)
        file.close()
    with open("data.csv", "r", encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
        file.close()

def writeToJSONFile(dict):
    with open("data.json", "w", encoding="utf8") as file:
        json.dump(dict, file)
        file.close()
    with open("data.json", "r", encoding="utf8") as file:
        reader = json.load(file)
        for row in reader:
            print(f'{row} : {dict[row]}')
        file.close()


list = [
    {'firstName': 'shira', 'lastName': 'shemesh','age':20 ,'address':'Haritva'},
    {'firstName': 'noa', 'lastName': 'choen', 'age': 5, 'address': 'Avi-Ezri'},
    {'firstName': 'Michal', 'lastName': 'Levi', 'age': 10, 'address': 'Avnei_nezer'},
    {'firstName': 'Chaia', 'lastName': 'Chazan', 'age': 15, 'address': 'Rashba'},
]

dict = {'firstName': 'shira', 'lastName': 'shemesh','age':20 ,'address':'Haritva'}
# count_word('hello.txt')

writeToCsvFile(list)

writeToJSONFile(dict)
 5712252 (Initial commit)
