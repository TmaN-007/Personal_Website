from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pathlib import Path
import os
import secrets
import DAL

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Upload configuration
app.config['UPLOAD_FOLDER'] = Path('static/images')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_image(file_storage):
    """
    Save uploaded image file to static/images directory
    Returns the saved filename or None if error
    """
    if not file_storage or file_storage.filename == '':
        return None

    if not allowed_file(file_storage.filename):
        return None

    # Sanitize filename
    filename = secure_filename(file_storage.filename)

    # Ensure upload folder exists
    upload_folder = Path(app.config['UPLOAD_FOLDER'])
    upload_folder.mkdir(parents=True, exist_ok=True)

    # Check if file exists, add unique suffix if needed
    file_path = upload_folder / filename
    if file_path.exists():
        # Split filename and extension
        name, ext = os.path.splitext(filename)
        # Add random suffix before extension
        suffix = secrets.token_hex(3)
        filename = f"{name}__{suffix}{ext}"
        file_path = upload_folder / filename

    # Save the file
    file_storage.save(file_path)

    return filename

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    project_list = DAL.get_projects()
    return render_template('projects.html', projects=project_list)

@app.route('/projects/new', methods=['GET', 'POST'])
def project_new():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        image = request.files.get('image')

        # Validate
        if not title:
            flash('Title is required', 'danger')
            return render_template('project_form.html')

        if not description:
            flash('Description is required', 'danger')
            return render_template('project_form.html')

        if not image or image.filename == '':
            flash('Image is required', 'danger')
            return render_template('project_form.html')

        # Save image
        saved_filename = save_image(image)
        if not saved_filename:
            flash('Invalid image file. Allowed formats: PNG, JPG, JPEG, GIF, WEBP', 'danger')
            return render_template('project_form.html')

        # Insert into database
        DAL.insert_project(title, description, saved_filename)

        flash('Project added successfully!', 'success')
        return redirect(url_for('projects'))

    # GET request - show form
    return render_template('project_form.html')

@app.route('/project2')
def project2():
    return render_template('project2.html')

@app.route('/project3')
def project3():
    return render_template('project3.html')

@app.route('/project4')
def project4():
    return render_template('project4.html')

@app.route('/photography')
def photography():
    return render_template('photography.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    # Initialize database on startup
    DAL.init_db()

    # Seed data if table is empty
    projects = DAL.get_projects()
    if len(projects) == 0:
        # Add seed projects with existing images
        DAL.insert_project(
            'Smart Glasses for Visually Impaired',
            'Assistive wearable with object detection and audio feedback using Arduino Nano ESP32 and YOLO algorithm',
            'Project_logos/Purdue_Logo.png'
        )
        DAL.insert_project(
            'Pantry Mobility Project',
            'Consulting project optimizing food pantry logistics for Toyota Mobility Foundation and IEAM',
            'Project_logos/TMF_logo_ogp.jpg'
        )
        DAL.insert_project(
            'Patient Monitoring System',
            'IoT system for real-time patient data access using PIC18F4525 and ESP32',
            'Project_logos/Purdue_Logo.png'
        )
        print("Database seeded with initial projects")

    app.run(debug=True)
