a= input('хотите начать нажмите entr')
print('Сколько будет 6•3')
a=input('=')
if a =='18':
    print('ты молодец это правельный ответ')
    c=1
else : 
    a=input('Неправильный ответ')
    c=0
a=input('нажмите entr чтобы продолжить')
print('Сколько будет:8•9 ')
a=input('=')
if a =='72': 
    print('Молодец правильно')
    c=1+c
else: 
    print('Неправильно')
    c=0+c 
print('Сколько будет 5•3')
a=input('=')
if a =='15':
    print('ты молодец это правельный ответ')
    c=1+ c
else : 
    a=input('Неправильный ответ')
    c=0 + c
a=input('нажмите entr чтобы продолжить')
print('Сколько будет:9•0 ')
a=input('=')
if a =='0': 
    print('Молодец правильно')
    c=1+c
else: 
    print('Неправильно')
    c=0+c 
a=input('нажмите entr чтобы продолжить')
print('Сколько будет:18:6')
a=input('=')
if a =='3': 
    print('Молодец правильно')
    c=1+c
else: 
    print('Неправильно')
    c=0+c 
g=input('произвести под счет да/нет: ')
if g =='да':
	if c  < 5 :  
		print ('надо под учить '+str(c)+'/2')
	if c < 4 :
		print ('двоешница '+str(c)+ '/2 ')
	if c == 5 :
		print(' отлично 5/5 ')
else: 
    print('хорошо') 

print('спасибо за то что играли в эту игру')
a=input('нажмите entr чтобы закончить')
