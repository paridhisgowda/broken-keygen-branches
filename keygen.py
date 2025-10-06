import base64
# WARNING: Using a placeholder salt for testing. DO NOT PUSH TO PROD.
TEST_SALT = "INVALID_SALT_v1" 
BASE_STRING = "FLAGG1T_"

def generate_key_fragment_broken():
    # Final encoding using the wrong salt produces an invalid key
    data_to_encode = (BASE_STRING + TEST_SALT).encode('utf-8')
    return base64.b64encode(data_to_encode).decode('utf-8')

if __name__ == "__main__":
    print(generate_key_fragment_broken())