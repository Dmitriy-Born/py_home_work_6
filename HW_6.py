import fileinput

fileName = 'tel.txt'

def writeFile(file_name):
    with open (file_name, 'a') as data: #с with не надо закрывать файл (он закроется автоматически после исполнения)
        data.writelines("Hello world\n")


def readFile(file_name):
    result = []
    with open (file_name, 'r+') as data: 
        for line in data:
            result.append(line.split())
    return result

def findUsers(userList):
    name = 'Ivan,'
    for user in userList:
        if user[1] == name:
            print (user[3])


def deleteFile(userList): #Реализация функции "удаления строки из файла"
    nameDel = 'Ivan,'
    for line in fileinput.input(userList, inplace=True):
        if nameDel in line:
            continue
        print(line, end='')

            
print(readFile(fileName))
findUsers(readFile(fileName))
deleteFile(fileName)
print(readFile(fileName))