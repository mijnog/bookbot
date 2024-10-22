import sqlite3
import matplotlib.pyplot as plt

def visualize_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('letter_counts.db')
    cursor = conn.cursor()

    # Fetch the data
    cursor.execute("SELECT * FROM letter_counts ORDER BY count DESC")
    data = cursor.fetchall()
    conn.close()

    # Debug: Print the data to see if it was fetched correctly
    print(data)

    # Ensure there is data to plot
    if not data:
        print("No data found in the database.")
        return

    # Prepare the data for plotting
    letters = [row[0] if row[0] != ' ' else 'space' for row in data]
    counts = [row[1] for row in data]

    # Create a bar chart
    plt.bar(letters, counts)
    plt.xlabel('Letters')
    plt.ylabel('Counts')
    plt.title('Letter Occurrences in Text')
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    visualize_data()
