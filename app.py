from flask import Flask
from connexion import App
from tasks.tasks import add_numbers
from uvicorn.middleware.asgi2 import ASGI2Middleware
from uvicorn.middleware.wsgi import WSGIMiddleware

app = Flask(__name__)
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"

connex_app = App(__name__, specification_dir="swagger/")
connex_app.add_api("swagger.yml", validate_responses=True)

# Configuration Celery
app.config.update(
    CELERY_BROKER_URL="redis://localhost:6379/0",
    CELERY_RESULT_BACKEND="redis://localhost:6379/0",
)


# comment
@app.route("/add/<int:x>/<int:y>", methods=["GET"])
def add(x, y):
    result = add_numbers.apply_async(args=[x, y])
    return {"task_id": result.id, "status": "Task en cours"}


# Utilisation de WSGIMiddleware pour adapter l'application WSGI à l'interface ASGI
asgi_app = ASGI2Middleware(WSGIMiddleware(app))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(asgi_app, host="127.0.0.1", port=8000, log_level="info")
