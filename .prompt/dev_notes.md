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
