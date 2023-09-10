from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


def gen_private_key(public_exponent=65537, key_size=2048):
    private_key = rsa.generate_private_key(
        public_exponent=public_exponent, key_size=key_size, backend=default_backend()
    )
    return private_key


def gen_public_key(private_key):
    public_key = private_key.public_key()
    return public_key
