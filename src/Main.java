public class Main {
    public static void main(String[] args) {
        SymbolTable symbolTable = new SymbolTable();

        symbolTable.insert("x", 10);
        symbolTable.insert("y", 20);
        symbolTable.insert("PI", 3.14159);
        symbolTable.insert("12", 12);

        System.out.println("Value of x: " + symbolTable.lookup("x"));
        System.out.println("Value of y: " + symbolTable.lookup("y"));
        System.out.println("Value of PI: " + symbolTable.lookup("PI"));
        System.out.println("Value of 12: " + symbolTable.lookup("12"));

        System.out.println("Is 'x' in the symbol table? " + symbolTable.contains("x"));
        System.out.println("Is '12' in the symbol table? " + symbolTable.contains("12"));

        symbolTable.remove("y");

        symbolTable.display();
    }
}