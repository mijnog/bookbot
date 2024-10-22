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

    # Ensure there is data to plot
    if not data:
        print("No data found in the database.")
        return

    # Get total count of all letters
    total_count = sum([row[1] for row in data])

    # Prepare the data for plotting (as percentages)
    letters = [row[0] if row[0] != ' ' else 'space' for row in data]
    counts = [row[1] for row in data]
    percentages = [(count / total_count) * 100 for count in counts]

    # Create a bar chart with percentages
    plt.bar(letters, percentages)
    plt.xlabel('Letters')
    plt.ylabel('Percentage (%)')
    plt.title('Letter Occurrences in Text (as Percentage)')

    # Show percentage labels on top of the bars
    for i, percentage in enumerate(percentages):
        plt.text(i, percentage, f'{percentage:.2f}%', ha='center', va='bottom')

    # Display the plot
    plt.show()

if __name__ == "__main__":
    visualize_data()
