mkdir -p candylady/media
python manage.py syncdb --all
python manage.py migrate --fake
