# SNIPPETS 

[Django Rest Framework Docs](https://www.django-rest-framework.org/tutorial/1-serialization/)

## Starting a project

```bash
mkdir <project_home_name>

cd <project_home_name>

python -m venv venv
# may have to use `python3`

source venv/bin/activate

touch requirements.txt

vi requirements.txt
# add `django`, `djangorestframework`, `django-cors-headers`)

pip install -r requirements.txt

django-admin startproject app 

cd app

django-admin startapp <app_name>
# e.g., `api`, `contacts`, `songs`, a name of a Model

cd .. && code .
```
