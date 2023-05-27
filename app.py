
import os
from playsound import playsound
from random import randint


notes=os.listdir("oct4/")
notes.sort()
lookfor='C'

notes_dict={1:'C',2:'D',3:'E',4:'F',5:'G',6:'A',7:'B'}

while True:

    note_num=randint(0,6)
    playsound("oct4/"+notes[note_num])
    my_answer=input("Enter the note played:")
    
    if my_answer in [lookfor,lookfor.lower()]:
    #[notes_dict[note_num],notes_dict[note_num].lower()]:
        print("right answer and the answer is",notes_dict[note_num])
    elif my_answer=='r':
        playsound("oct4/"+notes[note_num])
    elif my_answer=='exit':
        break
    else:
        print("nice try,do better")
