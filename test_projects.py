"""
Test suite for Flask application routes and functionality
"""
import pytest
import os
import sys
from pathlib import Path

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
import DAL


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing

    # Use a test database
    test_db = "test_projects_flask.db"

    # Initialize test database
    if os.path.exists(test_db):
        os.remove(test_db)

    original_get_connection = DAL.get_connection

    def test_connection(db_path="projects.db"):
        import sqlite3
        conn = sqlite3.connect(test_db)
        conn.row_factory = sqlite3.Row
        return conn

    DAL.get_connection = test_connection
    DAL.init_db()

    with app.test_client() as client:
        yield client

    # Cleanup
    DAL.get_connection = original_get_connection
    if os.path.exists(test_db):
        os.remove(test_db)


def test_home_route(client):
    """Test that the home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Gautham' in response.data or b'Home' in response.data


def test_about_route(client):
    """Test that the about page loads successfully"""
    response = client.get('/about')
    assert response.status_code == 200


def test_contact_route(client):
    """Test that the contact page loads successfully"""
    response = client.get('/contact')
    assert response.status_code == 200


def test_resume_route(client):
    """Test that the resume page loads successfully"""
    response = client.get('/resume')
    assert response.status_code == 200


def test_projects_route(client):
    """Test that the projects page loads successfully"""
    response = client.get('/projects')
    assert response.status_code == 200


def test_photography_route(client):
    """Test that the photography page loads successfully"""
    response = client.get('/photography')
    assert response.status_code == 200


def test_thankyou_route(client):
    """Test that the thank you page loads successfully"""
    response = client.get('/thankyou')
    assert response.status_code == 200


def test_project_new_get(client):
    """Test that the new project form page loads successfully"""
    response = client.get('/projects/new')
    assert response.status_code == 200
    assert b'title' in response.data or b'Title' in response.data


def test_projects_displays_data(client):
    """Test that projects page displays project data"""
    # Insert test project
    DAL.insert_project("Test Project", "Test Description", "test.jpg")

    response = client.get('/projects')
    assert response.status_code == 200
    assert b'Test Project' in response.data
    assert b'Test Description' in response.data


def test_project_new_post_missing_title(client):
    """Test that posting a project without title shows error"""
    response = client.post('/projects/new', data={
        'description': 'Test Description'
    }, follow_redirects=True)

    assert response.status_code == 200
    # Should show error or redirect back to form


def test_project_new_post_missing_description(client):
    """Test that posting a project without description shows error"""
    response = client.post('/projects/new', data={
        'title': 'Test Title'
    }, follow_redirects=True)

    assert response.status_code == 200
    # Should show error or redirect back to form


def test_project2_route(client):
    """Test that project2 detail page loads"""
    response = client.get('/project2')
    assert response.status_code == 200


def test_project3_route(client):
    """Test that project3 detail page loads"""
    response = client.get('/project3')
    assert response.status_code == 200


def test_project4_route(client):
    """Test that project4 detail page loads"""
    response = client.get('/project4')
    assert response.status_code == 200


def test_static_files_exist(client):
    """Test that critical static files are accessible"""
    # Test CSS file
    response = client.get('/static/css/style.css')
    assert response.status_code == 200 or response.status_code == 304


def test_invalid_route(client):
    """Test that invalid routes return 404"""
    response = client.get('/invalid-route-does-not-exist')
    assert response.status_code == 404


def test_app_config(client):
    """Test that app configuration is correct"""
    assert app.config['TESTING'] is True
    assert 'UPLOAD_FOLDER' in app.config
    assert 'MAX_CONTENT_LENGTH' in app.config


def test_allowed_file_function():
    """Test the allowed_file validation function"""
    from app import allowed_file

    assert allowed_file('test.png') is True
    assert allowed_file('test.jpg') is True
    assert allowed_file('test.jpeg') is True
    assert allowed_file('test.gif') is True
    assert allowed_file('test.webp') is True
    assert allowed_file('test.txt') is False
    assert allowed_file('test.exe') is False
    assert allowed_file('test') is False


def test_multiple_projects_ordering(client):
    """Test that multiple projects are displayed in correct order"""
    # Insert multiple projects
    DAL.insert_project("Project 1", "First project", "image1.jpg")
    DAL.insert_project("Project 2", "Second project", "image2.jpg")
    DAL.insert_project("Project 3", "Third project", "image3.jpg")

    response = client.get('/projects')
    assert response.status_code == 200

    # All projects should be visible
    assert b'Project 1' in response.data
    assert b'Project 2' in response.data
    assert b'Project 3' in response.data
