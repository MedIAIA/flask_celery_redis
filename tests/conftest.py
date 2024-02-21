# tests/conftest.py
import pytest
from tasks.tasks import redis_client


# Fixture pour le client Redis mocké
@pytest.fixture
def mock_redis_client(mocker):
    return mocker.patch("tasks.tasks.redis_client", autospec=True)


# Fixture pour le client Redis réel
@pytest.fixture
def real_redis_client():
    # Mettez en œuvre la création du client Redis réel selon les besoins de votre projet
    # Assurez-vous que cela est adapté à votre configuration de Redis
    # Exemple pour utiliser un client Redis local avec le module `redis-py` :
    import redis

    return redis.StrictRedis(host="localhost", port=6379, db=0)


# Fixture pour simuler l'acquisition réussie du verrou
@pytest.fixture
def lock_acquired(mock_redis_client):
    mock_redis_client.set.return_value = True
    return mock_redis_client


# Fixture pour simuler l'échec de l'acquisition du verrou
@pytest.fixture
def lock_not_acquired(mock_redis_client):
    mock_redis_client.set.return_value = False
    return mock_redis_client
