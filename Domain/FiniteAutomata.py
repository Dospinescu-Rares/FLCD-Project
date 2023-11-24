class FiniteAutomata:

    def __init__(self, fa_file_path):
        """
        Initializes empty variables in order to hold Finite Automata elements
        :param fa_file_path: The file path of the fa.in file
        """
        self.states = []
        self.alphabet = []
        self.initial_state = None
        self.final_states = []
        self.transitions = {}

        self.read_fa(fa_file_path)

    def read_fa(self, fa_file_path):
        """
        Reads and saves the elements of the Finite Automata
        :param fa_file_path: The file path of the fa.in file
        :return: None
        """
        with open(fa_file_path) as file:
            self.states = file.readline().strip().split(' ')[2:]
            self.alphabet = file.readline().strip().split(' ')[2:]
            self.initial_state = file.readline().strip().split(' ')[2:][0]
            self.final_states = file.readline().strip().split(' ')[2:]

            file.readline()
            for line in file:
                transition = line.strip().split(" ")

                if (transition[0], transition[1]) in self.transitions.keys():
                    self.transitions[(transition[0], transition[1])].append(transition[2])
                else:
                    self.transitions[(transition[0], transition[1])] = [transition[2]]

    def is_dfa(self):
        """
        Checks if the Finite Automata is a Deterministic Finite Automaton (DFA)
        :return: True if the FA is a DFA, False otherwise
        """
        for k in self.transitions.keys():
            if len(self.transitions[k]) > 1:
                return False
        return True

    def check_sequence(self, state, sequence):
        """
        Checks if a sequence is accepted by the FA by recursively checking each possible route
        :param state: The current state
        :param sequence: The sequence of the characters that need to checked
        :return: True if the sequence is accepted by the FA, False otherwise
        """
        if len(sequence) == 0 and state in self.final_states:
            return True
        elif len(sequence) == 0:
            return False
        else:
            routes = []
            for transition in self.transitions.items():
                if transition[0][0] == state and transition[0][1] == sequence[0]:
                    routes.append(self.check_sequence(transition[1][0], sequence[1:]))
            return True if True in routes else False

    def __str__(self):
        """
        Returns the elements of the Finite Automata as a printable string
        :return: The elements of the FA as a string
        """
        return f"\t\tStates = {self.states}\n" \
               f"\t\tAlphabet = {self.alphabet}\n" \
               f"\t\tTransitions = {self.transitions}\n" \
               f"\t\tInitial State = {self.initial_state}\n" \
               f"\t\tFinal States = {self.final_states}"
