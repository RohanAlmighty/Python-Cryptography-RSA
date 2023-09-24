from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey


def gen_private_key(
    public_exponent: int = 65537, key_size: int = 2048
) -> RSAPrivateKey:
    private_key = rsa.generate_private_key(
        public_exponent=public_exponent, key_size=key_size, backend=default_backend()
    )
    return private_key


def gen_public_key(private_key: RSAPrivateKey) -> RSAPublicKey:
    public_key = private_key.public_key()
    return public_key
