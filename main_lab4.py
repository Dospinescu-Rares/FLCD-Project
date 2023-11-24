from Domain.FiniteAutomata import FiniteAutomata


def main_lab4():
    """
    Offers a simple menu in order to use the Finite Automata
    :return: None
    """
    fa = FiniteAutomata('InputFiles/fa.in')

    while True:
        user_input = input("\t0. Exit\n"
                           "\t1. Display All Elements\n"
                           "\t2. Display States\n"
                           "\t3. Display Alphabet\n"
                           "\t4. Display Transitions\n"
                           "\t5. Display Initial State\n"
                           "\t6. Display Final States\n"
                           "\t7. Check if the FA is a DFA\n"
                           "\t8. Check a sequence\n"
                           "\tInput your command: ")

        if user_input == '1':
            print("\t\tFA Elements: \n" + str(fa))
        elif user_input == '2':
            print("\t\tFA States: " + str(fa.states))
        elif user_input == '3':
            print("\t\tFA Alphabet: " + str(fa.alphabet))
        elif user_input == '4':
            print("\t\tFA Transitions: " + str(fa.transitions))
        elif user_input == '5':
            print("\t\tFA Initial State: " + str(fa.initial_state))
        elif user_input == '6':
            print("\t\tFA Final States: " + str(fa.final_states))
        elif user_input == '7':
            print("\t\tIs the FA a DFA? " + str(fa.is_dfa()))
        elif user_input == '8':
            sequence = input("\t\tEnter your sequence: ")
            print("\t\tIs the given sequence accepted? " + str(fa.check_sequence(fa.initial_state, sequence)))
        elif user_input == '0':
            break
        else:
            print("\t\tInvalid input!")


main_lab4()
