import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;


/**
 * Custom implementation of a hash table data structure.
 * This hash table allows storing key-value pairs and provides
 * basic operations like put, get, containsKey, remove, and keySet.
 *
 * @param <K> the type of keys stored in the hash table
 * @param <V> the type of values associated with the keys
 */
public class MyHashTable<K, V> {
    private static final int DEFAULT_CAPACITY = 10;
    private LinkedList<Entry<K, V>>[] table;
    private int size;

    /**
     * Inner class representing key-value pairs stored in the hash table.
     *
     * @param <K> the type of keys
     * @param <V> the type of values
     */
    private static class Entry<K, V> {
        K key;
        V value;

        Entry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }

    /**
     * Default constructor. Initializes the hash table with default capacity.
     */
    public MyHashTable() {
        table = new LinkedList[DEFAULT_CAPACITY];
        size = 0;
    }

    /**
     * Private helper method to calculate the hash value for a given key.
     *
     * @param key the key for which the hash value is calculated
     * @return the hash value
     */
    private int getHash(K key) {
        return key.hashCode() % table.length;
    }

    /**
     * Inserts a key-value pair into the hash table. If the key already exists,
     * the associated value is updated.
     *
     * @param key   the key to be inserted or updated
     * @param value the value associated with the key
     */
    public void put(K key, V value) {
        int index = getHash(key);
        if (table[index] == null) {
            table[index] = new LinkedList<>();
        }

        for (Entry<K, V> entry : table[index]) {
            if (entry.key.equals(key)) {
                entry.value = value;
                return;
            }
        }

        table[index].add(new Entry<>(key, value));
        size++;
    }

    /**
     * Retrieves the value associated with the given key.
     *
     * @param key the key for which the value is retrieved
     * @return the value associated with the key, or null if key not found
     */
    public V get(K key) {
        int index = getHash(key);
        if (table[index] != null) {
            for (Entry<K, V> entry : table[index]) {
                if (entry.key.equals(key)) {
                    return entry.value;
                }
            }
        }
        return null;
    }

    /**
     * Checks if the hash table contains the given key.
     *
     * @param key the key to be checked for existence
     * @return true if the key is found, false otherwise
     */
    public boolean containsKey(K key) {
        int index = getHash(key);
        if (table[index] != null) {
            for (Entry<K, V> entry : table[index]) {
                if (entry.key.equals(key)) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * Removes the key-value pair with the given key from the hash table.
     *
     * @param key the key of the pair to be removed
     */
    public void remove(K key) {
        int index = getHash(key);
        if (table[index] != null) {
            table[index].removeIf(entry -> entry.key.equals(key));
            size--;
        }
    }

    /**
     * Returns a set of all keys stored in the hash table.
     *
     * @return a set containing all keys in the hash table
     */
    public Set<K> keySet() {
        Set<K> keys = new HashSet<>();
        for (LinkedList<Entry<K, V>> bucket : table) {
            if (bucket != null) {
                for (Entry<K, V> entry : bucket) {
                    keys.add(entry.key);
                }
            }
        }
        return keys;
    }

    /**
     * Returns the number of key-value pairs in the hash table.
     *
     * @return the number of key-value pairs in the hash table
     */
    public int size() {
        return size;
    }
}
