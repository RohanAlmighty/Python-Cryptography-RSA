from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def encrypt(public_key, original_message):
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


def decrypt(private_key, encrypted_message):
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
