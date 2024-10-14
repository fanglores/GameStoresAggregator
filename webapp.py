from flask import Flask, request, jsonify

# Create app and init database
app = Flask(__name__)

# Define methods
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    raise NotImplementedError

    return None


