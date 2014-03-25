import re
#variable declaration
wordsinmessage=[]
inp=0
data=[]
testwords=[]
str1=""
z=0
flag=0
words=[]
hammess=0
spammess=0
hamwords=0
spamwords=0
ham=0
spam=0
tlen=0
t2=0
temp=[]
wordtype=[]
count=0
messagetype=[]
message=[]
messagewords=[]
temp2=[]
if(1):
    datafile=open("test2.txt",'r')
    for row in datafile:
        data.append(row.strip().lower().split())
    length=len(data)
    datafile.close()
    # seperating message and its type from data
    for i in range (0,length):
        messagetype.append(data[i][0].strip())
        messagelen=len(data[i])
        message.append(" ".join(data[i][1:messagelen]))
    templen=len(message)
    
    # counting number of words, ham words, spam words
    for j in range (0,templen):
        temp=message[j].strip(",").split()
        if (messagetype[j]=="ham"):
            hammess+=1
        if (messagetype[j]=="spam"):
            spammess+=1    
        if (messagetype[j]=="ham"):
            hamwords+=len(temp)
        if (messagetype[j]=="spam"):
            spamwords+=len(temp)



def train():
    outputfile=open("output.txt",'w')
    for i in range (0,templen):
        temp=message[i].split()
        t2=len(temp)
        for j in range (0,t2):
            temp[j]= re.sub('[!^@^#^$^.^-^,^;^-]', '', temp[j])
            count+=message[i].count(temp[j])
            if((message[i].count(temp[j]))>0):
                if(messagetype[i]=="ham"):
                    ham+=(message[i].count(temp[j]))
                if(messagetype[i]=="spam"):
                    spam+=(message[i].count(temp[j]))
            for k in range ((i+1),templen):
                count+=message[k].count(temp[j])
                if((message[k].count(temp[j]))>0):
                    if(messagetype[k]=="ham"):
                        ham+=(message[k].count(temp[j]))
                    if(messagetype[k]=="spam"):
                        spam+=(message[k].count(temp[j]))
            for y in range(0,z):
                if(words[y]==str(temp[j])):
                    flag=1
                    break
            if(flag==0):
                str1=(str(temp[j])+"-"+str(count)+"-"+str(ham)+"-"+str(spam)+"\n")
                words.append(str(temp[j]).strip())
                outputfile.write(str1)
                z+=1
            ham=0
            spam=0
            flag=0
            count=0
    outputfile.close()

def add():
    teststr=[]
    datawrite=open("test2.txt",'a')
    str2=""
    str2=input()
    datawrite.write(str2+"\n")
    datawrite.close()
    strinp=[]
    strinp=str2.split()
    strinplen=len(strinp)
    dataread=open("test2.txt",'a')
    for z in dataread:
        teststr=z.split("-")
        for x in range(1,strinplen):
            if(teststr[0]==strinp[x]):
                if(strinp[0]=="ham"):
                    teststr[2]=str(int(teststr[2])+1)
                if(strinp[0]=="spam"):
                    teststr[2]=str(int(teststr[2])+1)
    data.close()

def test():
    totalpr=0.0
    wordpr=0.0
    hampr=0.0
    spampr=0.0
    t2=""
    dataf=open("output.txt",'r')
    teststr=""
    teststr=input()
    testwords=teststr.strip().split()
    tlen=len(testwords)
    for i in range (0,tlen):
        testwords[i]=re.sub('[!^@^#^$^.^-^,^;^-]', '', testwords[i])
        for t2 in dataf:
            temp=t2.split("-")
            if(temp[0]==testwords[i]):
                s1=int(temp[1])
                s2=int(temp[2])
                s3=int(temp[3])
                s4=(s2/s1)/((s2/s1)+(s3/s1))
                s5=(s3/s1)/((s3/s1)+(s2/s1))
                hampr+=s4
                spampr+=s5
    if(hampr>spampr):
        print("HAM MESSAGE")
    if(spampr>hampr):
        print("SPAM MESSAGE")
    dataf.close()
print("\n1.Training of Data\n2. Insert any Messages to our Database\n3. Test any Message\n press 0 to Quit\n")
print("Enter your choice:")
inp=int(input())
if(inp==1):
    train()
if(inp==2):
    add()
else:
    test()