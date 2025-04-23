from integrations.thehive_client import TheHiveClient

def test_create_alert():
    client = TheHiveClient("http://localhost:9000", "fakekey")
    assert hasattr(client, "create_alert")
