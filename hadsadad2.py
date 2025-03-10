import random as rnd
user_input=int(input('adad mored nazar khod ra bein 1 ta 100 vsred konid\n'))
low=1
high=100

print('pc shoro mikonad be hads zadan')

while True:
    pc_guess=rnd.randint(low,high)
    print(f'computer hads ra mizare: {pc_guess}')
    user = input('Agar adade computer kamtar ast vared konid "k", agar bishtar ast vared konid "b", va agar dorost ast vared konid "d": ')
    
    if user=='b':
        low=pc_guess+1
    elif user=='k':
        high=pc_guess-1
    elif user=='d':
        print(f"Computer dorost hads zade! Adad: {pc_guess}")
        break
    else:
        print('Faghat b , k , d ra vared konid.')