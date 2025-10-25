# AI Development Notes

## Prompt 1: Initial Website Structure

**Prompt:**
Look at the image I sent you and I want to create my personal website in only HTML and CSS for this assignment. The site should be a multi-page website with consistent navigation including Homepage (index.html), About Me (about.html), Resume (resume.html), Projects (projects.html), and Contact (contact.html). Use Bootstrap and containers to make all the pages responsive and better design. Keep all the pages in consistent design.

**AI Suggestion:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gautham - Personal Website</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="sticky-top bg-white shadow-sm">
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container">
                <a class="navbar-brand" href="index.html">Gautham</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto align-items-center">
                        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="about.html">About Me</a></li>
                        <li class="nav-item"><a class="nav-link" href="resume.html">Resume</a></li>
                        <li class="nav-item"><a class="nav-link" href="projects.html">Projects</a></li>
                        <li class="nav-item"><a class="nav-link btn-consultation" href="contact.html">Contact Me</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <main>
        <section class="hero py-5" style="background-color: #e8ddd5;">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-lg-6">
                        <h1 class="mb-4">Hi, I'm Gautham</h1>
                        <p class="lead mb-4">I help small businesses and entrepreneurs build meaningful digital experiences.</p>
                        <a href="projects.html" class="btn btn-primary me-3">View Projects</a>
                        <a href="contact.html" class="btn btn-outline-primary">Get in Touch</a>
                    </div>
                    <div class="col-lg-6">
                        <img src="images/profile.jpg" alt="Gautham" class="img-fluid rounded-4 shadow">
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-dark text-white text-center py-4">
        <div class="container">
            <p class="mb-0">&copy; 2025 Gautham. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

With custom CSS:
```css
:root {
    --primary-color: #8b5a5a;
    --primary-dark: #6d4747;
    --secondary-color: #e8ddd5;
}

.btn-primary {
    background-color: var(--primary-color);
    border-color: var(--primary-color);
}

.btn-outline-primary {
    color: var(--primary-color);
    border-color: var(--primary-color);
}

.navbar-brand {
    background: linear-gradient(135deg, #8b5a5a, #c17b7b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    font-size: 1.5rem;
}
```

**Reflection:** The AI gave me a full 5-page skeleton with Bootstrap already hooked up and a pretty clean navbar. Honestly, this saved me a ton of time since I didn't have to write all that boilerplate myself. The color scheme it picked worked well too, so I just went with it. Good starting point.

---

## Prompt 2: Populating Content with JSON Data

**Prompt:**
Fill up my resume and projects page with this JSON file attached below. Keep the image field empty... I'll add the images to the images folder later.

**AI Suggestion:**
```html
<!-- Resume Page -->
<section class="py-5">
    <div class="container">
        <h2 class="mb-4">Education</h2>
        <div class="mb-4">
            <h3>Master's in Information Systems</h3>
            <p class="text-muted">Indiana University, Bloomington | Expected May 2025 | GPA: 4.0/4.0</p>
        </div>
        <div class="mb-4">
            <h3>Bachelor's in Electronics and Communication Engineering</h3>
            <p class="text-muted">Amrita Vishwa Vidyapeetham | Aug 2019 - May 2023 | GPA: 9.18/10.0</p>
        </div>

        <h2 class="mb-4 mt-5">Experience</h2>
        <div class="mb-4">
            <h3>Sales & Marketing Intern</h3>
            <p class="text-muted">Staqo | Jun 2024 - Aug 2024</p>
            <ul>
                <li>Generated $50,000+ in sales from 50+ client meetings</li>
                <li>Developed strategic proposals and cold-called 300+ B2B prospects</li>
            </ul>
        </div>
        <!-- More experience entries... -->
    </div>
</section>

<!-- Projects Page -->
<div class="row g-4">
    <div class="col-md-6">
        <div class="card h-100">
            <div class="card-body">
                <h3 class="card-title">Customer Churn Prediction</h3>
                <p class="card-text">Machine learning model to predict customer churn with 85% accuracy</p>
                <a href="project1.html" class="btn btn-primary">Learn More</a>
            </div>
        </div>
    </div>
    <!-- More project cards... -->
</div>
```

**Reflection:** This worked pretty smoothly. The AI read through my JSON and laid everything out in a reasonable way. I did end up asking it to remove the dates and tech stacks from the project cards later because they looked cluttered, but the initial pass was solid enough that I didn't need to rewrite much by hand.

---

## Prompt 3: Creating Project Detail Pages

