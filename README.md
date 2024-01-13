# COMP0034 Week 6 Coding activities: HTML, CSS, Flask Jinja and Dash layout

## Set-up

1. Fork the repository <https://github.com/nicholsons/comp0034-wk6>
2. Clone the forked repository to create a project in your IDE
3. Create and activate a virtual environment in the project folder e.g.

    - MacOS: `python3 -m venv .venv` then `source .venv/bin/activate`
    - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
4. Check `pip` is the latest versions: `pip install --upgrade pip`
5. Install the requirements. You may wish to edit [requirements.txt](requirements.txt) first to remove the packages for
   Flask or Dash if you only want to complete the activities for one type of app.

    - e.g. `pip install -r requirements.txt`
6. Install the paralympics code e.g. `pip install -e .`

## Activity instructions

The activities introduce HTML and CSS in the specific contexts of Dash and
Flask. That is, you will learn just enough HTML and CSS to get you started with the application frameworks.

There are two versions of the activities. You can complete both, or just the version for the framework you intend
to use for coursework 2. Dash is for dashboard apps (apps that mostly contain charts); Flask is for any other app e.g.
pages that include a feature that uses a machine learning model or pages that work with the data in some other way.

1. [Dash activities](activities/1-dash.md)
2. [Flask activities](activities/1-flask.md)

If you want to learn a little HTML, CSS and JavaScript independently of the application framework then the activities
folder includes optional
activities: [html intro](activities/2-html_intro), [css intro](activities/3-css_intro), [responsive design intro](activities/4-responsive_intro.md),
and [js intro](activities/5-js_intro).