# Superheroes

A simple Flask restful API dor managing superheroes, their powers and the strength of those powers.

Built with SQLALchemy and Flask-Migrate


 # Features

- View all heroes and powers
- View specific hero or power by ID
- Update power descriptions
- Assign powers to heroes with strength levels
- Validation for names, descriptions, and strength

# Tech Stack

- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite

# Project Structure
.
├── app.py
├── instance
│   └── heroes.db
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── d1f004869988_added_description_column_to_the_hero_.py
├── models.py
├── Pipfile
├── Pipfile.lock
├── __pycache__
│   ├── app.cpython-38.pyc
│   ├── models.cpython-38.pyc
│   └── routes.cpython-38.pyc
├── README.md
├── routes.py
└── seed.py

# API Endpoints

>> Heroes
Method	Endpoint	    Description
GET	    /heroes	        Get all heroes
GET	    /heroes/<id>	Get a hero by ID

>> Powers
Method	 Endpoint	    Description
GET	     /powers	    Get all powers
GET	     /powers/<id>	Get a power by ID
PATCH	 /powers/<id>	Update a power's description

>> Hero Powers
Method	 Endpoint	    Description
GET	     /hero_powers	Get all hero-power relationships
POST	 /hero_powers	Assign a power to a hero with a strength level

# Validations
>> Hero and Power names must be at least 3 characters.

>>Power descriptions must be at least 20 characters.

>> Strength must be one of: "Strong", "Average", or "Weak".

# Getting started

>> Clone the repository
>> Install the dependecies
>> Run the applicatiion (flask run)
