import sqlite3

def setup_db():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                      (id INTEGER PRIMARY KEY, name TEXT, department TEXT, level INTEGER)''')
    conn.commit()
    conn.close()

def add_student(name, dept, level):
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, department, level) VALUES (?, ?, ?)", (name, dept, level))
    conn.commit()
    conn.close()
    print(f"✅ Student {name} added successfully!")

def view_students():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Current Student Records ---")
    if not rows:
        print("No records found.")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Level: {row[3]}")
    conn.close()

# --- NEW FUNCTION START ---
def delete_student(student_id):
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    # Check if the student exists first
    cursor.execute("SELECT name FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    
    if student:
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        print(f"🗑️ Student '{student[0]}' (ID: {student_id}) has been deleted.")
    else:
        print(f"❌ Error: No student found with ID {student_id}")
        
    conn.close()
# --- NEW FUNCTION END ---

setup_db()

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student") # New Option
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == '1':
        n = input("Name: ")
        d = input("Dept: ")
        l = int(input("Level: "))
        add_student(n, d, l)
    elif choice == '2':
        view_students()
    elif choice == '3':
        view_students() # Show list first so user knows which ID to pick
        s_id = int(input("\nEnter the ID of the student to delete: "))
        delete_student(s_id)
    elif choice == '4':
        print("Exiting system... Goodbye!")
        break