**Prompt:**
Add this as learn more for Customer Churn: [detailed narrative text provided]
This for Smart Glasses: [detailed narrative text provided]
This for Pantry Mobility: [detailed narrative text provided]
This for Patient Monitoring: [detailed narrative text provided]

**AI Suggestion:**
```html
<!-- project1.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Churn Prediction - Gautham</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main>
        <section class="py-5 bg-light">
            <article class="bg-white rounded-4 shadow-sm p-4 p-md-5">
                <h1 class="mb-4">Customer Churn Prediction</h1>
                <div class="project-content">
                    <p>This project began with a fundamental business challenge: understanding why customers leave...</p>
                    <p>The technical approach was methodical. I started with data preprocessing, handling missing values...</p>
                    <!-- Full narrative content -->
                </div>
                <div class="mt-5">
                    <a href="projects.html" class="btn btn-primary">Back to Projects</a>
                </div>
            </article>
        </section>
    </main>
</body>
</html>
```

**Reflection:** The AI built out separate detail pages for each project with all the text I gave it. One annoying thing was that it made the first paragraph bigger by default with some `class="lead"` thing, which looked weird, so I had to tell it to remove that. But other than that small fix, the pages came out looking clean and readable.

---

## Prompt 4: Logo Integration and Branding

**Prompt:**
Instead of this "Gautham" text in the navbar, make a cool GJ logo and link it. [Later: I uploaded the GJ_Logo.ico file]

Add Purdue logo to Smart Glasses and Patient Monitoring, add Indiana logo to Customer Churn, add TMF logo to Pantry Mobility, and add a white background to all the image boxes since some of the logos are background-free.

**AI Suggestion:**
```html
<!-- Updated navbar across all 11 pages -->
<a class="navbar-brand" href="index.html">
    <img src="images/GJ_Logo.ico" alt="GJ Logo" style="height: 40px; width: auto;">
</a>

<!-- Favicon added to all pages -->
<link rel="icon" type="image/x-icon" href="images/GJ_Logo.ico">

<!-- Project card with logo -->
<div class="card h-100 shadow-sm">
    <div style="height: 250px; background-color: white; display: flex; align-items: center; justify-content: center;">
        <img src="images/Project_logos/Purdue_logo.png" alt="Purdue University Logo"
             style="max-height: 200px; max-width: 90%; object-fit: contain;">
    </div>
    <div class="card-body d-flex flex-column">
        <h3 class="card-title">Smart Glasses for Visually Impaired</h3>
        <p class="card-text flex-grow-1">Computer vision and voice assistance system...</p>
        <a href="project2.html" class="btn btn-primary mt-auto">Learn More</a>
    </div>
</div>
```

Updated CSS to remove gradient from navbar-brand:
```css
/* Removed:
.navbar-brand {
    background: linear-gradient(135deg, #8b5a5a, #c17b7b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
*/
```

**Reflection:** This was actually pretty impressive. The AI swapped out the text with my logo image across all 11 HTML files and even remembered to add the favicon. The white background containers for the university logos were a nice touch too since some of them had transparent backgrounds that would've looked weird otherwise. Saved me from having to manually edit each file.

---

## Prompt 5: Background Color and Navigation Polish

**Prompt:**
Make all the pages the same background color as index.html except for the navbar which should all be the same color as now. [Later: Actually, change the background color for every other page except for the index page back to the original color. Add a tiny bit more shadow to the navbar. Change back the color of the underline in resume to the original.]

**AI Suggestion:**
```css
/* Enhanced navbar shadow */
header.sticky-top {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

/* Resume border color restored */
.resume-section {
    border-color: var(--secondary-color) !important;
}

/* Contact Me button visibility fix */
.btn-consultation:hover {
    background-color: var(--primary-dark) !important;
    color: #fff !important;
}

.btn-consultation.active {
    background-color: var(--primary-dark) !important;
    color: #fff !important;
}
```

Background colors:
- index.html: `style="background-color: #e8ddd5;"` on hero section only
- All other pages: reverted to original `bg-light` or white backgrounds

**Reflection:** I kind of went back and forth on this one. First I asked for all pages to have the same background, then realized it looked too uniform and asked to revert it. The AI handled the back-and-forth without getting confused, which was nice. The navbar shadow enhancement was subtle but made the header pop more, and fixing the Contact Me button so the text stayed visible was a good catch.

---

## Reflection

Using AI for this website project was honestly a mixed bag, but overall it saved me a lot of grunt work. The biggest win was not having to manually type out repetitive HTML structures across 11 different pages. Things like navigation bars, footers, and Bootstrap boilerplate would've taken forever to copy-paste and update by hand, but the AI just churned them out.

