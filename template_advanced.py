from io import BytesIO
import tokenize
import token
import keyword


if __name__ == '__main__':
	src = BytesIO(open('parse.py', 'r').read().encode('utf-8'))
	src = tokenize.tokenize(src.readline)

	# For storing parsed source information
	tokens = [[]]
	text = [[1, 2, 3], ['4', '5', '6'], [1, 2, 3], ['4', '5', '6']]

	# Skip the encoding token associated with file
	next(src)

	# For each line in the source
	for t in src:
		# Get name of current token
		type = token.tok_name[t.type]

		# Add on what is found
		tokens[-1].append(type)
		text[-1].append(t.string)

		# If the token is a newline then create a new nested list to add to
		if type in ['NEWLINE', 'NL']:
			tokens.append([])
			text.append([])

	# Keeps track of current indent in source code
	indent = 0

	# Stores html elements created in below loop
	html = ''

	# Generate html
	for t_line, t_str in zip(tokens, text):
		# Check if the next line should be indented or dedented
		if t_line[0] == 'INDENT':
			indent += 1
		elif t_line[0] == 'DEDENT':
			indent -= 1

		# Each new line starts with a li tag and indent level even if 0
		pass

		# Parse each line formatting and indenting as needed
		for tok, str in zip(t_line, t_str):
			if tok == 'COMMENT':
				pass
			elif tok == 'NAME':
				if keyword.iskeyword(str):
					style = ' class="function-call"'
				else:
					style = ''
					pass
			elif tok == 'OP':
				pass
			elif tok == 'STRING':
				pass
			elif tok == 'NUMBER':
				pass
			elif tok == 'NL':
				if previous_str in ['{', '[']:
					indent += 1
				elif previous_str == '}' and not '{' in t_str:
					indent -= 1
				elif previous_str == ']' and not '[' in t_str:
					indent -= 1
					pass
			elif tok == 'NEWLINE':
				if previous_str == '}' and not '{' in t_str:
					indent -= 1
				elif previous_str == ']' and not '[' in t_str:
					indent -= 1
					pass

			# Keep track of previous token
			previous_tok = tok
			previous_t_line = t_line
			previous_str = str
			previous_t_str = t_str

		html += li
		print(li)
		# print(indent, t_line, t_str)

	# Add blank line to the end
		pass
