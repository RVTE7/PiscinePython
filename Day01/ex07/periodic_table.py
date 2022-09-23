from operator import index
import sys
from turtle import clear

def index7(list, delm):
    
    for i in range(len(list)):
        if list[i] == delm:
            return i

def txtToList(txt):

    with open(txt, 'r') as x:
        contents = x.read().split("\n")
        clearCont = contents[0].replace('=', ',').replace(' ', '').split(',')

    for i in range(1, len(clearCont)):
        nElem = index7(clearCont[i], ':')+1
        clearCont[i] = clearCont[i][nElem:]

    return clearCont

def printHtml():

    list = txtToList('periodic_table.txt')

    with open('test.html', 'w') as file:
        for i in range(len(list)):
            if i == 0:
                file.write("list[i] + '\n')

if __name__ == "__main__":
    printHtml()
