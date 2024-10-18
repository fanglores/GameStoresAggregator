from flask import Flask, request, jsonify
import database

# Create app and init database
app = Flask(__name__)

# Define methods
@app.route('/search', methods=['GET'])
def search():
    print('GET /search')

    query = request.args.get('query')
    print(f'Query is {query}')

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    similar_games = database.get_alike_by_name(query)

    if len(similar_games) == 0:
        print('error')
        return jsonify({"error": "Database response is empty"}), 400

    result_list = []
    for game in similar_games:
        result_list.append({
            'game_name': game[0],
            'store_name': game[1],
            'price': game[2],
            'last_updated': game[3].isoformat()
        })

    return jsonify(result_list), 200

# Start the app
app.run(debug=True)
