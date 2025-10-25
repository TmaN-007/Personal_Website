# Flask Personal Website with SQLite DAL

## Project Structure

```
Personal_Website/
├── app.py                 # Main Flask application with routes and config
├── DAL.py                 # Data Access Layer with sqlite3 functions
├── requirements.txt       # Python dependencies
├── projects.db           # SQLite database (created on first run)
├── static/
│   ├── css/
│   │   └── style.css     # Custom CSS styles
│   └── images/           # Static images and uploaded project images
│       ├── GJ_Logo.ico
│       ├── Profile_Image.jpg
│       ├── Project_logos/
│       └── images_photography/
└── templates/
    ├── base.html         # Base template with navbar and footer
    ├── index.html        # Home page
    ├── about.html        # About page
    ├── resume.html       # Resume page
    ├── contact.html      # Contact form page
    ├── thankyou.html     # Thank you page after contact
    ├── photography.html  # Photography gallery
    ├── projects.html     # Projects list with database table
    ├── project_form.html # Add new project form with image upload
    ├── project2.html     # Smart Glasses project detail
    ├── project3.html     # Pantry Mobility project detail
    └── project4.html     # Patient Monitoring project detail
```

## Features Implemented

### 1. Data Access Layer (DAL.py)
- Uses stdlib `sqlite3` with `row_factory = sqlite3.Row`
- Functions:
  - `get_connection(db_path="projects.db")` - Get database connection
  - `init_db()` - Initialize database and create projects table
  - `insert_project(title, description, image_filename)` - Insert new project
  - `get_projects()` - Return list of dictionaries ordered by created_at DESC

### 2. Database Schema
```sql
CREATE TABLE projects(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  image_filename TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Image Upload Handling
- File upload to `static/images/` directory
- Validation: png, jpg, jpeg, gif, webp (max 5MB)
- Sanitization using `secure_filename()`
- Automatic unique suffix if file exists
- Configuration:
  ```python
  app.config['UPLOAD_FOLDER'] = Path('static/images')
  app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
  ```

### 4. Flask Routes
- `GET /` - Home page
- `GET /about` - About page
- `GET /resume` - Resume page
- `GET /contact` - Contact form
- `GET /thankyou` - Thank you page
- `GET /photography` - Photography gallery
- `GET /projects` - List all projects from database
- `GET /projects/new` - Show project form
- `POST /projects/new` - Handle form submission and image upload
- `GET /project2`, `/project3`, `/project4` - Detail pages

### 5. Templates
- **base.html**: Shared layout with Bootstrap 5, navbar with active state based on `request.endpoint`, flash message area, and footer
- **projects.html**: Table view with columns for Title, Description, and Image
- **project_form.html**: Bootstrap form with HTML5 validation (title, description, image file input)
- All pages extend `base.html` using Jinja2 inheritance

### 6. App Initialization
- Database initialized on startup with `DAL.init_db()`
- Automatic seeding with 3 sample projects if table is empty

## How to Run

1. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the site**:
   - Open browser to http://127.0.0.1:5000/
   - Navigate to Projects page to see database-driven content
   - Use "Add New Project" button to test image upload

## Dependencies (requirements.txt)
```
Flask==3.0.3
Werkzeug==3.0.4
Jinja2==3.1.4
itsdangerous==2.2.0
MarkupSafe==3.0.1
click==8.1.7
blinker==1.8.2
```

## Key Features
- ✅ Templated architecture with Jinja2
- ✅ SQLite database with proper DAL layer
- ✅ Image upload with validation and security
- ✅ Flash messages for user feedback
- ✅ Bootstrap 5 responsive design
- ✅ Active navbar state tracking
- ✅ HTML5 form validation
- ✅ Automatic database seeding

## Testing the Upload Feature

1. Go to http://127.0.0.1:5000/projects
2. Click "Add New Project"
3. Fill in:
   - Title: e.g., "My Test Project"
   - Description: e.g., "This is a test project description"
   - Image: Select an image file (PNG, JPG, etc.)
4. Click "Add Project"
5. You'll be redirected to the projects page with a success message
6. The new project will appear in the table with the uploaded image
