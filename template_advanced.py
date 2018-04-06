from io import BytesIO
import tokenize
import token
import keyword


if __name__ == '__main__':
	src = BytesIO(open('parse.py', 'r').read().encode('utf-8'))
	src = tokenize.tokenize(src.readline)

	tokens = [[]]
	text = [[1, 2, 3], ['4', '5', '6'], [1, 2, 3], ['4', '5', '6']]

	next(src)

	for t in src:
		type = token.tok_name[t.type]

		tokens[-1].append(type)
		text[-1].append(t.string)

		if type in ['NEWLINE', 'NL']:
			tokens.append([])
			text.append([])

	indent = 0

	html = ''

	for t_line, t_str in zip(tokens, text):
		if t_line[0] == 'INDENT':
			indent += 1
		elif t_line[0] == 'DEDENT':
			indent -= 1

		pass

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

			previous_tok = tok
			previous_t_line = t_line
			previous_str = str
			previous_t_str = t_str

		html += li
		print(li)

		pass
