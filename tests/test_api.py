import pytest
import ner_app


@pytest.fixture
def client():
    """
    Pytest fixture to generate a flask text client
    :return: Flask client
    """

    app = ner_app.create_ner_app()
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


def test_empty_text(client):
    """Test case for empty text"""

    rv = client.post(
        "/",
        data=dict(
            text="",
        ),
        follow_redirects=True,
    )
    assert "400" in rv.status
    print(rv.data)  # the raw json data
    assert rv.headers["Content-Type"] == "application/json"
    resp = rv.json
    assert resp["Error"] == "empty text"


def test_no_companies(client):
    """Test case for invalid text/ text with no companies"""

    rv = client.post(
        "/",
        data=dict(
            text="no real names here",
        ),
        follow_redirects=True,
    )
    assert "400" in rv.status
    print(rv.data)  # the raw json data
    assert rv.headers["Content-Type"] == "application/json"
    resp = rv.json
    assert resp["Error"] == "no companies found"


def test_longlines_nowrap(client):
    """Test case for long un-wrapped lines - Edge case"""

    # text with 9 company names
    test_text = """
    Contrary to what one might expect, most companies in this industry are small. This is because, although the product may be complicated, only a small investment is needed to fund the manufacture of many types of electronic components, especially in the software segment of this industry. However, these small companies are often bought by big revenue earners once they develop a hit product. Among computer hardware producers, the top names are Hitachi and Hewlett-Packard. Dell has been known for its direct-sale marketing strategy, yet in the rough times for PC’s of late has seen a considerable decline. The smaller companies that are not bought up must focus on differentiating their products and developing the brand name to compete with the diverse portfolios of the big companies.
    As for software companies, Microsoft Corp., IBM, Google and Oracle Corp. rule the roost. These companies should not sit too easily though since recently consumer electronics products have been merging with products from the computer industry, for example phones now have Internet capability, as do game consoles, PDAs, and many other items. This convergence means that companies can expect increased competition from industries who were not previously direct competitors. Companies, such as Apple, have grown to be giants in their own right by offering both hardware and software. This business model has led other companies that have traditionally focused exclusively on software to also enter the hardware production industry.
    """
    rv = client.post(
        "/",
        data=dict(
            text=test_text,
        ),
        follow_redirects=True,
    )
    assert rv.status == "200 OK"
    print(rv.data)
    assert rv.headers["Content-Type"] == "application/json"
    resp = rv.json
    assert len(resp) == 9


def test_wrapped_lines(client):
    """Test case for multiple wrapped lines - Edge case"""

    # text with 9 company names
    test_text = """
    Contrary to what one might expect, most companies in this industry are small. 
    This is because, although the product may be complicated, only a small investment 
    is needed to fund the manufacture of many types of electronic components, especially 
    in the software segment of this industry. However, these small companies are often 
    bought by big revenue earners once they develop a hit product. Among computer hardware 
    producers, the top names are Hitachi and Hewlett-Packard. Dell has been 
    known for its direct-sale marketing strategy, yet in the rough times for PC’s of late 
    has seen a considerable decline. The smaller companies that are not bought up must 
    focus on differentiating their products and developing the brand name to compete with 
    the diverse portfolios of the big companies.
    As for software companies, Microsoft Corp., IBM, Google and Oracle Corp. rule 
    the roost. These companies should not sit too easily though since recently consumer electronics 
    products have been merging with products from the computer industry, for example phones now have 
    Internet capability, as do game consoles, PDAs, and many other items. This convergence means that 
    companies can expect increased competition from industries who were not previously direct competitors. 
    Companies, such as Apple, have grown to be giants in their own right by offering both hardware and 
    software. This business model has led other companies that have traditionally focused exclusively on 
    software to also enter the hardware production industry.
    """
    rv = client.post(
        "/",
        data=dict(
            text=test_text,
        ),
        follow_redirects=True,
    )
    assert rv.status == "200 OK"
    print(rv.data)  # the raw json data
    assert rv.headers["Content-Type"] == "application/json"
    resp = rv.json
    assert len(resp) == 9
