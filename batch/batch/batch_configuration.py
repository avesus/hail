import os

KUBERNETES_TIMEOUT_IN_SECONDS = float(os.environ.get('KUBERNETES_TIMEOUT_IN_SECONDS', 5.0))
REFRESH_INTERVAL_IN_SECONDS = int(os.environ.get('REFRESH_INTERVAL_IN_SECONDS', 5 * 60))
DEFAULT_NAMESPACE = os.environ['HAIL_DEFAULT_NAMESPACE']
PROJECT = os.environ['PROJECT']
assert PROJECT != ''
KUBERNETES_SERVER_URL = os.environ['KUBERNETES_SERVER_URL']
BATCH_BUCKET_NAME = os.environ['HAIL_BATCH_BUCKET_NAME']
WORKER_LOGS_BUCKET_NAME = os.environ['HAIL_WORKER_LOGS_BUCKET_NAME']
HAIL_SHA = os.environ['HAIL_SHA']
HAIL_SHOULD_PROFILE = os.environ.get('HAIL_SHOULD_PROFILE') is not None
ENABLE_STANDING_WORKER = os.environ.get('ENABLE_STANDING_WORKER') is not None
STANDING_WORKER_MAX_IDLE_TIME_MSECS = int(os.environ['STANDING_WORKER_MAX_IDLE_TIME_SECS']) * 1000
WORKER_MAX_IDLE_TIME_MSECS = 30 * 1000
HAIL_SHOULD_CHECK_INVARIANTS = os.environ.get('HAIL_SHOULD_CHECK_INVARIANTS') is not None
