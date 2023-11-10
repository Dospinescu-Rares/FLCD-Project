from Domain.ProgramInternalForm import ProgramInternalForm
from Domain.Scanner import *
from Domain.SymbolTable import SymbolTable


def main():
    """
    Runs the lexical scanner for programs p1.vcl, p2.vcl, p3.vcl and p1err.vcl
    :return: None
    """
    file_names = ["InputFiles/p1.vcl", "InputFiles/p2.vcl", "InputFiles/p3.vcl", "InputFiles/p1err.vcl"]

    with open('OutputFiles/st.out', 'w'):
        pass
    with open('OutputFiles/pif.out', 'w'):
        pass

    for file_name in file_names:
        symbol_table = SymbolTable(21)
        pif = ProgramInternalForm()
        scanner = Scanner('InputFiles/Token.in')

        lexical_errors = scanner.check_lexical_errors(file_name, symbol_table, pif)

        with open('OutputFiles/st.out', 'a') as writer:
            writer.write(f"Symbol table for program {file_name}:\n{str(symbol_table)}\n\n")
        with open('OutputFiles/pif.out', 'a') as writer:
            writer.write(f"Program Internal Form for program {file_name}:\n{str(pif)}\n\n")

        if lexical_errors == '':
            print(f"The program {file_name} has no lexical errors.\n")
        else:
            print(f"The program {file_name} has the following lexical errors:\n{lexical_errors}\n")


main()
