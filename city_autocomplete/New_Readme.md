City Autocomplete API

This is a Django-based RESTful API that provides autocomplete suggestions for city names based on the input provided by users. The suggestions are generated based on the similarity of the input string to city names and optionally the proximity of the cities to a given geographical location.
Prerequisites

    Python 3
    Django
    Django Rest Framework

Project Setup

    Clone the repository: git clone https://github.com/yourusername/yourrepository.git
    Move into the project directory: cd yourrepository
    Install dependencies: pip install -r requirements.txt
    Migrate the database: python manage.py migrate

Importing City Data

City data is imported from a TSV file using a Django management command. The command reads city data from the cities_canada-usa.tsv file and creates instances of the City model.

    Place your TSV file in the directory: ./suggestions/management/commands/
    Run the command: python manage.py load_cities

The City model contains the following fields:

    name: the name of the city
    country: the country the city is located in
    latitude: the latitude coordinate of the city
    longitude: the longitude coordinate of the city
    full_name: a property that concatenates name, state, and country

Starting the Server

To start the server, run python manage.py runserver. By default, the server will start on http://127.0.0.1:8000/.
Endpoints

The application provides the following endpoint:

GET /suggestions

Parameters:

    q: a string that represents the city name to get suggestions for
    latitude and longitude (optional): coordinates used to prioritize city suggestions near those coordinates

Example:

GET /suggestions?q=Londo&latitude=43.70011&longitude=-79.4163