import antlr4
from antlr4 import *
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from SQLLexer import SQLLexer
from SQLParser import SQLParser
from SQLListener import SQLListener
from SQLVisitor import SQLVisitor


class SQLAnnotate:

    def __init__(self, **kwargs):
        self.lexer = None
        self.input = None
        self.stream = None
        self.parser = None
        self.tree = None
        self.schema = None
        self.visitor = None
        self.inputStream = None
        self.error = None
        self.data = None
        self.debug = False

        self.errorList = [
            "0000:SQL NOT FOUND",
            "0001:SCHEMA NOT DEFINED",
            "0002: SYNTAX ERROR"
        ]

        # detect sql query
        if 'sql' in kwargs: 
            self.input = kwargs['sql']
        else:
            self.error = self.errorList[0]
        
        # ensure that schema is loaded
        if 'schema' in kwargs: 
            self.schema = kwargs['schema']
        else:
            self.error = self.errorList[1]
    
    def setDebug (self, debug = False):
        self.debug = debug
        return self

    def loadSchema (self, schema):
        self.schema = schema
        return self
    
    def annotate (self):

        if not self.input == None:
            self.lexer = SQLLexer(self.input)
            self.stream = CommonTokenStream(self.lexer)
            self.parser = SQLParser(self.stream)
            self.tree = self.parser.sql_statement()

            if self.parser.getNumberOfSyntaxErrors() > 0:
                self.error = self.errorList[2]
            else:
                # walk to parse tree and generate annnotations
                self.visitor = SQLVisitor()
                self.visitor.loadSchema (self.schema)
                self.data = self.visitor.setDebug(self.debug).visit(self.tree)
        
        return self
    
    def getAnnotations (self):
        return {
            'error': self.error,
            'data': self.data
        }
