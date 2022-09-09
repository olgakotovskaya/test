#from random import choice,randint,sample,shuffle,randrange
#a=[1,2,34,56,6,7,4,5,6]
#print(choice(a))
#print(randint(2,10))
#print(sample(a,4))




#a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
#q= a.append(13)
#print(a)
#c=0
#world= 13
#for i in a :
  #  if i==world:
 #       c+=1
#        print(c)
#print(len(a))
#print( a.count(13))
#print(13*27)
#print(351/10)
#p=36*13/100
#if p<70:
    #print('неужели')
    #if p>70:
    #    print('я так и знал')
#else :
 #   print('совпадение не думаю')
# dict={'a':3,'h':6,'i':12,'f':9}
# for i in dict:
#     if i in dict.keys():


#a ={'a':3,'h':6,'i':12,'f':9}
#for value in a.values():
 #   if value % 3 == 0:
  #      print('hi')
   # elif value % 5 == 0:
    #    print('bye')

city = ['Bishkek', 'Osh', 'Batken', 'NewYork']
commands = input('''Выберите действие:
1. Добавить 
2. Отобразить
3. Заменить город \n>>> ''').lower()
if commands == 'добавить':
    new_city = input('Введите название города: ')
    if new_city in city:
        print('Такой город уже есть')
    else:
        city.append(new_city)
elif commands == 'отобразить':
    print(city)
for new_city in city:
    new_city.extend(city)
    city.reverse()
    print(city)

