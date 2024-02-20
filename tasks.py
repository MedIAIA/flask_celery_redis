from celery import Celery
import time
import redis

app = Celery('tasks', broker='redis://localhost:6379/0')
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Configuration du backend de verrouillage
app.conf.update(
    task_acks_late=True,
    worker_prefetch_multiplier=1,
)

@app.task(bind=True)
def add_numbers(self, x, y):
    lock_key = f"lock:{self.name}:{x}:{y}"
    
    # Essayer d'acquérir le verrou
    lock_acquired = redis_client.set(lock_key, "locked", nx=True, ex=10)
    
    if not lock_acquired:
        # Le verrou n'a pas pu être acquis, tâche déjà en cours d'exécution
        return "La tâche est déjà en cours d'exécution."
    
    try:
        # Le code de votre tâche va ici
        time.sleep(5)  # Simule un travail long
        result = x + y
        return result
    except Exception as e:
        # Gestion des erreurs
        raise
    finally:
        # Libérer le verrou après l'exécution de la tâche
        redis_client.delete(lock_key)
