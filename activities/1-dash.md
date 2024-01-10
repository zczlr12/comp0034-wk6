# Plotly Dash version of the activities

The Dash application is based on the paralympics data used in COMP0035 tutorials.

In this activity you will:

- Create a Dash page with an HTML layout
- Style the Dash layout using Bootstrap CSS
- Adapt the Dash layout to support responsive styling
- Adapt the Dash layout to allow several chart areas
- Add dropdown selectors and check boxes to the Dash layout

The activity builds towards a single page Dashboard design with the following layout:

<table>
<tr><td colspan="2">Heading and intro</td><tr>
<tr>
<td>dropdown selector to choose chart content <br> line chart</td>
<td>checkbox selector to choose chart type <br> bar chart</td>
</tr>
<tr>
<td>map showing locations of events</td>
<td>card showing info for an event when clicked on in the map</td>
</tr>
</table>

## Check the Dash app runs

There is code to run a [basic Dash app](../paralympics_dash/paralympics_dash.py) that displays 'Hello world'. This
is copied from the [Dash tutorial](https://dash.plotly.com/tutorial).

1. `python paralympics_dash/paralympics_dash.py`

   You may need to change the port number if you already have something running on the default port 8050
   e.g. `flask --app paralympics_flask run --debug --port=5050`.

2. Go to the URL that is shown in the terminal. By default, this is <http://127.0.0.1:8050>.
3. Stop the app using `CTRL+C`

## Create a Dash page with an HTML layout

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

You can practice using HTML with the optional activity [2-html-intro.md](2-html_intro.md).

### Using HTML in Dash

Dash provides an API, [Dash HTML Components](https://dash.plotly.com/dash-html-components), that "provides pure Python
abstraction around HTML, CSS, and JavaScript.

Instead of writing HTML or using an HTML templating engine, you compose your layout using Python with the Dash HTML
Components module (dash.html)"

The HTML tags supported by Dash are [listed here](https://dash.plotly.com/dash-html-components#full-elements-reference).
You may need to refer to an [HTML reference](https://www.w3schools.com/html/) to know what the tags and their attributes
are; however you
will not write HTML files. You will only use Dash html python functions.

This is an example given in the Dash documentation:

```python
from dash import html

html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])
```

which equates to the following HTML:

```html

<div>
    <h1>Hello Dash</h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
        <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
    </div>
</div>
```

HTML elements can have properties such as style (CSS), class (CSS classes which you will see later) and id (to uniquely
identify an element on a page). More on this in a later section.

### Add HTML elements to the Dash layout

The dash app starter code in `paralympics_dash.py`.

## Style the Dash layout using Bootstrap CSS

## Adapt the Dash layout to support responsive styling

## Adapt the Dash layout to allow several chart areas

## Add dropdown selectors and check boxes to the Dash layout
