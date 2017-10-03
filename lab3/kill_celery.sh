ps -ax | grep celery |  cut -c1-5 | xargs -L1 sudo kill -9
ps -ax | grep flower |  cut -c1-5 | xargs -L1 sudo kill -9

