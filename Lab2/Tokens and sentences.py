signs = {'.', ',', ';', '!', '?', ':', '/', '-', '\"'}

def tokens_txt():
    with open('nkjp.txt', 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                if word[-1] in signs:
                    yield word[-1]
                    continue
                yield word


def sentences_txt():
    with open('nkjp.txt', 'r', encoding='utf-8') as file:
        sentence = ''
        flag = False

        for sign in file.read():
            if flag:
                if sign.isupper():
                    yield sentence.strip()
                    sentence = ''

                elif not sign.isspace():
                    flag = False
                sentence = sentence + sign

            else:
                sentence = sentence + sign
                if sign == '.':
                    flag = True
        yield sentence


def tokens_conll():
    with open('nkjp.conll', 'r', encoding='utf-8') as file:
        for line in file:
            yield line.split()[0][1:-1]


def sentences_conll():
    with open('nkjp.conll', 'r', encoding='utf-8') as file:
        sentence = ''
        flag = False

        for line in file:
            line, type = line.split()[0][1:-1], line.split()[2]

            if type == 'Interp':
                flag = False

            if flag:
                sentence = sentence + ' '
            sentence = sentence + line
            flag = True

            if line == '.':
                yield sentence
                sentence = ''
                flag = False

