# AI Development Notes

## Prompt 1: Initial Website Structure

**Prompt:**
```
Look at the image I sent you and I want to create my personal website in only HTML and css for this assignment. The site should be a multi-page website with consistent navigation including Homepage (index.html), About Me (about.html), Resume (resume.html), Projects (projects.html), and Contact (contact.html). Use Bootstrap and containers to make all the pages responsive and better design. Keep all the pages in consistent design.
```

**AI Output:**
The AI created a complete website structure with:
- All 5 HTML pages with Bootstrap integration
- Consistent navigation across all pages
- A styles.css file with custom color scheme
- Responsive grid layouts using Bootstrap containers
- Hero section on index.html with profile image
- Form validation on contact page
- Thank you page after form submission

**Decision:** **Accepted** - The output provided a solid foundation with proper HTML structure, Bootstrap integration, and consistent styling across all pages.

---

## Prompt 2: Populating Content with JSON Data

**Prompt:**
```
Fill up the my resume and projects page with this json file attached below. Keep the image field empty... ill add the images to the images folder later
```

**AI Output:**
The AI populated:
- Resume page with education (2 degrees), experience (5 jobs with bullet points), skills (4 categories), certifications (3 AWS certs), and interests
- Projects page with 7 projects including descriptions, dates, and technology tags
- Maintained the existing HTML structure while inserting the JSON data

**Decision:** **Accepted with modifications** - Initially accepted the output, but later requested removal of 3 projects and dates/tech tags, adding "Learn More" buttons instead that link to individual project detail pages.

---

## Prompt 3: Creating Photography Gallery

**Prompt:**
```
Under the moon picture add a sentence saying "The moon, October 13, 2024." and under that add a button which says see more of my photography which leads to photography.html which should show all the photos i have in the images_photography folder which is in the images folder. Make the photos a collage with a short desc below it
```

**AI Output:**
The AI created:
- Caption under moon image with date
- "See More of My Photography" button linking to photography.html
- New photography.html page with responsive 3-column grid (Bootstrap col-lg-4)
- All 12 photos from images_photography folder displayed as cards
- Each photo with descriptive caption centered below
- "Back to About Me" button at bottom

**Decision:** **Accepted** - The output created a clean, responsive gallery layout with proper image paths and descriptions. The collage layout worked well with Bootstrap's grid system.

---

## Prompt 4: Adding University Logos to Projects

**Prompt:**
```
Add purdue logo to smart glass and patient monitoring, add indiana logo to customer churn, add tmf logo to pantry mobility, and add a white background to all the image boxes since some of the logos are background free
```

**AI Output:**
The AI:
- Replaced project placeholder images with appropriate logos
- Added Indiana University logo to Project 1 (Customer Churn)
- Added Purdue logo to Projects 2 and 4 (Smart Glasses, Patient Monitoring)
- Added Toyota Mobility Foundation logo to Project 3 (Pantry Mobility)
- Created white background containers (250px height) with flexbox centering
- Set max-height and max-width constraints for proper logo display

**Decision:** **Accepted** - The output properly implemented the logo placements with professional styling and white backgrounds that ensured visibility for transparent logos.

---

## Prompt 5: Background Color Consistency

**Prompt:**
```
Change the background color for every other page except for the index page back to the original color. Add a tiny bit more shadow to the navbar. Change back the color of the underline in resume to the original
```

**AI Output:**
The AI:
- Removed inline `style="background-color: #e8ddd5;"` from all pages except index.html
- Restored original white backgrounds for about/resume/projects/contact/thankyou
- Restored light gray (bg-light) for photography and project detail pages
- Added enhanced navbar shadow: `box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);`
- Changed resume section borders back to `var(--secondary-color)`

**Decision:** **Accepted** - The output correctly reverted the styling changes while maintaining the enhanced navbar shadow for better visual hierarchy.

---

## Reflection (150+ words)

Throughout this project, AI assistance through Claude Code significantly accelerated my development process. The AI excelled at generating boilerplate HTML structures, implementing Bootstrap's responsive grid system, and maintaining consistent styling across multiple pages. It saved me hours of manually writing repetitive HTML and CSS code, particularly when creating the navigation structure across 11 HTML files and populating content from JSON data.

However, AI wasn't perfect. It initially struggled with understanding nuanced design requests, such as the exact spacing between elements and the proper implementation of hover effects on the photography gallery. I had to iterate multiple times on the "Contact Me" button visibility issue and the paragraph spacing on the About page. The AI also initially added unnecessary complexity to simple tasks, like creating modal overlays for photos when I ultimately decided on a static gallery.

I balanced AI assistance with my own judgment by treating the AI as a collaborative coding partner rather than a replacement. I provided clear, specific prompts and carefully reviewed each output before accepting. When the AI suggested solutions, I evaluated them against web design best practices and accessibility standards. For instance, I requested changes to justify text alignment, adjust logo sizing, and ensure proper color contrast. This approach allowed me to leverage AI's speed for structural work while maintaining creative control over design decisions and user experience details.

The key to successful AI collaboration was iterative refinement—starting with broad requests and progressively narrowing down to specific styling and functionality adjustments. This project demonstrated that AI tools are most effective when combined with human oversight, design sensibility, and a clear understanding of project requirements.
