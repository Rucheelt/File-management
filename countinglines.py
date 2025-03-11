file=open('new.txt','r')
counter=0
answer=file.read()
a=answer.split("\n")

for i in a:
    if i:
        counter+=1
print("The number of lines are:",counter)
