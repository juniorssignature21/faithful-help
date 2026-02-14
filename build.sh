python -m pip install -r requirements.txt

python manage.py collectstatic --noinput

# Apply database migrations
python manage.py makemigrations

python manage.py migrate