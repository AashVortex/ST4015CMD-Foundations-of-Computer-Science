# Import the required module
from urllib.parse import quote, unquote

# Original string to encode
original_string = "Hello World! This is a test: 100% safe."

# URL encode the string
encoded_string = quote(original_string)
print("Encoded URL:", encoded_string)

# URL decode the string back to original
decoded_string = unquote(encoded_string)
print("Decoded URL:", decoded_string)