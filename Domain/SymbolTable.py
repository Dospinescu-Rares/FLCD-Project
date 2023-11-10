from Domain.HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        """
        Initializes a SymbolTable which uses a HashTable
        :param size: The size of the SymbolTable
        """
        self.__hash_table = HashTable(size)

    def add(self, key):
        """
        Adds a key to the SymbolTable
        :param key: The key being inserted
        :return: The position in which the key was inserted
        """
        return self.__hash_table.add(key)

    def remove(self, key):
        """
        Removes a key from the SymbolTable
        :param key: The key being removed
        :return: None
        """
        self.__hash_table.remove(key)

    def contains(self, key):
        """
        Checks for the presence of a key in the SymbolTable
        :param key: The key we are searching for
        :return: The location of the key, -1 otherwise
        """
        return self.__hash_table.contains(key) or -1

    def get_position(self, key):
        """
        Searches for the key's position in the SymbolTable
        :param key: The key whose position we are searching for
        :return: The position of the key
        """
        return self.__hash_table.get_position(key)

    def __str__(self) -> str:
        """
        :return: The SymbolTable as a string
        """
        return str(self.__hash_table)
