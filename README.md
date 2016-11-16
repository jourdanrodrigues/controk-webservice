# Controk WebService

[![travis-badge]][travis]
[![codecov-badge]][codecov]
[![code-climate-badge]][code-climate]
[![license-badge]][license]

[![docker]]()

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

### With "virtualenv"

Assuming you have [virtualenv](https://virtualenv.pypa.io/en/stable/) installed and knows how to use it.

- Create a ".env" file base on ".env.example";
- Run `virtualenv -p /path/to/python3.5 venv`
- Run `source venv/bin/activate`
- Run `pip install -r requirements.txt`
- Run `python manage.py test`

### With "docker"

Assuming you have [docker-compose]() installed.

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
