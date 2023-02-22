## Getting started
### Pre-requisites
1. Latest Python [version](https://www.python.org/downloads/)
2. [MySQL Community Edition](https://dev.mysql.com/downloads/installer/)

### Create a virtual environment (venv)
```
py -m venv .venv
```

### Active the virtual environment
```
.\.venv\Scripts\activate
```

### Install PIP packages
```
pip install -r requirements.txt
```

### Apply latest migrations + seeds to database
```
flask --app src\app db upgrade
```

### Run Flask project
```
flask --app src\app run
```

## Database Migrations
- Uses [Flask-Migrate](https://www.google.com/search?client=firefox-b-d&q=flask-migrate)
- We're currently an issue on auto-generating migration files based on model changes
  - Temporary workaround is just to generate an empty migration file then manually declaring the changes

### Generate empty migration file
```
flask --app src\app db revision --message "<what is inside this migration>"
```

### Then update database
```
flask --app src\app db upgrade
```

