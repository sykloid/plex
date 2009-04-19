'''A simple lexical analysis framework written in python.'''

import re

class Token(object) :
    '''A class representing a lexical token.

    Each token must necessarily have a type and the lexeme.
    Other attributes can be used as required.
    '''

    def __init__(self, lexeme, token_type, **kwargs) :
        self.lexeme = lexeme
        self.type = token_type

    def __repr__(self) :
        return '<Token: type = "{0}", lexeme = "{1}">'.format(
            self.type,
            self.lexeme if len(self.lexeme) < 20 else self.lexeme[:17] + '...'
        )

    def __str__(self) :
        return self.lexeme
