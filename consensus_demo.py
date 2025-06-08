import random

# PoW simulation
miners = [{'id': 'Miner1', 'power': random.randint(10, 100)},
          {'id': 'Miner2', 'power': random.randint(10, 100)}]
pow_winner = max(miners, key=lambda m: m['power'])

# PoS simulation
stakers = [{'id': 'Staker1', 'stake': random.randint(1, 100)},
           {'id': 'Staker2', 'stake': random.randint(1, 100)}]
pos_winner = max(stakers, key=lambda s: s['stake'])

# DPoS simulation
delegates = ['Delegate1', 'Delegate2', 'Delegate3']
votes = {'Delegate1': 1, 'Delegate2': 2, 'Delegate3': 0}
dpos_winner = max(votes, key=votes.get)

# Output
print(f"[PoW] Winner: {pow_winner['id']} with power {pow_winner['power']}")
print(f"[PoS] Winner: {pos_winner['id']} with stake {pos_winner['stake']}")
print(f"[DPoS] Winner: {dpos_winner} with {votes[dpos_winner]} votes")

