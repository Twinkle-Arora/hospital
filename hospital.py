 Program Name : hos1.py
#hos1.py
import os
import pickle

#class defination for hospital
class Hospital:
    def __init__(self):
        self.pid=0
        self.pname=" "
        self.drname=" "
        self.indate=" "
        self.disease=" "
        self.pres=" "
        self.dtofdis=" "

#method to display data
    def display(self):
            print("Patient ID         : "+str(self.pid))
            print("Patient Name       : "+self.pname)
            print("Doctors Name       : "+self.drname)
            print("Admit Date         : "+self.indate)
            print("Diagnosed Disease  : "+self.disease)
            print("Presicription      : "+self.pres)
            print("Discharge Date     : "+self.dtofdis)
            print("\n\n")

#method for accepting data            
    def input(self):
            self.pid=input("Enter PID : ")
            self.pname=raw_input("Enter Name : ")
            self.drname=raw_input("Enter Doctor Name : ")
            self.indate=raw_input("Admit Date : ")
            self.disease=raw_input("Disease : ")
            self.pres=raw_input("Prescription : ")
            self.dtofdis=raw_input("Discharge Date : ")

def dataentry():
    print("\n\tEnter New Data for a Patient")
    f1=open("Patent.dat","ab")
    choice='y'
    while (choice=='y'):
        hobj.input()
        pickle.dump(hobj,f1)
        choice=raw_input("\n\tAdd more Patients? y/n : ")

    f1.close()

def displaydata():
    f2=open("Patent.dat","rb")
    try:
        while True:
            hobj=pickle.load(f2)
            hobj.display()
    except EOFError:
      f2.close()

def datadeletion():
    tpid=input("\n\tEnter Patient ID for deletion : ")
    f1=open("Patent.dat","rb")
    f2=open("temp.dat","wb")
    try:
        while True:
            hobj=pickle.load(f1)
            if(tpid!=hobj.pid):
                pickle.dump(hobj,f2)
    except EOFError:
            print(“Patient Deleted!!!!”)
            f1.close()
            f2.close()
            os.remove("Patent.dat")
            os.rename("temp.dat","Patent.dat")

def datamodification():
    tpid=input("\n\tEnter Patient ID for Modification : ")
    f1=open("Patent.dat","rb+")
    try:
        while True:
            k=f1.tell()
            hobj=pickle.load(f1)
            if (tpid==hobj.pid):
                print("Enter New Details")
                hobj.input()
                f1.seek(k)
                pickle.dump(hobj, f1)
    except EOFError:
            f1.close()


def searchpatient():
    tpid=input("\n\tEnter a Patient ID for Search : ")
    f1=open("Patent.dat","rb")
    try:
        while True:
            hobj=pickle.load(f1)
            if (tpid==hobj.pid):
                hobj.display()
    except EOFError:
            f1.close()
        
def printMenu():
    print("\t\t\t\tPATIENT INFORMATION SYSTEM")
    print("\t\t\t\t\tMain Menu")
    print("\t\t\t\t--------------------------")
    print("\t\t1. Add a New Patient")
    print("\t\t2. Display Patients Details ")
    print("\t\t3. Modify Patients Details ")
    print("\t\t4. Remove a Patients Details ")
    print("\t\t5. Search and Display a Patients Details ")
    print("\t\t6. EXIT")
    
hobj=Hospital()
#main method 
o=0
while (int(o)!=6):
    printMenu()
    o=input("\n\tEnter your Choice [1-6] : ")

    if (int(o)==1):
        dataentry()
    if (int(o)==2):
        displaydata()
    if (int(o)==3):
        datamodification()
    if (int(o)==4):
        datadeletion()
    if (int(o)==5):
        searchpatient()
    if (int(o)==6):
        print("\n\n\t\tThank You for using the system")
    
 
