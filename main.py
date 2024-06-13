from Parser import *
if __name__ == '__main__':
    parser = Parser()
    d = parser.parse_file('test.json')
    print(d)
