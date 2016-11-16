# Controk WebService

[![travis-badge]][travis]
[![codecov-badge]][codecov]
[![code-climate-badge]][code-climate]
[![license-badge]][license]

[![docker]]()

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

**Note**: This is the WebService part of the Controk system and may have some features faked for demonstrative purposes. [Click here](https://github.com/jourdanrodrigues/controk-docker) for the fully working system.

### Prerequisites

These instructions will build the environment to run commands on the project.

#### Based on "virtualenv"

Assuming you already have [virtualenv](https://virtualenv.pypa.io/en/stable/) and Python v3.5 installed and have little idea of how to use them.

- `virtualenv -p /path/to/python3.5 venv`;
- `source venv/bin/activate`.

#### Based on "docker"

Assuming you have [docker compose](https://docs.docker.com/compose/) installed (along with [Docker](https://www.docker.com/)).

- `docker-compose build`

### Installing

#### Based on "virtualenv"

- Create `.env` file, based on `.env.example`, and set your environment as you wish;
- `source venv/bin/activate`;
- `python manage.py runserver`.

The server must be running at [http://localhost:8000/].

#### Based on "docker"

- The next command will give you a running server. Needing anything specific, change in `docker-compose.yml`;
- `docker-compose up`.

## Running the tests

### Based on "virtualenv"

- Create a ".env" file base on ".env.example" in the project's root;
- Run `pip install -r requirements.txt`;
- Run `python manage.py test`.

### Based on "docker"

- Open the `docker-compose.yml` file with your favorite text editor and change the `webservice` service command to `python manage.py test`;
- `docker-compose up`.

## Deployment

Clone the project:

`git clone https://github.com/jourdanrodrigues/controk-webservice`

Build the project with docker compose:

`docker-compose build`

Raise the project:

`docker-compose up`

## Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](http://www.django-rest-framework.org/)
* [Docker](https://www.docker.com/)
* [PostgreSQL](https://www.postgresql.org/)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/jourdanrodrigues/controk-webservice/tags). 

## Authors

* **Jourdan Rodrigues** - *Initial work* - [Jourdan Rodrigues](https://github.com/jourdanrodrigues/)

See also the list of [contributors][contributors] who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE][license] file for details

[code-climate-badge]: https://codeclimate.com/github/jourdanrodrigues/controk-webservice/badges/gpa.svg
[code-climate]: https://codeclimate.com/github/jourdanrodrigues/controk-webservice
[codecov-badge]: https://codecov.io/gh/jourdanrodrigues/controk-webservice/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/jourdanrodrigues/controk-webservice
[docker]: https://img.shields.io/docker/automated/jourdanrodrigues/controk-webservice.svg
[license-badge]: https://img.shields.io/github/license/jourdanrodrigues/controk-webservice.svg
[license]: https://github.com/jourdanrodrigues/controk-webservice/blob/master/LICENSE
[travis-badge]: https://travis-ci.org/jourdanrodrigues/controk-webservice.svg?branch=master
[travis]: https://travis-ci.org/jourdanrodrigues/controk-webservice?branch=master

[contributors]: https://github.com/jourdanrodrigues/controk-webservice/contributors
