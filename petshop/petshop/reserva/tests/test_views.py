import pytest
from pytest_django.asserts import assertTemplateUsed

def testar_view(client):
    response = client.get('/reserva/criar/')

    assert response.status_code == 200
    assertTemplateUsed(response,'criar_reserva.html')

