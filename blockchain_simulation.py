import hashlib, time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        raw = f'{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}'
        return hashlib.sha256(raw.encode()).hexdigest()

# Chain setup
genesis_block = Block(0, time.time(), "Genesis Block", "0")
block1 = Block(1, time.time(), "Second Block", genesis_block.hash)
block2 = Block(2, time.time(), "Third Block", block1.hash)

# Display chain
for block in [genesis_block, block1, block2]:
    print(f'Index: {block.index} | Hash: {block.hash[:10]}... | Prev: {block.previous_hash[:10]}...')

# Tampering
print("\nTampering Block 1's data...")
block1.data = "Hacked Data"
block1.hash = block1.calculate_hash()

# Chain validity check
print("\nAfter tampering:")
for block in [genesis_block, block1, block2]:
    print(f'Index: {block.index} | Hash: {block.hash[:10]}... | Prev: {block.previous_hash[:10]}...')
