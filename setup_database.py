import sqlite3
import os

# Create or connect to the database
conn = sqlite3.connect('equipment.db')
cursor = conn.cursor()


# ✅ NEW: Create table for machine metadata
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MachineInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        existing_image TEXT,
        machine_name TEXT,
        purchase_date TEXT,
        last_inspection_date TEXT,
        last_service_date TEXT
    )
''')

# ✅ NEW: Insert sample machine data
cursor.executemany('''
    INSERT INTO MachineInfo (existing_image, machine_name, purchase_date, last_inspection_date, last_service_date)
    VALUES (?, ?, ?, ?, ?)
''', [
    ("A", "Machine 1", "12-12-2022", "22-04-2024", "08-01-2025"),
    ("B", "Machine 2", "12-12-2023", "22-08-2024", "08-02-2025"),
    ("C", "Machine 3", "12-12-2021", "23-08-2024", "08-04-2025")
])

# Commit and close
conn.commit()
conn.close()
print("✅ Database updated successfully!")