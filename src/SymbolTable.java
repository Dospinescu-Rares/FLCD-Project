/**
 * The SymbolTable class provides a simple interface to manage symbols (identifiers and constants)
 * using a custom hash table implementation. It allows inserting, looking up, checking existence,
 * and removing symbols based on their names.
 * Symbols are stored as key-value pairs, where the key is the symbol name (a String) and
 * the value can be any Object.
 */
public class SymbolTable {
    private MyHashTable<String, Object> symbolTable;

    public SymbolTable() {
        symbolTable = new MyHashTable<>();
    }

    /**
     * Inserts a symbol into the symbol table with the given name and value.
     *
     * @param name  the name of the symbol (identifier or constant)
     * @param value the value associated with the symbol
     */
    public void insert(String name, Object value) {
        symbolTable.put(name, value);
    }

    /**
     * Looks up and retrieves the value associated with the given symbol name.
     *
     * @param name the name of the symbol to be looked up
     * @return the value associated with the symbol, or null if not found
     */
    public Object lookup(String name) {
        return symbolTable.get(name);
    }

    /**
     * Checks if the symbol table contains a symbol with the given name.
     *
     * @param name the name of the symbol to be checked
     * @return true if the symbol is in the table, false otherwise
     */
    public boolean contains(String name) {
        return symbolTable.containsKey(name);
    }

    /**
     * Removes the symbol with the given name from the symbol table.
     *
     * @param name the name of the symbol to be removed
     */
    public void remove(String name) {
        symbolTable.remove(name);
    }

    /**
     * Displays the contents of the symbol table.
     * Symbols are displayed as key-value pairs.
     */
    public void display() {
        System.out.println("Symbol Table Contents:");
        for (String key : symbolTable.keySet()) {
            Object value = symbolTable.get(key);
            System.out.println(key + " => " + value);
        }
    }
}
