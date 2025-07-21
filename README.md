# Overview

This project is designed to help reinforce my skills in building interactive web applications using Django. As a future actuary, I have a lot of exams to study for and
my goal was to create a webpage with formula sheets for each of my exams. 
In order to do this I had to understand the architecture of a Django project, how to dynamically generate HTML content from views, 
and how to integrate front-end and back-end components in a cohesive web application.

The web app I created is a study tool for students preparing for the Financial Mathematics (FM) exam. It presents key formulas and concepts as flashcards, helping users to quickly review and memorize material.

To run the app locally:
1. Open a terminal and navigate to the project folder.
2. Activate your Python virtual environment.
3. Run `python manage.py runserver`.
4. Open a browser and go to `http://127.0.0.1:8000/` to see the homepage.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

- **Home Page (`/`)**  
  This is the landing page of the app. It contains a welcome message and a link to the FM Formulas page. The content is generated through Django's template rendering engine and served from a view in `views.py`.

- **FM Formulas Page (`/FM_formulas/`)**  
  This page dynamically generates a list of flashcards for key FM exam concepts. Each flashcard is created in Python code and rendered into HTML using a loop in the template. Users can view terms like interest formulas, annuities, and perpetuities, each with an explanation or formula.

Navigation between pages is handled by standard HTML links and Django’s URL routing system.

# Development Environment

- **Tools Used**:
  - Visual Studio Code
  - Git and GitHub
  - Python virtual environment (venv)

- **Languages and Frameworks**:
  - Python 3
  - Django 4.x
  - HTML/CSS (for templates)

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/stable/)
* [W3Schools - Django Tutorial](https://www.w3schools.com/django/)
* [Stack Overflow](https://stackoverflow.com/)
* [MDN Web Docs](https://developer.mozilla.org/en-US/)

# Future Work

* Store flashcards in a database using Django models instead of hardcoding them.
* Add a feature to shuffle or filter flashcards by category.
* Include a user form to create and save custom flashcards.
* Add a third page to test user knowledge with a quiz-style interface.
