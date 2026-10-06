from fastapi.testclient import TestClient
from backend import app as service
import pytest

client=TestClient(service.app)

def test_quote_server_calculates_prices():
    response=client.post('/api/quote',json=[{'id':'desk-oak','quantity':2},{'id':'chair-form','quantity':2}])
    assert response.status_code==200
    assert response.json()['total']==87600

@pytest.mark.parametrize('items',[[{'id':'invented','quantity':1}],[{'id':'desk-oak','quantity':99}],[{'id':'desk-oak','quantity':0}],[{'id':'desk-oak','quantity':1},{'id':'desk-oak','quantity':1}]])
def test_invalid_sku_stock_quantity_or_duplicates_are_rejected(items):
    assert client.post('/api/quote',json=items).status_code==422

def test_paid_agent_disabled_by_default(monkeypatch):
    monkeypatch.delenv('ENABLE_CODEX',raising=False)
    assert client.post('/api/ask',json={'message':'Подберите мебель'}).status_code==503

def test_busy_agent_does_not_start_second_process(monkeypatch):
    monkeypatch.setenv('ENABLE_CODEX','1')
    service.LOCK.acquire()
    try: assert client.post('/api/ask',json={'message':'Подберите мебель'}).status_code==429
    finally: service.LOCK.release()
