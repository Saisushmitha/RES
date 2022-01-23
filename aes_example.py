import pyaes, pbkdf2, binascii, os, secrets

# Decryption Key Set
iv = enter_initialization_vector
key = binascii.unhexlify('enter_key')
encryptedtext = binascii.unhexlify("enter_encrypted_text")

# Encryption Key Set
# plaintext = "Enter plain text here"


# Encrypt the plaintext with the given key:
# ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
# ----------------------------------------------------
# aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
# ciphertext = aes.encrypt(plaintext)
# print('Encrypted:', binascii.hexlify(ciphertext))


# Decrypt the ciphertext with the given key:
# plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)
# ----------------------------------------------------
# aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
# decrypted = aes.decrypt(encryptedtext)
# print('Decrypted:', decrypted)