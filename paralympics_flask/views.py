from flask import current_app as app


@app.route('/', methods=['GET'])
def index():
    """
    Returns a view (HTML page) with a greeting message 'Hello, world'.
    """
    return 'Hello, world!'
