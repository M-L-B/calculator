#還原字串h3e5=hhheeeee
y=0
string=str(input('你想要輸入的字串'))
string_len=len(string)
for x in range (1,string_len+1,2):
    for z in range (int(string[x])):
        print(string[y])    
    y=x+1