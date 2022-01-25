from flask import Flask, jsonify
from blockchain import Blockchain
# Mining our Blockchain
# Creating a Web App
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Create a Blockchain
blockchain = Blockchain()
print(blockchain)
# Mining a new block


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just minded a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Getting the full Blockchain


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Running the app
app.run(host = '0.0.0.0', port = 5000)