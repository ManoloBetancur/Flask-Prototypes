import asyncio
from flask import Flask, render_template, jsonify

app = Flask(__name__)

data_list = [1, 2, 3, 4, 5]  # Replace with your list of IDs

async def async_data_lookup():
    while data_list:
        id = data_list.pop(0)
        # Simulate a 3-second data lookup (replace this with your actual async operation)
        await asyncio.sleep(3)
        yield {'id': id, 'value': f'Data for ID {id}'}

@app.route('/fetch_data')
async def fetch_data():
    async for data in async_data_lookup():
        return jsonify(data)
    return jsonify(None)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
