from . import app

@app.task(bind=True, default_retry_delay=10, max_retries=3, acks_late=True)
def etl(url, s3_url):
    try:
        pass
    except Exception as exc:
        raise self.retry(exc = exc)