That said, it wasn't perfect. Sometimes I'd ask for something simple like adjusting paragraph spacing, and it would misunderstand or add unnecessary complexity. The photography gallery was a good example—I asked for hover effects, and it went overboard with modals and transitions. Eventually I just told it to scrap all that and keep the images static because the fancy stuff wasn't adding any value.

I learned pretty quickly that vague prompts got vague results. When I said things like "make it look better," the AI would just guess at what I wanted. But when I was specific—like "add ps-lg-4 padding on the left"—it nailed it every time. So I started treating it more like a junior developer who needed clear instructions rather than a mind reader.

The weirdest part was figuring out how much to trust it. Sometimes the AI would suggest something that looked fine at first glance but didn't quite make sense when I thought about usability or accessibility. I had to review everything it generated and make judgment calls about what to keep and what to change.

In the end, I think I found a good balance. I handled the big-picture stuff—deciding on the overall structure, color scheme, and which features to include—while the AI handled the tedious stuff like updating copyright notices or swapping logos across multiple files. It's like having an assistant who's really fast but needs supervision. You can get a lot done quickly, but you can't just set it and forget it. Human oversight still matters, especially for design choices and making sure the user experience actually makes sense.

---

## Prompt 6: Flask Conversion with SQLite DAL and Image Upload

**Prompt:**
You are an expert Flask developer. Convert my small Flask site into a templated app with a SQLite DAL and a Projects feature that reads from and writes to a DB, including **image upload** to `static/images/`. Follow the assignment and use my instructor's class examples as the coding style reference.

Use these class examples as style references:
* Routing + rendering pattern (`application.py` using `render_template`, `request`, and DAL calls). Use the same GET/POST handler structure for the form page.
* Simple DAL functions pattern that return **lists of dictionaries** and use `sqlite3` (see `getAllMovies`).
* Insert + select functions in the DAL (`saveMovieDB`, `getAllMovies`) as a model for our projects table.
* Package versions for Flask stack (requirements). Keep compatible with these versions unless there's a good reason.

**AI Suggestion:**

Created **DAL.py** with clean separation:
```python
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
```

Updated **app.py** with proper Flask configuration:
```python
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

def save_image(file_storage):
    """Save uploaded image with validation and unique naming"""
    if not file_storage or file_storage.filename == '':
        return None
    if not allowed_file(file_storage.filename):
        return None

    filename = secure_filename(file_storage.filename)
    upload_folder = Path(app.config['UPLOAD_FOLDER'])
    upload_folder.mkdir(parents=True, exist_ok=True)

    # Add unique suffix if file exists
    file_path = upload_folder / filename
    if file_path.exists():
        name, ext = os.path.splitext(filename)
        suffix = secrets.token_hex(3)
        filename = f"{name}__{suffix}{ext}"
        file_path = upload_folder / filename

    file_storage.save(file_path)
    return filename

@app.route('/projects')
def projects():
    project_list = DAL.get_projects()
    return render_template('projects.html', projects=project_list)

@app.route('/projects/new', methods=['GET', 'POST'])
def project_new():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        image = request.files.get('image')

        # Validation
        if not title or not description or not image:
            flash('All fields are required', 'danger')
            return render_template('project_form.html')

        # Save image
        saved_filename = save_image(image)
        if not saved_filename:
            flash('Invalid image file', 'danger')
            return render_template('project_form.html')

        # Insert into database
        DAL.insert_project(title, description, saved_filename)
        flash('Project added successfully!', 'success')
        return redirect(url_for('projects'))

    return render_template('project_form.html')
```

Created **templates/base.html** with shared layout:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Gautham - Digital Experience Designer{% endblock %}</title>
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='images/GJ_Logo.ico') }}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header class="sticky-top bg-white shadow-sm">
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container">
                <a class="navbar-brand" href="{{ url_for('home') }}">
                    <img src="{{ url_for('static', filename='images/GJ_Logo.ico') }}" alt="GJ Logo" style="height: 40px;">
                </a>
                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav ms-auto align-items-center">
                        <li class="nav-item">
                            <a class="nav-link {% if request.endpoint == 'home' %}active{% endif %}" href="{{ url_for('home') }}">Home</a>
                        </li>
                        <!-- More nav items with active state tracking -->
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <main>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="container mt-3">
                    {% for category, message in messages %}
                        <div class="alert alert-{{ category }} alert-dismissible fade show">
                            {{ message }}
                            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                        </div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>

    <footer class="bg-dark text-white text-center py-4">
        <div class="container">
            <p class="mb-0">&copy; 2025 Gautham Jayakrishnan. All rights reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

