import sys
import sqlite3

# Create a database or connect to an existing one
conn = sqlite3.connect('letter_counts.db')
cursor = conn.cursor()

# Create a table to store letter counts
cursor.execute('''CREATE TABLE IF NOT EXISTS letter_counts (
                    letter TEXT PRIMARY KEY,
                    count INTEGER
                )''')
conn.commit()

# Main Code
def sort_on(dict):
    return dict["num"]

def main() -> int:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    print(f"Number of total words: {len(words)}")
    file_contents_lower = file_contents.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz "
    letter_counts = {letter: 0 for letter in alphabet}
    for letter in file_contents_lower:
        if letter in letter_counts:
            letter_counts[letter] += 1

    list_of_counts = []
    for k, v in letter_counts.items():
        list_of_counts.append({'char': k, 'num': v})
    list_of_counts.sort(reverse=True, key=sort_on)
    
    # Insert the letter counts into the database
    store_letter_counts(list_of_counts)

    # Query the database to verify data was inserted
    conn = sqlite3.connect('letter_counts.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM letter_counts")
    data = cursor.fetchall()
    conn.close()

    print(data)  # This should now print the counts

def store_letter_counts(list_of_counts):
    conn = sqlite3.connect('letter_counts.db')
    cursor = conn.cursor()

    for item in list_of_counts:
        char = item['char']
        num = item['num']
        cursor.execute('''INSERT OR REPLACE INTO letter_counts (letter, count) 
                          VALUES (?, ?)''', (char, num))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    sys.exit(main())
