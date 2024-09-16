# Generated from ./src/parser/SQL.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,27,178,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,4,8,79,8,8,11,8,12,8,80,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,4,23,148,
        8,23,11,23,12,23,149,1,23,5,23,153,8,23,10,23,12,23,156,9,23,1,24,
        4,24,159,8,24,11,24,12,24,160,1,25,1,25,5,25,165,8,25,10,25,12,25,
        168,9,25,1,25,1,25,1,26,4,26,173,8,26,11,26,12,26,174,1,26,1,26,
        1,166,0,27,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,1,0,3,3,0,65,90,95,95,97,122,1,0,48,57,
        3,0,9,10,13,13,32,32,183,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,
        1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,
        1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,1,55,1,0,0,0,3,57,
        1,0,0,0,5,59,1,0,0,0,7,61,1,0,0,0,9,64,1,0,0,0,11,66,1,0,0,0,13,
        68,1,0,0,0,15,71,1,0,0,0,17,74,1,0,0,0,19,82,1,0,0,0,21,89,1,0,0,
        0,23,94,1,0,0,0,25,100,1,0,0,0,27,104,1,0,0,0,29,107,1,0,0,0,31,
        109,1,0,0,0,33,116,1,0,0,0,35,123,1,0,0,0,37,128,1,0,0,0,39,135,
        1,0,0,0,41,140,1,0,0,0,43,142,1,0,0,0,45,144,1,0,0,0,47,147,1,0,
        0,0,49,158,1,0,0,0,51,162,1,0,0,0,53,172,1,0,0,0,55,56,5,42,0,0,
        56,2,1,0,0,0,57,58,5,44,0,0,58,4,1,0,0,0,59,60,5,61,0,0,60,6,1,0,
        0,0,61,62,5,60,0,0,62,63,5,62,0,0,63,8,1,0,0,0,64,65,5,60,0,0,65,
        10,1,0,0,0,66,67,5,62,0,0,67,12,1,0,0,0,68,69,5,60,0,0,69,70,5,61,
        0,0,70,14,1,0,0,0,71,72,5,62,0,0,72,73,5,61,0,0,73,16,1,0,0,0,74,
        78,3,47,23,0,75,76,3,41,20,0,76,77,3,47,23,0,77,79,1,0,0,0,78,75,
        1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,18,1,0,0,0,
        82,83,5,115,0,0,83,84,5,101,0,0,84,85,5,108,0,0,85,86,5,101,0,0,
        86,87,5,99,0,0,87,88,5,116,0,0,88,20,1,0,0,0,89,90,5,102,0,0,90,
        91,5,114,0,0,91,92,5,111,0,0,92,93,5,109,0,0,93,22,1,0,0,0,94,95,
        5,119,0,0,95,96,5,104,0,0,96,97,5,101,0,0,97,98,5,114,0,0,98,99,
        5,101,0,0,99,24,1,0,0,0,100,101,5,97,0,0,101,102,5,110,0,0,102,103,
        5,100,0,0,103,26,1,0,0,0,104,105,5,111,0,0,105,106,5,114,0,0,106,
        28,1,0,0,0,107,108,5,59,0,0,108,30,1,0,0,0,109,110,5,100,0,0,110,
        111,5,101,0,0,111,112,5,108,0,0,112,113,5,101,0,0,113,114,5,116,
        0,0,114,115,5,101,0,0,115,32,1,0,0,0,116,117,5,105,0,0,117,118,5,
        110,0,0,118,119,5,115,0,0,119,120,5,101,0,0,120,121,5,114,0,0,121,
        122,5,116,0,0,122,34,1,0,0,0,123,124,5,105,0,0,124,125,5,110,0,0,
        125,126,5,116,0,0,126,127,5,111,0,0,127,36,1,0,0,0,128,129,5,118,
        0,0,129,130,5,97,0,0,130,131,5,108,0,0,131,132,5,117,0,0,132,133,
        5,101,0,0,133,134,5,115,0,0,134,38,1,0,0,0,135,136,5,110,0,0,136,
        137,5,117,0,0,137,138,5,108,0,0,138,139,5,108,0,0,139,40,1,0,0,0,
        140,141,5,46,0,0,141,42,1,0,0,0,142,143,5,40,0,0,143,44,1,0,0,0,
        144,145,5,41,0,0,145,46,1,0,0,0,146,148,7,0,0,0,147,146,1,0,0,0,
        148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,154,1,0,0,0,
        151,153,7,1,0,0,152,151,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,
        154,155,1,0,0,0,155,48,1,0,0,0,156,154,1,0,0,0,157,159,7,1,0,0,158,
        157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,
        50,1,0,0,0,162,166,5,39,0,0,163,165,9,0,0,0,164,163,1,0,0,0,165,
        168,1,0,0,0,166,167,1,0,0,0,166,164,1,0,0,0,167,169,1,0,0,0,168,
        166,1,0,0,0,169,170,5,39,0,0,170,52,1,0,0,0,171,173,7,2,0,0,172,
        171,1,0,0,0,173,174,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,
        176,1,0,0,0,176,177,6,26,0,0,177,54,1,0,0,0,7,0,80,149,154,160,166,
        174,1,6,0,0
    ]

class SQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    TCNAME = 9
    SELECT = 10
    FROM = 11
    WHERE = 12
    AND = 13
    OR = 14
    SEMICOLON = 15
    DELETE = 16
    INSERT = 17
    INTO = 18
    VALUES = 19
    NULL = 20
    DOT = 21
    OPENPAR = 22
    CLOSEPAR = 23
    WORD = 24
    NUMBER = 25
    STRING = 26
    WS = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "','", "'='", "'<>'", "'<'", "'>'", "'<='", "'>='", "'select'", 
            "'from'", "'where'", "'and'", "'or'", "';'", "'delete'", "'insert'", 
            "'into'", "'values'", "'null'", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "TCNAME", "SELECT", "FROM", "WHERE", "AND", "OR", "SEMICOLON", 
            "DELETE", "INSERT", "INTO", "VALUES", "NULL", "DOT", "OPENPAR", 
            "CLOSEPAR", "WORD", "NUMBER", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "TCNAME", "SELECT", "FROM", "WHERE", "AND", "OR", 
                  "SEMICOLON", "DELETE", "INSERT", "INTO", "VALUES", "NULL", 
                  "DOT", "OPENPAR", "CLOSEPAR", "WORD", "NUMBER", "STRING", 
                  "WS" ]

    grammarFileName = "SQL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


