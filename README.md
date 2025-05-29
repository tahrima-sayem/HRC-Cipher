# HRC-Cipher

**A Hybrid Lightweight Text Encryption Scheme Based on Reversal, Caesar Cipher, and Compression**

---

## Overview

**HRC-Cipher** is a lightweight symmetric encryption algorithm tailored for encrypting **short text messages**. It integrates three core techniques:

- Word-level reversal
- Caesar cipher using ASCII-based byte shifting
- Lossless compression (Huffman coding)

The algorithm is ideal for:
- Educational cryptography
- Embedded systems or constrained environments
- Lightweight private communication

---

## How It Works

The encryption process consists of the following stages:

1. **Tokenization**: The input text is split into words.
2. **Reversal**: Each word is reversed to add obfuscation.
3. **Caesar Cipher**: A random key \( k \in [1,10] \) is chosen and applied via ASCII Caesar cipher.
4. **Key Hint**: The Caesar key is encoded (1 → 'a', ..., 10 → 'j') and appended to the encrypted string.
5. **Compression**: Huffman encoding is used to compress the ciphertext.

### Decryption

The process is reversed:
- Decompress
- Extract and decode the key hint
- Apply inverse Caesar cipher
- Reverse words to recover original text

---

## Repository Structure

```
HRC-Cipher/
├── HRC.py              # Main encryption and decryption logic
├── Pipeline.png        # Flow diagram
└── README.md           # This documentation
```

---

## Getting Started

### Requirements

- Python 3.x
- No external libraries needed (`random`, `heapq`, `collections` are standard)

### Example Usage

```python
from hrc_cipher import encrypt_pipeline, decrypt_pipeline

# Input message to encrypt
plaintext = "Hello, this is a secure message!"

# Encrypt the message
result = encrypt_pipeline(plaintext)
print("Encrypted Output:", result["compressed"])

# Decrypt the message
decrypted = decrypt_pipeline(result["compressed"], result["tree"])
print("Decrypted Output:", decrypted["plaintext"])

---

## Sample Performance

| Input Length | Compressed Bits | Compression Ratio | Time (ms) |
|--------------|------------------|--------------------|-----------|
| 50 chars     | 220              | 0.55               | 0.12      |
| 100 chars    | 430              | 0.54               | 0.15      |

---

## Paper & Credits

This code supports the following extended abstract:

**HRC-Cipher: A Hybrid Lightweight Text Encryption Scheme Based on Reversal, Caesar Cipher, and Compression for Short Messages**  
*IEEE Computer Society Bangladesh Chapter Symposium (BDC Symposium) 2025 — Submitted*  
Author: Tahrima Sayem Sowa

---

## Online Demo / Code Access

- GitHub Repository: [https://github.com/tahrima-sayem/HRC-Cipher/blob/main/HCR.py](https://github.com/tahrima-sayem/HRC-Cipher/blob/main/HCR.py)
- Flow Diagram: Available in `Pipeline.png`

---

## Contact

For questions, suggestions, or collaboration:  
Email: tahrimasowa@gmail.com
