web: gunicorn app:app -w 4 -b 0.0.0.0:$PORT --worker-class gthread --threads 4 --timeout 120 --max-requests 1000 --max-requests-jitter 50 --keep-alive 10 --log-level warning
