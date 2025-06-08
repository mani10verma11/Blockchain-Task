import hashlib, time

class Block:
    def __init__(self, data, previous_hash=''):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = ''

    def calculate_hash(self):
        raw = f'{self.timestamp}{self.data}{self.previous_hash}{self.nonce}'
        return hashlib.sha256(raw.encode()).hexdigest()

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        start = time.time()
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(prefix):
                break
            self.nonce += 1
        end = time.time()
        print(f"Block mined with nonce {self.nonce} in {end - start:.4f} seconds. Hash: {self.hash}")

# Example
difficulty = 4
block = Block("Mining simulation data")
block.mine_block(difficulty)
