from flask import Flask, render_template, request
import folium

app = Flask(__name__)


@app.route('/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)


@app.route('/')
def serve_index():
    return app.send_static_file('open-know-where-2.html')


@app.route('/geo')
def generate_map():
    # Extract parameters from the URL
    country = request.args.get('country')
    region = request.args.get('region')
    #Americas Africa Europe Asia MENA
    source = request.args.get('source')
    machines = request.args.get('machines')
    people = request.args.get('people')
    # makers, researchers, startups, gig
    facilities = request.args.get('facilities')
    project = request.args.get('project')
    #GIG IMA MAKE DATA AWARDS

    # Generate the Folium map based on the parameters
    # Customize the map creation code according to your requirements
    # Here's a simple example that generates a basic map
    m = folium.Map(location=[0, 0], zoom_start=2)
    folium.Marker([0, 0], popup=country).add_to(m)

    # Get the HTML string of the map
    map_html = m.get_root().render()

    # Render the map HTML template with the map_html as context
    return render_template('map.html', map_html=map_html)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)