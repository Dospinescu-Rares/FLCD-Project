import re


class Scanner:
    def __init__(self, tokens_file_path):
        """
        Initializes a Scanner with a file path to the Token.in file and then reads the tokens this file
        This scanner is responsible for finding lexical errors in programs
        :param tokens_file_path: The file path of the Token.in file
        """
        self.tokens_file_path = tokens_file_path
        self.separators = []
        self.operators = []
        self.reserved_words = []
        self.read_tokens()

    def read_tokens(self):
        """
        Reads the tokens from the Token.in file and saves them in self.separators,
        self.operators and self.reserved_words
        :return: None
        """
        with open(self.tokens_file_path, 'r') as f:
            for line in f:
                if not line.strip():
                    break
                separator = line.strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
            for line in f:
                if not line.strip():
                    break
                self.operators.append(line.strip())
            for line in f:
                if not line.strip():
                    break
                self.reserved_words.append(line.strip())

    def check_lexical_errors(self, file_path, st, pif):
        """
        Checks for lexical errors in a given program and writes the Symbol Table and PIF in separate files
        :param file_path: The file path of the program being checked
        :param st: The file path to the Symbol Table output file
        :param pif: The file path of the PIF output file
        :return: The lexical errors, if any were found
        """
        lexical_errors = ""

        with open(file_path, 'r') as file:
            lineCounter = 0
            for line in file:
                lineCounter += 1
                for token in self.tokenize_function(line.strip()):
                    if token in self.reserved_words + self.separators + self.operators:
                        if token == ' ':
                            continue
                        pif.add(token, st.contains(token))
                    elif self.check_if_identifier(token) or self.check_if_constant(token) or self.check_if_string(token):
                        identifier = st.add(token)
                        pif.add(token, identifier)
                    else:
                        lexical_errors += 'Lexical error at token ' + token + ', at line ' + str(lineCounter) + "\n"
        return lexical_errors

    def tokenize_function(self, line):
        """
        Finds tokens in a given line
        :param line: The line we need to look for tokens in
        :return: A list of tokens found in a given line
        """
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_part_of_operator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.get_operator_token(line, index)
                tokens.append(token)
                token = ''
            elif line[index] == '\"':
                if token:
                    tokens.append(token)
                token, index = self.get_string_token(line, index)
                tokens.append(token)
                token = ''
            elif line[index] in self.separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def is_part_of_operator(self, char):
        """
        Looks to see if a character is part of an operator
        :param char: The char we are checking
        :return: True if the character is part of an operator, False otherwise
        """
        for op in self.operators:
            if char in op:
                return True
        return False

    def get_operator_token(self, line, index):
        """
        Finds an operator token after being given a line and an index
        :param line: The line where we need to search
        :param index: The index where we need to search
        :return: The token and the index where we found it
        """
        token = ''
        while index < len(line) and self.is_part_of_operator(line[index]):
            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def check_if_identifier(token):
        """
        Checks if a token is an identifier using a regex
        :param token: The token we are checking
        :return: True if the token is an identifier, False otherwise
        """
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){,7}', token) is not None

    @staticmethod
    def check_if_constant(token):
        """
        Checks if a token is a constant
        :param token: The token we are checking
        :return: True if the token is a constant, False otherwise
        """
        return re.match(r'^(0|[+\-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    @staticmethod
    def get_string_token(line, index):
        """
        Finds the full string token
        :param line: The line where we are searching
        :param index: The index where we are searching
        :return: The full string token found at the given line and index
        """
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\"':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def check_if_string(token):
        """
        Checks if a token is a string
        :param token: The token we are checking
        :return: True if the token is a string, False otherwise
        """
        return re.match(r'^".*"$', token) is not None
