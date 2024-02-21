# tests/test_tasks.py
import pytest
from tasks.tasks import add_numbers  # Mettez à jour l'importation ici


def test_add_numbers_lock_acquired(mock_redis_client):
    # Configurer le mock pour que le verrou soit acquis
    mock_redis_client.set.return_value = True

    # Appeler la fonction sous test
    result = add_numbers(3, 4)  # Mettez à jour l'appel ici

    # Vérifier que la fonction renvoie le résultat attendu
    assert result == 7
