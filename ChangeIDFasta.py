"""
This program will change the Id Name of each fasta file to the 

>Repeatname#class/Subclass format

ex. 
>AluS#SINE/Marmoset 
"""
from Bio import SeqIO
import re 

RepeatName=re.compile('Alu(\w+)')
RMLibFile=open("C:\\Users\\jbro262\\Desktop\\DuplicatesRemoved\\SquirrelMonkeyAluRMFormat.fas","a")

for record in SeqIO.parse("C:\\Users\\jbro262\\Desktop\\DuplicatesRemoved\\SquirrelMonkeyAlu.fas","fasta"):
    a=RepeatName.findall(record.id)
    RMLibFile.write(">"+"Alu"+a[0]+"#"+"SINE"+"/SquirrelMonkey"+'\n'+str(record.seq)+'\n')        
    
RMLibFile.close()
print("Done!!!")
