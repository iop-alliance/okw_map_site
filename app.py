from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

@app.route('/')
def serve_index():
    return app.send_static_file('open-know-where-2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)