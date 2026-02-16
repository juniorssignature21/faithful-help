
pip install setuptools
pip install -r requirements.txt


# Apply database migrations
echo "Make Migrations..."
python manage.py makemigrations

python manage.py migrate

echo "Collect Static..."
python manage.py collectstatic --noinput

echo "Build process completed!"