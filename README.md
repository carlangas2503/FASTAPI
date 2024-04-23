# FASTAPI

# Cómo iniciar el proyecto?

1. Create a new virtual venv with name 'env': **python -m venv env**
2. Start virtual venv: **.\env\Scripts\activate**
3. Install dependencies from 'requirements.txt': **pip install -r requirements.txt**
4. if you add new dependencies, remenber save in file 'requirements.txt': **pip freeze > requirements.txt**
5. init api server: **uvicorn app:app --reload**