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

![HRC-Cipher Flow Diagram](./Pipeline.png)
<p align="center">
  Figure - Block Diagram Of the System
</p>

### Encryption

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
```

---

## Sample Performance

### Sample output

**Original Text:**       Hello! This is Tahrima.<br>
**Reversed Words:**      !olleH sihT si .amirhaT<br>
**Caesar Encrypted:**    |ÊÇÇÀ£{ÎÄÃ¯{ÎÄ{¼ÈÄÍÃ¼¯<br>
**Key Used:**            91<br>
**Key Char:**            »<br>
**Cipher + Key:**        |ÊÇÇÀ£{ÎÄÃ¯{ÎÄ{¼ÈÄÍÃ¼¯»<br>
**Huffman Compressed:**  00101101010101010110111110101111111000100000111111100011111001100001110010111010...<br>
**Compression Ratio:**   0.4792<br>
**Execution Time:**      0.08 ms<br>
**Decrypted Text:**       Hello! This is Tahrima.<br>

### Performance Table for different length of sample

| Input Length | Compressed Bits | Compressed Bits | Compression Ratio | Time (ms) |
|--------------|------------------|------------------|--------------------|-----------|
| 30 chars     | 240              | 111              | 0.46               | 0.08      |
| 63 chars     | 512              | 263              | 0.51               | 0.10      |
| 85 chars     | 680              | 366              | 0.53               | 0.26      |
| 110 chars    | 880              | 461              | 0.54               | 0.28      |
| 176 chars    | 1408             | 718              | 0.51               | 0.20      |
| 394 chars    | 3152             | 1665             | 0.53               | 0.19      |
| 690 chars    | 5520             | 2955             | 0.54               | 0.28      |

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
