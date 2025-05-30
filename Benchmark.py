import time
import random
import zlib
import sys

# -- HRC-Cipher (Caesar shift + Compression) --
def hrc_cipher_encrypt(text):
    start = time.time()
    reversed_text = ' '.join(word[::-1] for word in text.split())
    key = random.randint(1, 96)  # Caesar key in range 1–96
    shifted = ''.join(chr((ord(c) + key) % 256) for c in reversed_text)
    full_data = shifted + chr(key)  # Append key as character
    compressed = zlib.compress(full_data.encode())
    end = time.time()
    return {
        'ciphertext': compressed,
        'exec_time_ms': (end - start) * 1000,
        'output_bits': len(compressed) * 8,
        'memory_kb': sys.getsizeof(compressed) / 1024
    }

# -- XOR Cipher --
def xor_cipher_encrypt(text, key=42):
    start = time.time()
    encrypted = ''.join(chr(ord(c) ^ key) for c in text)
    end = time.time()
    return {
        'ciphertext': encrypted,
        'exec_time_ms': (end - start) * 1000,
        'output_bits': len(encrypted) * 8,
        'memory_kb': sys.getsizeof(encrypted) / 1024
    }

# -- TEA (Simulated) --
def tea_encrypt(text):
    start = time.time()
    time.sleep(0.0015)
    end = time.time()
    size = len(text)
    return {
        'ciphertext': 'tea' * size,
        'exec_time_ms': (end - start) * 1000,
        'output_bits': size * 8,
        'memory_kb': size * 2
    }

# -- PRESENT (Simulated) --
def present_encrypt(text):
    start = time.time()
    time.sleep(0.002)
    end = time.time()
    size = len(text)
    return {
        'ciphertext': 'prs' * size,
        'exec_time_ms': (end - start) * 1000,
        'output_bits': size * 8,
        'memory_kb': size * 2.5
    }

# -- Comparison Display --
def compare_all(text):
    input_bits = len(text) * 8
    print(f"\n🔐 Input Text: \"{text}\"")
    print(f"📏 Input Bits: {input_bits} bits\n")

    results = {
        'HRC-Cipher': hrc_cipher_encrypt(text),
        'XOR': xor_cipher_encrypt(text),
        'TEA': tea_encrypt(text),
        'PRESENT': present_encrypt(text),
    }

    print(f"{'Cipher':<12} | {'Input Bits':<11} | {'Output Bits':<13} | {'Time (ms)':<10} | {'Memory (KB)':<12}")
    print("-" * 75)
    for name, data in results.items():
        print(f"{name:<12} | {input_bits:<11} | {data['output_bits']:<13} | {data['exec_time_ms']:<10.2f} | {data['memory_kb']:<12.2f}")

# -- Main Execution --
if __name__ == "__main__":
    user_text = input("Enter text to encrypt: ")
    compare_all(user_text)
