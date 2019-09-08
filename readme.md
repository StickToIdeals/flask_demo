执行命令:

package:

    pipenv shell
    pipenv install 
    
server:

    python manage.py runserver -h 127.0.0.1 -p 5000
   
manage:

    python manage.py db_ceeate_all
    python manage.py clean
    python manage.py forge -t 0001 -c 100

worker:
    
    celery worker -A manage.celery -l INFO
    
beta:
    
    celery beat -A manage.celery -l INFO