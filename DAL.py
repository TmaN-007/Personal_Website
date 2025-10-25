import sqlite3

def get_connection(db_path="projects.db"):
    """Get database connection with row factory"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database and create projects table if it doesn't exist"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_filename TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def insert_project(title, description, image_filename):
    """Insert a new project into the database"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO projects (title, description, image_filename)
        VALUES (?, ?, ?)
    ''', (title, description, image_filename))

    conn.commit()
    conn.close()

def get_projects():
    """Get all projects ordered by created_at DESC, returns list of dicts"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, title, description, image_filename, created_at
        FROM projects
        ORDER BY created_at DESC
    ''')

    rows = cursor.fetchall()
    conn.close()

    # Convert Row objects to dictionaries
    projects = []
    for row in rows:
        projects.append({
            'id': row['id'],
            'title': row['title'],
            'description': row['description'],
            'image_filename': row['image_filename'],
            'created_at': row['created_at']
        })

    return projects