Created **templates/projects.html** with database table:
```html
{% extends "base.html" %}

{% block content %}
<section class="projects-section py-5">
    <div class="container">
        <h1 class="display-3 mb-3 text-center">Projects</h1>
        <div class="text-center mb-5">
            <a href="{{ url_for('project_new') }}" class="btn btn-primary btn-lg">Add New Project</a>
        </div>

        {% if projects %}
        <div class="table-responsive">
            <table class="table table-striped table-bordered align-middle">
                <thead class="table-dark">
                    <tr>
                        <th>Title</th>
                        <th>Description</th>
                        <th style="width: 200px;">Image</th>
                    </tr>
                </thead>
                <tbody>
                    {% for p in projects %}
                    <tr>
                        <td>{{ p.title }}</td>
                        <td>{{ p.description }}</td>
                        <td class="text-center">
                            <img src="{{ url_for('static', filename='images/' ~ p.image_filename) }}"
                                 alt="{{ p.title }}"
                                 class="img-fluid"
                                 style="max-height:150px;object-fit:contain;">
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% endif %}
    </div>
</section>
{% endblock %}
```

Created **templates/project_form.html** with image upload:
```html
{% extends "base.html" %}

{% block content %}
<section class="py-5">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="bg-white rounded-4 shadow-sm p-4 p-md-5">
                    <h1 class="mb-4 text-center">Add New Project</h1>

                    <form action="{{ url_for('project_new') }}" method="post"
                          enctype="multipart/form-data" class="needs-validation" novalidate>
                        <div class="mb-4">
                            <label for="title" class="form-label">Title *</label>
                            <input type="text" class="form-control" id="title" name="title" required>
                        </div>

                        <div class="mb-4">
                            <label for="description" class="form-label">Description *</label>
                            <textarea class="form-control" id="description" name="description" rows="5" required></textarea>
                        </div>

                        <div class="mb-4">
                            <label for="image" class="form-label">Project Image *</label>
                            <input type="file" class="form-control" id="image" name="image" accept="image/*" required>
                            <div class="form-text">Allowed: PNG, JPG, JPEG, GIF, WEBP (Max 5MB)</div>
                        </div>

                        <button type="submit" class="btn btn-primary btn-lg px-5">Add Project</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</section>
{% endblock %}
```

Updated **requirements.txt** to match instructor's versions:
```
Flask==3.0.3
Werkzeug==3.0.4
Jinja2==3.1.4
itsdangerous==2.2.0
MarkupSafe==3.0.1
click==8.1.7
blinker==1.8.2
```

**Reflection:** This was probably the most technically complex prompt I've done with AI so far. I was worried it would mess up the structure since I had to convert 11 static HTML pages into a Flask app with templates, but it actually handled it really well.

The AI followed the instructor's coding style pretty closely. The DAL functions return lists of dictionaries just like the class examples, the route handlers follow the same GET/POST pattern, and it used `render_template` everywhere consistently. That was important because the assignment specifically said to match the class style.

What impressed me most was the image upload implementation. The AI included proper validation (file type, size limits), security (using `secure_filename()`), and even added logic to append a unique suffix if a file already exists. That's the kind of detail I might have missed if I was rushing through it myself.

The template inheritance with `base.html` cleaned up a ton of code duplication. Instead of having the navbar and footer repeated in 11 files, now it's all in one place. The active nav state tracking with `{% if request.endpoint == 'home' %}active{% endif %}` was a nice touch too—I didn't even ask for that specifically.

One thing I had to debug was the virtual environment. The AI initially tried to run the app without activating venv, which threw a ModuleNotFoundError. But once I pointed that out, it fixed it immediately. The database seeding also needed a manual run to populate the initial projects, but that was more of a workflow thing than a code issue.

The projects table view looks clean with Bootstrap's striped table styling, and the form validation uses HTML5 attributes plus Bootstrap's validation classes. The flash messages for success/error states work perfectly and auto-dismiss, which gives good user feedback.

Overall, this conversion took what would have been several hours of manual refactoring and compressed it into maybe 30 minutes of prompting and testing. The AI understood the architecture I needed (DAL → Routes → Templates), implemented all the pieces correctly, and even caught edge cases like duplicate filenames. It's the kind of task where AI really shines—taking well-defined requirements and generating a lot of boilerplate code that follows consistent patterns. I still had to review everything and test it end-to-end, but the heavy lifting was done for me.
