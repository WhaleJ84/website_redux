#!/usr/bin/env python3.8
"""
Used to start the Flask application and uses the `personal_website/__init__.py` file to build.
"""

import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from personal_website import create_app, db

app = create_app(os.getenv('PERSONAL_WEBSITE_ENV') or 'dev')
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
