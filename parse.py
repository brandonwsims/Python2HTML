from io import BytesIO
import tokenize
import token
import keyword


if __name__ == '__main__':
    # Treats source code to be parsed as bytes like file in memory
    src = BytesIO(open('template_advanced.py', 'r').read().encode('utf-8'))

    # String for storing the html to be generated for parsing the source
    html = ''

    # For each line in the source code
    for line in src:
        # Start off by opening a li tag for the html generation
        li = '<li>\n\t'

        # Store line as plain text
        plain = line.decode('utf-8').replace('\n', '')

        # Strip lexemes from line
        tokens = tokenize.tokenize(BytesIO(line).readline)
        lexemes = [t.string for t in tokens]
        lexemes = lexemes[1:-1]

        # Strip tokens from line
        tokens = tokenize.tokenize(BytesIO(line).readline)
        tokens = [token.tok_name[t.type] for t in tokens]
        tokens = tokens[1:-1]

        first = True
        for lex, tok in zip(lexemes, tokens):
            if first:
                first = False
                indent = lex.count('\t')
                li += '<span class="indent-level-{}"></span>'.format(indent)

            if keyword.iskeyword(lex):
                style = 'class="function-call"'
            elif tok == 'NUMBER':
                style = 'class="literal"'
            elif tok == 'STRING':
                style = 'class="string"'
            elif tok == 'OP':
                style = 'class="keyword"'
            else:
                style = 'class=""'

            if tok not in ['NEWLINE', 'NL', 'DEDENT', 'INDENT']:
                li += '<span {}>{} </span>'.format(style, lex)

        # Close li tag
        li += '\n</li>'

        # Append to html
        html += li

        # For debugging
        # print(plain)
        # print(lexemes)
        # print(tokens)
        print(li)

    # Skip encoding line
    # next(src)

    # with open('template_advanced.py', 'r') as template:
    #     lines = template.read().split('\n')
    #     for line in lines:
    #         print(line)

