'''This is my solution to Leetcode #535.

I'm basically just goofing off here. This isn't an good solution.'''
class Codec:

    def __init__(self):
        self.prefix = 'http://tinyurl.com'
        # Encoded url to url
        self.encoded_url_for_url = dict()
    
    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        decimal_hash = hash(long_url)
        hex_hash = hex(decimal_hash)
        encoded_url = f'{self.prefix}/{hex_hash[3:5]}'
        self.encoded_url_for_url[encoded_url] = long_url
        return encoded_url    

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.encoded_url_for_url[short_url]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
