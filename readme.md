







export PYTHONPATH=/Users/simed/exemple_api_flask_celery_redis:$PYTHONPATH
pre-commit autoupdate
pre-commit run --all-files
m -rf ~/.cache/pre-commit
git commit . -m 'quick fix' --no-verify


+++++++++++++++++++++++++++++++

echo "# flask_celery_redis" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MedIAIA/flask_celery_redis.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/MedIAIA/flask_celery_redis.git
git branch -M main
git push -u origin main