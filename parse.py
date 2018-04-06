from io import BytesIO, StringIO
import tokenize
import token
import keyword


if __name__ == '__main__':
    # Treats source code to be parsed as file in memory
    src = BytesIO(open('template_advanced.py', 'r').read().encode('utf-8'))
    src_t = BytesIO(open('template_advanced.py', 'r').read().encode('utf-8'))

    # Generates iterable object containing parsed information from source
    tokenized = tokenize.tokenize(src_t.readline)

    # Skip encoding line that was generated during tokenize
    next(tokenized)

    # Store both the tokens of the file and the lexemes which the represent
    all_tokens = [[]]
    all_lexemes = [[]]

    # The parsed source doesn't go line by line, so format it as line by line
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

        # Add proper indentation to the line
        # indent = line.count('\t')
        indent = line.count('    ')
        li += '<span class="indent-level-{}"></span>'.format(indent)

        # For helping get the lookahead
        count = 0

        # Line by line
        for tok, lex in zip(tokens, lexemes):
            # Lookahead for formatting
            try:
                lookahead = [tokens[count+1], lexemes[count+1]]
            except:
                lookahead = [None, None]

            # Apply proper style depending in type of token
            if keyword.iskeyword(lex):
                style = 'class="function-call"'
            elif tok == 'NUMBER':
                style = 'class="literal"'
            elif tok == 'STRING':
                style = 'class="string"'
            elif tok == 'OP':
                style = 'class="keyword"'
            elif tok == 'COMMENT':
                style = 'class="comment"'
            else:
                style = 'class=""'

            # If we're not at EOL then add the lexeme
            if tok not in ['NEWLINE', 'NL', 'DEDENT', 'INDENT']:
                space = ''
                if keyword.iskeyword(lex) and lookahead[1] == '[':
                    space = ' '
                elif tok == 'NAME' and not lookahead[1] in ['(', ',', ')', '[',
                                                          ']', '.', ':']:
                    space = ' '
                elif lex in [':', ',', '=', '==', '+=', '+', '-=', '-']:
                    if lex == '-' and not (lookahead[0] in ['NUMBER', 'NAME',
                                                       'STRING'] and not prev[
                        0] in ['NUMBER', 'NAME', 'STRING']):
                        space = ' '
                    elif lex != '-':
                        space = ' '
                elif tok == 'OP':
                    if not lookahead[1] in [',', '.', ')',
                                            '(', ']', '[', '-']:
                        if lookahead[0] == 'OP' and lookahead[1] != ':':
                            space = ' '
                elif tok == 'STRING' and lookahead[0] == 'NAME' and (
                    not lookahead[1] == ':'):
                    space = ' '
                li += '<span {}>{}{}</span>'.format(style, lex, space)

            # For help in formatting keep the last set of tok and lex
            prev = [tok, lex]

            # Increment count for the next iteration
            count += 1

        # Close li tag
        li += '\n</li>'

        # Append to html
        html += li

        # For debugging
        # print(line)
        # print(lexemes)
        # print(tokens)
        # print()

    # Write the generated HTML to file once we're done
    with open('template.html', 'w') as template_file:
        template_file.write(html)
