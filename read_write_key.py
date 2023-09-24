from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey


def read_key_private(private_key_file: str = "private_key.pem") -> RSAPrivateKey:
    with open(private_key_file, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=None, backend=default_backend()
        )
    return private_key


def read_key_public(public_key_file: str = "public_key.pem") -> RSAPublicKey:
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(), backend=default_backend()
        )
    return public_key


def write_key_private(
    private_key: RSAPrivateKey, private_key_file: str = "private_key.pem"
) -> None:
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    with open(private_key_file, "wb") as f:
        f.write(pem)


def write_key_public(
    public_key: RSAPublicKey, public_key_file: str = "public_key.pem"
) -> None:
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    with open(public_key_file, "wb") as f:
        f.write(pem)
