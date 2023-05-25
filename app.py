from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_static_html():
    # Serve the static HTML file from the 'static' folder
    return send_from_directory('the-internet-of-production-alliance-files', 'open-know-where-2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)