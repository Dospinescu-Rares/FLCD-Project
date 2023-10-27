import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;

public class Main {
    public static void main(String[] args) {
        SymbolTable symbolTable = new SymbolTable();

        try {
            PrintStream out = new PrintStream(new FileOutputStream("result.txt"));
            System.setOut(out);
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found - " + e.getMessage());
            return;
        }

        System.out.println("Inserting the following values to the symbol table: x=10, PI=3.14159, 12=12");
        symbolTable.insert("x", 10);
        symbolTable.insert("PI", 3.14159);
        symbolTable.insert("12", 12);

        System.out.println("\nUsing Lookup to check the values of the elements that were inserted");
        System.out.println("Value of x: " + symbolTable.lookup("x"));
        System.out.println("Value of PI: " + symbolTable.lookup("PI"));
        System.out.println("Value of 12: " + symbolTable.lookup("12"));

        System.out.println("\nChecking if all the elements are present in the symbol table");
        System.out.println("Is 'x' in the symbol table? " + symbolTable.contains("x"));
        System.out.println("Is 'PI' in the symbol table? " + symbolTable.contains("PI"));
        System.out.println("Is '12' in the symbol table? " + symbolTable.contains("12"));
        System.out.println("Is 'z' in the symbol table? " + symbolTable.contains("z"));

        System.out.println("\nRemoving the element with key 'y' from the symbol table");
        symbolTable.remove("y");
        System.out.println("Is 'y' in the symbol table? " + symbolTable.contains("y") + "\n");

        symbolTable.display();
    }
}