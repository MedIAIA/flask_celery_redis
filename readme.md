







export PYTHONPATH=/Users/simed/exemple_api_flask_celery_redis:$PYTHONPATH
pre-commit autoupdate
pre-commit run --all-files
m -rf ~/.cache/pre-commit
git commit . -m 'quick fix' --no-verify
