def about_me(name='Brandon Sims'):
	return {
		'name': 'Brandon Sims',
		'age': 24,
		'education': 'B.S. in Computer Science from AState',
		'languages': [
			'C++',
			'Python',
			'Javascript'
		]
	}

if __name__ == '__main__':
	print(about_me())