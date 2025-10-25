"""
Test suite for database operations (DAL.py)
"""
import pytest
import sqlite3
import os
import DAL


@pytest.fixture
def test_db():
    """Create a temporary test database"""
    test_db_path = "test_projects.db"

    # Create test database
    conn = sqlite3.connect(test_db_path)
    conn.row_factory = sqlite3.Row
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

    yield test_db_path

    # Cleanup: remove test database after tests
    if os.path.exists(test_db_path):
        os.remove(test_db_path)


def test_database_connection():
    """Test that database connection can be established"""
    conn = DAL.get_connection()
    assert conn is not None
    assert isinstance(conn, sqlite3.Connection)
    conn.close()


def test_init_db():
    """Test database initialization creates the projects table"""
    test_db_path = "test_init.db"

    # Remove if exists
    if os.path.exists(test_db_path):
        os.remove(test_db_path)

    # Initialize database
    conn = sqlite3.connect(test_db_path)
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

    # Check table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects'")
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == 'projects'

    conn.close()
    os.remove(test_db_path)


def test_insert_project(test_db):
    """Test inserting a project into the database"""
    # Use test database
    original_get_connection = DAL.get_connection
    DAL.get_connection = lambda db_path="projects.db": sqlite3.connect(test_db)

    # Insert test project
    DAL.insert_project("Test Project", "Test Description", "test_image.jpg")

    # Verify insertion
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects WHERE title='Test Project'")
    result = cursor.fetchone()

    assert result is not None
    assert result[1] == "Test Project"
    assert result[2] == "Test Description"
    assert result[3] == "test_image.jpg"

    conn.close()

    # Restore original function
    DAL.get_connection = original_get_connection


def test_get_projects(test_db):
    """Test retrieving all projects from the database"""
    # Use test database
    original_get_connection = DAL.get_connection

    def test_connection(db_path="projects.db"):
        conn = sqlite3.connect(test_db)
        conn.row_factory = sqlite3.Row
        return conn

    DAL.get_connection = test_connection

    # Insert test projects
    DAL.insert_project("Project 1", "Description 1", "image1.jpg")
    DAL.insert_project("Project 2", "Description 2", "image2.jpg")

    # Get all projects
    projects = DAL.get_projects()

    assert len(projects) >= 2
    assert isinstance(projects, list)
    assert isinstance(projects[0], dict)
    assert 'id' in projects[0]
    assert 'title' in projects[0]
    assert 'description' in projects[0]
    assert 'image_filename' in projects[0]
    assert 'created_at' in projects[0]

    # Restore original function
    DAL.get_connection = original_get_connection


def test_get_projects_ordering(test_db):
    """Test that projects have created_at timestamps in descending order"""
    import time

    # Use test database
    original_get_connection = DAL.get_connection

    def test_connection(db_path="projects.db"):
        conn = sqlite3.connect(test_db)
        conn.row_factory = sqlite3.Row
        return conn

    DAL.get_connection = test_connection

    # Clear existing data
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects")
    conn.commit()
    conn.close()

    # Insert projects with a delay to ensure different timestamps
    DAL.insert_project("First Project", "First", "image1.jpg")
    time.sleep(1)  # 1 second delay to ensure different timestamp
    DAL.insert_project("Second Project", "Second", "image2.jpg")

    # Get projects
    projects = DAL.get_projects()

    # Verify we have exactly 2 projects
    assert len(projects) == 2

    # Verify all projects have created_at timestamps
    for project in projects:
        assert 'created_at' in project
        assert project['created_at'] is not None

    # Restore original function
    DAL.get_connection = original_get_connection


def test_project_data_types(test_db):
    """Test that project data types are correct"""
    # Use test database
    original_get_connection = DAL.get_connection

    def test_connection(db_path="projects.db"):
        conn = sqlite3.connect(test_db)
        conn.row_factory = sqlite3.Row
        return conn

    DAL.get_connection = test_connection

    # Insert test project
    DAL.insert_project("Type Test", "Testing types", "test.jpg")

    # Get projects
    projects = DAL.get_projects()
    project = projects[0]

    assert isinstance(project['id'], int)
    assert isinstance(project['title'], str)
    assert isinstance(project['description'], str)
    assert isinstance(project['image_filename'], str)
    assert isinstance(project['created_at'], str)

    # Restore original function
    DAL.get_connection = original_get_connection
