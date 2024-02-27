import sqlite3

# Function to create a new contact
def create_contact(conn, name, cell, email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, cell, email) VALUES (?, ?, ?)", (name, cell, email))
    conn.commit()
    print(f"Contact {name} added successfully.")

# Function to display all contacts
def display_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Cell#: {contact[2]}, E-mail: {contact[3]}")

# Connect to the SQLite database (or create if not exists)
conn = sqlite3.connect('contacts.db')

# Create a table to store contacts if not exists
conn.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        cell TEXT NOT NULL,
        email TEXT
    )
''')

# Insert 5 rows of data
contacts_data = [
    ("Sunil", "6362753027", "Sunil@gmail.com"),
    ("Rakesh", "8277490733", "Rakesh@gmail.com"),
    ("Rohan", "6360112301", "Rohan@gmail.com"),
    ("Gokul", "8618220347", "Gokul@gmail.com"),
    ("Raghavendra", "9108070437", "Raghavendra@gmail.com")
]

for contact_data in contacts_data:
    create_contact(conn, *contact_data)

# Display all contacts
display_contacts(conn)

# Close the database connection
conn.close()
