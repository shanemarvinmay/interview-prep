import pytest

from tiny_url_solution import Codec

# I did this just to refresh on fixtures.
@pytest.fixture
def codec():
    return Codec()

@pytest.fixture
def example_url():
    return 'https://example-url.com/extension'

def test_Codec_encode_encoded_url_shorter(codec, example_url):
    encoded_url = codec.encode(example_url)
    assert len(encoded_url) < len(example_url)


@pytest.mark.parametrize('url', ['exmple.com', 'https://example-url.com/extension'])
def test_Codec_encode_decoded_url_matches(url):
    codec = Codec()

    encoded_url = codec.encode(url)
    decoded_url = codec.decode(encoded_url)

    assert decoded_url == url
