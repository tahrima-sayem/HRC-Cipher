import random                
import heapq                 
import time                  
from collections import Counter  

# ---------- Caesar Cipher ----------
def ascii_caesar_encrypt(text, key):
    return ''.join(chr((ord(char) + key) % 256) for char in text)               # Encrypts text using Caesar cipher by shifting ASCII values

def ascii_caesar_decrypt(text, key):
    return ''.join(chr((ord(char) - key) % 256) for char in text)               # Decrypts text encrypted by Caesar cipher

# ---------- Word Reversal ----------
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split())                        # Reverses each word in the input text individually

# ---------- Key Mapping ----------
def key_to_char(key):
    return chr(96 + key)                                                        # Converts integer key (1–10) to a single lowercase letter (a–j)

def char_to_key(char):
    return ord(char) - 96                                                       # Converts key character (a–j) back to integer (1–10)

# ---------- Huffman Coding ----------
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None                                                        
        self.right = None                                                       

    def __lt__(self, other):
        return self.freq < other.freq                                           # Defines comparison for priority queue (min-heap)

def build_huffman_tree(text):                                                   # Builds a Huffman tree based on character frequency
    freq = Counter(text)                                                        
    heap = [HuffmanNode(ch, fr) for ch, fr in freq.items()]                     
    heapq.heapify(heap)                                                         

    while len(heap) > 1:                                                        
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]                                                             

def build_huffman_codes(root):
    codes = {}                                                                  # Recursively builds Huffman codes from tree

    def build_codes_rec(node, current_code):
        if node:
            if node.char is not None:
                codes[node.char] = current_code  
            build_codes_rec(node.left, current_code + '0')
            build_codes_rec(node.right, current_code + '1')

    build_codes_rec(root, '')
    return codes

def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)                                # Encodes input text using Huffman codes

def huffman_decode(encoded_text, root):                                         # Decodes Huffman-encoded text using the tree
    decoded = ''
    node = root
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded += node.char
            node = root
    return decoded

# ---------- Encryption Pipeline ----------
def encrypt_pipeline(plaintext):
    start = time.time() 

    reversed_text = reverse_words(plaintext)                                    # Step 1: Reverse each word
    key = random.randint(1, 10)                                                 # Step 2: Random key (1–10)
    caesar_text = ascii_caesar_encrypt(reversed_text, key)                      # Step 3: Caesar encrypt
    key_char = key_to_char(key)                                                 # Step 4: Convert key to letter
    cipher_with_key = caesar_text + key_char                                    # Step 5: Append key letter

    tree = build_huffman_tree(cipher_with_key)                                  # Step 6: Build Huffman tree
    codes = build_huffman_codes(tree)                                           # Step 7: Generate Huffman codes
    compressed = huffman_encode(cipher_with_key, codes)                         # Step 8: Huffman encode

    end = time.time()

    return {
        "compressed": compressed,
        "tree": tree,
        "key": key,
        "key_char": key_char,
        "original": plaintext,
        "reversed": reversed_text,
        "caesar": caesar_text,
        "cipher_with_key": cipher_with_key,
        "compression_ratio": len(compressed) / (len(cipher_with_key) * 8),
        "execution_time_ms": (end - start) * 1000
    }

# ---------- Decryption Pipeline ----------
def decrypt_pipeline(compressed, tree):
    decompressed = huffman_decode(compressed, tree)                             # Step 1: Huffman decode
    key_char = decompressed[-1]                                                 # Step 2: Extract key char
    key = char_to_key(key_char)                                                 # Step 3: Convert to int
    caesar_only = decompressed[:-1]                                             # Step 4: Remove key char
    decrypted_caesar = ascii_caesar_decrypt(caesar_only, key)                   # Step 5: Caesar decrypt
    final_plaintext = reverse_words(decrypted_caesar)                           # Step 6: Reverse back

    return {
        "compressed": compressed,
        "decompressed": decompressed,
        "key_char": key_char,
        "key": key,
        "decrypted_caesar": decrypted_caesar,
        "plaintext": final_plaintext
    }

# ---------- Main Program ----------
def main():
    user_input = input("Enter text to encrypt: ")                               # Ask user for input
    enc = encrypt_pipeline(user_input)                                          # Run encryption pipeline

    print("\n--- 🔐 ENCRYPTION OUTPUT ---")
    print("Original Text:         ", enc["original"])
    print("Reversed Words:        ", enc["reversed"])
    print("Caesar Encrypted:      ", enc["caesar"])
    print("Key Used:              ", enc["key"])
    print("Key Char:              ", enc["key_char"])
    print("Cipher + Key:          ", enc["cipher_with_key"])
    print("Huffman Compressed:    ", enc["compressed"][:80] + "...")
    print(f"Compression Ratio:      {enc['compression_ratio']:.4f}")
    print(f"Execution Time:         {enc['execution_time_ms']:.2f} ms")

    dec = decrypt_pipeline(enc["compressed"], enc["tree"])                      # Run decryption

    print("\n--- 🔓 DECRYPTION OUTPUT ---")
    print("Compressed ciphertext: ", dec["compressed"][:80] + "...")
    print("Decompressed text:     ", dec["decompressed"])
    print("Extracted Key Char:    ", dec["key_char"])
    print("Extracted Key:         ", dec["key"])
    print("Decrypted Caesar Text: ", dec["decrypted_caesar"])
    print("Plaintext:             ", dec["plaintext"])

# Main program
if __name__ == "__main__":
    main()
