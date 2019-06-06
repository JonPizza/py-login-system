from random import randint
from sha import sha512 # TODO: Create sha

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
invalid_creds = False

username = input('Username: ')
user_pass = input('Password: ')

with open('users.txt', 'r') as users:
  #Make sure no one has used the username before
  if username in read(users).split('\n'):
    invalid_creds = True
    
if not invalid_creds:
  print('Creating Account...')
  salt = [chars[randint(0, len(chars)] for x in range(8)] 
  
  with open('users.txt', 'a') as users:
   users.append(username + '$' + sha512(user_pass + salt) + '$' + salt)
  
  
  print(f'Done. Time Elapsed: {__time__}')
else:
  print('Someone has alredy taken that username.')
