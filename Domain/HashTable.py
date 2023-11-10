from collections import deque


class HashTable:
    def __init__(self, size):
        """
        Initializes a HashTable with a given size
        :param size: The size of the HashTable
        """
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    def hash(self, key):
        """
        Returns the hash of a given key
        :param key: The key whose hash we are looking for
        :return: The hash of the key
        """
        result = 0
        for character in key:
            result += ord(character) - ord('0')
        return result % self.__size

    def add(self, key):
        """
        Adds a key to the HashTable
        :param key: The key being added to the HashTable
        :return: The position in which the key was inserted
        """
        if self.contains(key):
            return self.get_position(key)
        self.__items[self.hash(key)].append(key)
        return self.get_position(key)

    def remove(self, key):
        """
        Removes a key from the HashTable
        :param key: The key being removed from the HashTable
        :return: None
        """
        self.__items[self.hash(key)].remove(key)

    def contains(self, key):
        """
        Searches for the key in the HashTable
        :param key: The key we are searching for
        :return: True if the key is part of the HashTable, False otherwise
        """
        return key in self.__items[self.hash(key)]

    def get_position(self, key):
        """
        Finds the position of a key in the HashTable
        :param key: The key we are searching for
        :return: The position and the index of the deque where the key is located
        """
        listPosition = self.hash(key)
        listIndex = 0
        for item in self.__items[listPosition]:
            if item != key:
                listIndex += 1
            else:
                break
        return listPosition, listIndex

    def __str__(self):
        """
        :return: Returns the HashTable as a string
        """
        result = ""
        for i in range(self.__size):
            result = result + str(i) + "->" + str(self.__items[i]) + "\n"
        return result
