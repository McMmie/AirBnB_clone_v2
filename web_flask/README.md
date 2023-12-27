<h1>Web Framework with Flask</h1>

## What is a Web Framework?

A web framework is a software framework designed to aid the development of web applications including web services, web resources, and web APIs. It provides a structured way to build and organize code, offering developers pre-built components, libraries, and tools to streamline the development process.

## Building a Web Framework with Flask

### What is Flask?

Flask is a lightweight and easy-to-extend web framework for Python. It is known for its simplicity and flexibility, making it an excellent choice for building web applications, APIs, and microservices. This section will guide you on how to build a basic web framework using Flask.

### Defining Routes in Flask

In Flask, a route is a URL pattern that the application will "route" to a specific function. These routes determine how the application responds to different HTTP requests. Defining routes is a fundamental aspect of building a web application with Flask.

#### What is a Route?

A route in Flask is a decorator that binds a function to a URL. It specifies the endpoint where the web application should respond, along with the HTTP methods it should handle.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
```

### Handling Variables in a Route

Flask allows you to capture variables from the URL, making your routes dynamic. You can define variable parts by enclosing them in `< >` brackets.

```python
@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'
```

## Templates in Flask

### What is a Template?

In web development, a template is a file containing a mix of HTML, variables, and control structures. Flask uses the Jinja2 template engine, allowing you to create dynamic and reusable HTML pages.

### Creating an HTML Response in Flask using a Template

1. Create a folder named `templates` in your project directory.
2. Save your HTML templates in this folder.
3. Render templates using the `render_template` function.

```python
from flask import render_template

@app.route('/index')
def index():
    return render_template('index.html')
```

### Creating a Dynamic Template (Loops, Conditions...)

Jinja2 templates support various control structures, including loops and conditions. This enables you to dynamically generate content based on data from your application.

```html
<!-- Example of a loop in a Jinja2 template -->
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>

<!-- Example of a condition in a Jinja2 template -->
{% if condition %}
    <p>Condition is True</p>
{% else %}
    <p>Condition is False</p>
{% endif %}
```

### Displaying HTML Data from a MySQL Database

To display data from a MySQL database in your Flask application, you'll need to use a MySQL database driver (e.g., Flask-MySQL). Install the required packages and configure the database connection. Then, query the database and pass the data to your templates.

```python
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database'

mysql = MySQL(app)

@app.route('/users')
def show_users():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)
```

This README provides a basic guide to building a web framework with Flask, defining routes, working with templates, and integrating data from a MySQL database. Explore Flask's documentation for more advanced features and best practices.
