from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey, RSAPrivateKey


def encrypt(public_key: RSAPublicKey, original_message: str) -> bytes:
    bytes_message = bytes(original_message, "utf-8")
    encrypted_message = public_key.encrypt(
        bytes_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return encrypted_message


def decrypt(private_key: RSAPrivateKey, encrypted_message: bytes) -> str:
    bytes_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    original_message = str(bytes_message, "utf-8")
    return original_message
