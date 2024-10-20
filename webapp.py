from flask import Flask, request, jsonify, render_template
import database

# Create app and init database
app = Flask(__name__, static_folder='static', template_folder='templates')

# Define methods
@app.route('/search', methods=['GET'])
def search():
    print('GET /search')

    query = request.args.get('query')
    print(f"Query is '{query}'")

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # TODO: make database to
    similar_games = database.get_alike_by_name(query)
    result = []

    if len(similar_games) > 0:
        for game in similar_games:
            result.append({
                'game_name': game[0],
                'store_name': game[1],
                'price': game[2],
                'last_updated': game[3].isoformat()
            })

    return jsonify(success=True, result=result), 200

@app.route('/item/<string:item_name>')
def item(item_id):
    result = database.get_by_name(item_name)
    if result:
        return render_template('item.html', item=result)
    return "Item not found", 404

@app.route('/')
def index():
    return render_template('index.html')

# Start the app
app.run(debug=True)
