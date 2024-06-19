class MyIter():
    def __init__(self, string: str) :
        self.string = string
        self.index = 0
        self.length = len(string)

    def peek(self) -> str:
        return self.string[self.index]
    
    def next(self) -> str:
        if self.index >= self.length: raise IndexError
        c = self.string[self.index]
        self.index += 1
        return c
    
    def is_end(self) -> bool:
        return self.index >= self.lengh
    
class MyParser():
    # TODO: replace while True -> while not it.is_end()

    def parse_str(self, it: MyIter):
        name = ""
        it.next()
        while not it.is_end():
            c = it.next()
            if c == "\"":
                return name
            name += c

    def parse_list(self, it: MyIter):
        l = []
        it.next()
        
        while not it.is_end():
            c = it.peek()

            if c == ']':
                it.next()
                return l
            elif c in '-ntr[{\"' or c.isdigit():
                item = self.parse_item(it)
                l.append(item)
            else:
                it.next()

    def parse_obj(self, it: MyIter):
        obj = {}
        while not it.is_end():
            c = it.peek()

            if c == '}':
                it.next()
                return obj
            elif c == "\"":
                pair = self.parse_pair(it)
                obj.update(pair)
            else:
                it.next()

    def parse_bool(self, it: MyIter):
        if it.next() == 'f':
            for _ in range(4):
                it.next()
            return False
        else:
            for _ in range(3):
                it.next()
            return True
        
    def parse_item(self, it: MyIter):
        while not it.is_end():
            c = it.peek()

            if c == '[':
                item = self.parse_list(it)
                return item
            elif c == '{':
                item = self.parse_obj(it)
                return item
            elif c == "\"":
                item = self.parse_str(it)
                return item
            elif c.isdigit() or c == '-':
                item = self.parse_number(it)
                return item
            elif c in 'tf':
                item = self.parse_bool(it)
                return item
            elif c in 'n':
                for _ in range(3):
                    it.next()
                return None
            else:
                it.next()
            
    def parse_pair(self, it: MyIter):
        while it.peek() != "\"":
            it.next()
        key = self.parse_str(it)
        var = self.parse_item(it)
        return {key: var}


    def parse_number(self, it: MyIter):
        c: str
        while not it.is_end():
            c = it.peek()
            if c.isdigit() or c in '-+.e':
                break
            it.next()

        num = ''
        while not it.is_end():
            if c.isdigit() or c in '-+.e':
                num += it.next()
            else:
                return float(num)
            c = it.peek()
            
    def parse_file(self, path: str):
        text: str
        with open(path) as f:
            text = f.read()
        it = MyIter(text)

        return self.parse_obj(it)
        
