import random

ch='y'

while ch=='y':
    uc=input('Enter r for rock, p for paper and s for scissors:\n')
    cc=random.choice(['r','p','s'])

    if uc=='r' and cc=='s' or uc=='s' and cc=='p' or uc=='p' and cc=='r':
        
        print(f'User Wins! System choice:{cc}\n')
        
    elif cc==uc:
        print(f'it is a tie! System choice:{cc}\n')
    
    elif cc=='r' and uc=='s' or cc=='s' and uc=='p' or cc=='p' and uc=='r':
        
        print(f'System Wins! System choice:{cc}\n')
        
    else:
        print('Wrong input\n')
    
