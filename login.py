
chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#%^&*()'
logged = False

def sha512(data):
	return hashlib.sha512(data.encode('utf-8')).hexdigest()

username = input('Username: ')
user_pass = input('Password: ')
print('\n'*100)

with open('users.txt', 'r') as users:
	for user in users.read().split('\n'):
		if user.split('$')[1] == sha512(user_pass + user.split('$')[2]):
			print('Sucessfully logged in.')
			ea = input('Would You Like To Edit Account Deets [Y/n]? ')
			if ea.lower() == 'y':
				print('Nah Maybe Later')
			elif ea.lower() != 'n':
				print('idk bro')
			else:
				print('Good Choice Kid.')
			break
