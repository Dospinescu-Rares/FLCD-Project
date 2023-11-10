class ProgramInternalForm:
    def __init__(self):
        """
        Initializes the ProgramInternalForm with an empty list
        """
        self.__pif = []

    def add(self, token, internal_form):
        """
        Adds a (token, internal_form) pair to the list
        :param token: The token being added to the list
        :param internal_form: The token's internal form
        :return: None
        """
        self.__pif.append((token, internal_form))

    def __str__(self):
        """
        :return: Returns the ProgramInternalForm as a string
        """
        result = ""
        for pair in self.__pif:
            result += f"Token '{pair[0]}': {str(pair[1])}\n"
        return result
