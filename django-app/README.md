Django frontend instructions:

1. Install dependencies (preferably in venv):
   pip install -r requirements.txt

2. Run migrations and create a superuser:
   python manage.py migrate
   python manage.py createsuperuser

3. Collect static (optional for deploy):
   python manage.py collectstatic

4. Run dev server:
   python manage.py runserver 8000

Notes:
- Ensure Express-Mongo backend is running and accessible (default http://localhost:3001).
- For sentiment analyzer: NLTK will download vader_lexicon on first POST to /sentiment/.
