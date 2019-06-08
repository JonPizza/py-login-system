from random import randint
import hashlib, time


start_time = time.time()

def sha512(data):
	return hashlib.sha512(data.encode('utf-8')).hexdigest()

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#%^&*()' # Everything that's not '$'
invalid_creds = False

username = input('Username: ')
user_pass = input('Password: ')
print('\n'*100)

with open('users.txt', 'r') as users:
	#Make sure no one has used the username before
	file_content = users.read().split('\n')
	usernames = []
	for i in file_content:
		usernames.append(i.split('$')[0])

	if username in usernames:
		invalid_creds = True
    
if not invalid_creds:
	print('Creating Account...')	
	salt = ''.join([chars[randint(0, len(chars)-1)] for x in range(8)]) #8 long rand chars 
  
	with open('users.txt', 'a') as users:
		users.write(username + '$' + sha512(user_pass + salt) + '$' + salt +'\n')

	print(f'Done. Time Elapsed: {time.time()-start_time}')
else:
	print('Someone has alredy taken that username.')
