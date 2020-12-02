import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    # g is used to store data that might be accessed by multiple functions during the request
    if 'db' not in g:
        # establishes a connection to the file pointed at by the DATABASE configuration key
        g.db = sqlite3.connect(
            # current_app points to the Flask application handling the request
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # tells the connection to return rows that behave like dicts
        g.db.row_factory = sqlite3.Row

    return g.db

# checks if a connection was created by checking if g.db was set
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    # tells Flask to call that function when cleaning up after returning the response
    app.teardown_appcontext(close_db)
    #adds a new command that can be called with the flask command
    app.cli.add_command(init_db_command)