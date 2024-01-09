# Flask version of the activities

The Flask application is based on the paralympics application that you created for the REST API, however the Marshmallpw
schemas and REST API routes have been removed. The application code should otherwise be as you saw at the end of week 4.

## Check the Flask app runs

Check that the app runs before starting any of the activities.

1. `flask --app paralympics_flask run --debug`

   You may need to change the port number if you already have something running on the default port 5000
   e.g. `flask --app paralympics_flask run --debug --port=5050`.
2. Go to the URL that is shown in the terminal. By default, this is http://127.0.0.1:5000
3. Stop the app using `CTRL+C`

## Create a page using HTML

### HTML basics

The basic tag structure for HTML is `<start_tag> some content </end_tag>`. This set of opening tag + content + closing
tag is referred to as an **HTML element**.

A small number of elements only have an opening tag e.g. `<img>`, `<br>`, `<hr>`. There is a list of
these [void elements here](https://developer.mozilla.org/en-US/docs/Glossary/Void_element).

Elements can also have attributes that give additional information. In this course you will mostly use id
e.g. `id="some-name"` and class e.g. `class="some-class"`. `id` is used to locate a particular element on a webpage,
and `class` is used in adding styles to elements (more on these in later sections).

HTML documents start with a document type declaration `<!DOCTYPE html>`. This is required at the start of the document.

The HTML document itself begins with `<html>` and ends with `</html>`

The part that is mostly not visible in the final webpage is between `<head>` and `</head>`. This is typically metadata,
i.e. info about the page.

The part of the HTML document that is visible in the browser is between `<body>` and `</body>`.

A minimal page structure looks like the following:

```html
<!DOCTYPE html>
<!-- This is an HTML comment, you won't see it on the page -->
<!-- Head section -->
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>COMP0034 Introduction to HTML - Basic page structure</title>
</head>
<!-- Body section -->
<body>
<p>Here is some text on a page.</p>
</body>
</html>
```

### How Flask uses HTML

Flask returns pages from a route using the `render_template` function.

This function takes an HTML template as a parameter.

By default, Flask looks for templates in a folder named `templates` in the application package.

### Activity: change the Flask index() route to display a page from an HTML template

1. Find the [templates folder](../paralympics_flask/templates) in the Flask application.
2. Find and open [index.html](../paralympics_flask/templates/index.html).
3. Add enough HTML to create a basic page with a paragraph tag in the body that says 'Welcome to HTML!'
   e.g. `<p>Welcome to HTML!</p>`.
4. You will need to add `from flask import render_template` to the imports section
   of `views.py`. 
5. Modify the `index()` route in `views.py` to `return render_template('index.html')` in
   place of the current text. 
6. Run the app e.g. `flask --app paralympics_flask run --debug`. 
7. Go to the URL that is shown in the terminal e.g. <http://127.0.0.1:5000>
8. Check the page displays 'Welcome to HTML!' rather than 'Hello, world!'
9. Stop the app using `CTRL+C`

If you get stuck, look at the [week 7 code](), the route with `def index_html():`

## Apply styling using CSS

Bootstrap downloaded from https://getbootstrap.com/docs/5.3/getting-started/download/
https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css

## Use Jinja to create templates

https://flask.palletsprojects.com/en/3.0.x/tutorial/templates/