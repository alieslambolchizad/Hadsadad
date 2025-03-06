import random as rnd
pc_choise = rnd.randint(1, 10)

person_choise = int(input('adad hadsi khod ra vared konid \n'))
while pc_choise != person_choise:
    if person_choise > pc_choise:
        person_choise = int(input('adad kamtar ra vared kon \n'))
    elif person_choise < pc_choise:
        person_choise = int(input('adad bozorgtar ra vared kon \n'))

print(f'afarin dorost hads zadi! adad ma {pc_choise} bod')


