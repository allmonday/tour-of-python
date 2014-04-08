class Word(str):
    def __noew__(cls, word):
        if ' ' in word:
            print 'truncating to first space'
            word = word[:word.index(' ')]
        return str.__new__(cls, word)
