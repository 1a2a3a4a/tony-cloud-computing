sudo celery multi start 10 -A tasks -l info
sudo flower  -A tasks --address=0.0.0.0 --port=5555
