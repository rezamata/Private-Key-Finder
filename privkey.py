import hashlib

# Define the start and end of the range (as integers)
start = int("100000000000000000")
end = int("1ffffffffffffffffff")

# The target Hash160 to find
target_hash = ""  # Replace this with your actual target hash

# Iterate through the private key range
for key in range(start, end + 1):
    # Convert the key to a 64-character hexadecimal string with leading zeros
    key_hex = hex(key)[2:].zfill(64)
    print(f"Checking key: {key_hex}")

    # Perform SHA-256 hashing
    sha256_hash = hashlib.sha256(key_hex.encode()).digest()

    # Perform RIPEMD-160 hashing on the SHA-256 result (Hash160)
    hash160 = hashlib.new('ripemd160', sha256_hash).hexdigest()

    # Check if the generated Hash160 matches the target
    if hash160 == target_hash:
        print(f"Match found! Private key: {key_hex}")
        break
else:
    print("No match found in the range.")
