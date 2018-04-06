from io import BytesIO, StringIO
import tokenize
import token
import keyword


if __name__ == '__main__':
    # Treats source code to be parsed as file in memory
    src = BytesIO(open('template_advanced.py', 'r').read().encode('utf-8'))
    src_t = BytesIO(open('template_advanced.py', 'r').read().encode('utf-8'))

    tokenized = tokenize.tokenize(src_t.readline)

    # Skip encoding line
    next(tokenized)

    all_tokens = [[]]
    all_lexemes = [[]]

    for t in tokenized:
        type = token.tok_name[t.type]
        all_tokens[-1].append(type)
        all_lexemes[-1].append(t.string)
        if type in ['NEWLINE', 'NL']:
            all_tokens.append([])
            all_lexemes.append([])


    # String for storing the html to be generated for parsing the source
    html = ''

    # For each line in the source code
    for line, tokens, lexemes in zip(src, all_tokens, all_lexemes):
        # Get plain text of source
        line = line.decode('utf-8')
        line = line.replace('\n', '')

        # Start off by opening a li tag for the html generation
        li = '<li>\n\t'

        first = True
        for tok, lex in zip(tokens, lexemes):
            if first:
                first = False
                indent = line.count('\t')
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
        # print(line)
        # print(lexemes)
        # print(tokens)
        # print()
        print(li)

    # Skip encoding line
    # next(src)

    # with open('template_advanced.py', 'r') as template:
    #     lines = template.read().split('\n')
    #     for line in lines:
    #         print(line)

