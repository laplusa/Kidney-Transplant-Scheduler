#!  /usr/bin/env  python3

import numpy as np
import random as rd
import copy

blood_dict = {1:'A', 2:'B', 3:'AB', 4:'O'}
hla_dict = {1:'DR-1',2:'DR-2',3:'A-1',4:'A-2',5:'B-1',6:'B-2'}

class Person:
    def __init__(self,index):
        self.index = index
        self.blood = blood_dict[rd.randint(1,4)]
        self.hla = [ hla_dict[rd.randint(1,2)], hla_dict[rd.randint(3,4)], hla_dict[rd.randint(5,6)] ]

class Node:
    def __init__(self,index):
        self.index = index
        self.Patient = Person(index)
        self.Donate = Person(index)
    def display(self):
        print("Node Index:%d\n"%self.index)
        print("Patient %d: blood--%s, HLA--%s %s %s\n"%(self.index,self.Patient.blood,self.Patient.hla[0],self.Patient.hla[1],self.Patient.hla[2]))
        print("Donate %d: blood--%s, HLA--%s %s %s\n"%(self.index,self.Donate.blood,self.Donate.hla[0],self.Donate.hla[1],self.Donate.hla[2]))
        print("\n")

# Person1:Patient  Person2: Donate  1:Matched 0: Unmatched
def Match(Person1,Person2):
    hla_point = 0
    hla_flag = 0
    for i in range(3):
        if Person1.hla[i] == Person2.hla[i]:
            hla_point += 1
    if hla_point >= 2:
        hla_flag = 1
    blood_flag = 0
    if Person1.blood == Person2.blood  or Person2.blood == 'O'  or Person1.blood == 'AB':
        blood_flag = 1
    if blood_flag == 1 and hla_flag== 1:
        return 1
    else:
        return 0


if __name__ == "__main__":
    ##  Code for generate data
    data = []
    num = 0
    size = 500
    for i in range(500):
        node = Node(i)
        if( Match(node.Patient, node.Donate) == 0) and num < size:
            num += 1
            data.append(node)
    print(len(data))
    for i in range(size):
        data[i].display()
    
    filename = 'database.txt'

    try:
        with open(filename,'w') as file_obj:
            for i in range(size):
                file_obj.write('%d %s %s %s %s \n'%(data[i].index,data[i].Patient.blood,data[i].Patient.hla[0],data[i].Patient.hla[1],data[i].Patient.hla[2]))
                file_obj.write('%d %s %s %s %s \n'%(data[i].index,data[i].Donate.blood,data[i].Donate.hla[0],data[i].Donate.hla[1],data[i].Donate.hla[2]))
    except FileNotFoundError:
        msg = filename + "does not exist.\n"
        print(msg)

    ## If you use code above , size and filename here should be deleted
    #size = 2000
    #filename = 'database.txt'

    ## load the data from txt
    array = []
    try:
        with open(filename,'r') as file_obj:
            for i in range(size):
                line_str = file_obj.readline()
                content = line_str.split()
                node = Node(int(content[0]))
                node.Patient.blood = content[1]
                node.Patient.hla = copy.deepcopy([ content[2],content[3],content[4] ])
                line_str = file_obj.readline()
                content = line_str.split()
                node.Donate.blood = content[1]
                node.Donate.hla = copy.deepcopy([ content[2],content[3],content[4] ])
                array.append(node)
    except FileNotFoundError:
        msg = filename + "does not exist.\n"
        print(msg)
    
    for i in range(size):
        array[i].display()



