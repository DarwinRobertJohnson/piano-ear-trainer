import os
from playsound import playsound
from random import randint


notes=os.listdir("oct4/")
notes.sort()
lookfor='C'
score=0
count=0

notes_dict={1:'C',2:'D',3:'E',4:'F',5:'G',6:'A',7:'B'}

def checkNote(note_num):
    
    if notes_dict[note_num+1] ==lookfor:
        print("Yes it is right")
        return True

while True:

    note_num=randint(0,6)
    playsound("oct4/"+notes[note_num])
    my_answer=input("Was it "+lookfor+":")
    
    if notes_dict[note_num+1]==lookfor:
        count+=1

    if my_answer=='yes':
        res=checkNote(note_num)
        if res:
            score+=1

    elif my_answer=="exit":
        break
    print(notes_dict[note_num+1])


print(str(score)+"/"+str(count))
