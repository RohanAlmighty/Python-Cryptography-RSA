from gen_key import gen_private_key, gen_public_key
from crypt_key import encrypt, decrypt
from read_write_key import (
    read_key_private,
    read_key_public,
    write_key_private,
    write_key_public,
)

if __name__ == "__main__":
    private_key = gen_private_key()
    public_key = gen_public_key(private_key)

    write_key_private(private_key, private_key_file="private_key.pem")
    write_key_public(public_key, public_key_file="public_key.pem")

    private_key = read_key_private(private_key_file="private_key.pem")
    public_key = read_key_public(public_key_file="public_key.pem")

    original_message = str(input("Input Text: "))
    print(original_message)

    encrypted_message = encrypt(public_key, original_message)
    print(encrypted_message)

    original_message = decrypt(private_key, encrypted_message)
    print(original_message)
