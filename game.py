import numpy as np

number=np.random.randint(1,101)#загадываем число

#rколичество попыток 

count=0

while True:
    
    predict=int(input('Угадай число от1 до 100:')) 
    
    if predict>number:
        print('Число должно быть меньше')
    
    elif predict<number: 
        print('Число должно быть больше')
    else:
        print(f'Вы угадали число={number} за {count} попыток')
        
        break