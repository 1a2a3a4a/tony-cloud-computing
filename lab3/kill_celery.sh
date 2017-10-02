ps -ax | grep celery |  cut -c1-5 | xargs -L1 sudo kill -9

