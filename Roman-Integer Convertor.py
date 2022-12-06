print('''Roman number to integer converter

''')
while True:
    user=input('Enter roman number: ').upper()
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i=0
    num=0
    while i<len(user):
        if i+1<len(user) and user[i:i+2] in roman:
            num+=roman[user[i:i+2]]
            i+=2
        else:
            num+=roman[user[i]]
            i+=1
    print(num)
    ans=input('DO YOU WANT TO PLAY AGAIN???(Y/N): ').lower()
    if ans=='y':
        continue
    else:
        break
