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

class Rule(object) :
    '''A class representing rule for lexical analysis.

    Each rule must have the following :
        * A regular expression pattern which represents the rule.
        * The token type given to all lexemes which match the pattern.

    Additionally, a rule may also specify a callback function to be called when
    the rule matches. This function is given the token's type, and the text that
    matched.

    Currently, the default callback is the constructor of the Token class, which
    simply creates a token with the given attributes and returns it.

    A callback of None can be used as a placeholder for a rule which is to
    discard its token.
    '''

    def __init__(self, token_type, pattern, callback = Token) :
        self.type = token_type
        self.pattern = re.compile(pattern)
        self.callback = callback

    def __repr__(self) :
        return '<Rule type = {0}, pattern = {1}, callback = {2}'.format(
            self.type, self.pattern, self.callback
        )
