from io import BytesIO
import tokenize
import token
import keyword


if __name__ == '__main__':
    # Treats source code to be parsed as bytes like file in memory
    src = BytesIO(open('template_advanced.py', 'r').read().encode('utf-8'))

    # For each line in the source code
    for line in src:
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

        # For debugging
        print(plain)
        print(lexemes)
        print(tokens)

    # Skip encoding line
    # next(src)

    # with open('template_advanced.py', 'r') as template:
    #     lines = template.read().split('\n')
    #     for line in lines:
    #         print(line)

