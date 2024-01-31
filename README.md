# Python take-home-test (Desciption of task)

Expose an API for querying salary data:

- The goal of this exercise is to design a read-only API (REST) that returns one or more records from the provided dataset
- Don't worry about any web application concerns other than serializing JSON and returning via a GET request.
- Filter by one or more fields/attributes (e.g. /compensation_data?salary[gte]=120000&primary_location=Portland)
- Sort by one or more fields/attributes (e.g. /compensation_data?sort=salary)
- Extra: return a sparse fieldset (e.g. /compensation_data?fields=first_name,last_name,salary)

# Quick start

```git clone git@github.com:Lopatk1n/compensation_service.git```

See Makefile for more commands

```make setup```

# Examples

```
curl --location --globoff 'localhost:8000/compensation/?annual_vacation_in_weeks=1&total_base_salary_in_2018[gte]=5000&fields=employment_type%2Crequired_hours_per_week%2Ctotal_base_salary_in_2018&sort=total_base_salary_in_2018%2Cemployment_type'
```

```
curl --location 'localhost:8000/compensation/'
```

# Api Docs

```
http://127.0.0.1:8000/docs#/
```