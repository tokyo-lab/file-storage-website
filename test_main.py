from urlshort import create_app

# look for word 'Shorten' in homepage


def test_shorten(client):
    response = client.get("/")
    assert b"Shorten" in response.data
