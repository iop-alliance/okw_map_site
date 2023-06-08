# import pandas as pd
import folium
from folium.plugins import (
    # HeatMap,
    FloatImage,
    LocateControl,
    MarkerCluster,
)
import json
# from dev_libs.js_handler import create_cluster_icon_sq, create_cluster_icon_tr, create_cluster_icon_cr
from dev_libs.data_handler import Fablabs, Gig


# In[2]:


class MapGenerator():
    colors = [
        "#7F3C8D",
        "#11A579",
        "#3969AC",
        "#F2B701",
        "#E73F74",
        "#80BA5A",
        "#E68310",
        "#008695",
        "#CF1C90",
        "#f97b72",
        "#4b4b8f",
        "#A5AA99",
    ]

    layers = {}

    def __int__(self):#, region, country, sources, people, machines, facilities, cross_references):
        self.machines = [Fablabs().machines.data]
        self.people = [Gig().people.data]
        self.facilities = [Fablabs().facilities.data]
        self.map = None
        return True

    def read_data(self, default=True):
        return True

    def map_design(self, style):
        return True


point_max = (Fablabs().machines.data.latitude.max(),  Fablabs().machines.data.longitude.max())
point_min = (Fablabs().machines.data.latitude.min(),  Fablabs().machines.data.longitude.min())

unique_values = Fablabs().machines.data["class_1"].unique()

# create an empty dictionary to store dataframes
machines_bytype = {}
# geojson = {}

# iterate over unique values and create new dataframes
for value in unique_values:
    machines_bytype[value] = Fablabs().machines.data[Fablabs().machines.data["class_1"] == value]

machines_map = folium.Map(
    tiles=None,
    control=False,
    prefer_canvas=True,
    zoom_control=False,
    # minNativezoom=2
)

folium.raster_layers.TileLayer(
    tiles="cartodbpositron",
    # name="Basic",
    control=False,
    minNativezoom=3,
    # max_zoom=14,
    # zoom_start=4,
    # noWrap=True
).add_to(machines_map)


machines_map.fit_bounds((point_min, point_max))


# In[8]:


marker_cluster = MarkerCluster(
    name='<i class="fas fa-caret-down" style="color: #00A676;"></i> Machinery',
    icon_create_function=Fablabs().machines.cluster_icon,
    control=True,
    options={
        "spiderLegPolylineOptions": {"weight": 0.5, "color": "#FFF", "opacity": 0.5}
    },
).add_to(machines_map)


icon = '<i class="fas fa-circle" style="color: {color};"></i>'

for index, (key, data) in enumerate(machines_bytype.items()):

    data.crs = "EPSG:4326"

    group = folium.plugins.FeatureGroupSubGroup(
        marker_cluster,
        icon.format(color=MapGenerator.colors[index]) + " " + key.title().replace("_", " "),
        control=False,
    )

    MapGenerator.layers[key] = group
    # name', 'brand', 'slug', 'class_1', 'edited', 'lab', 'country_code', 'latitude', 'longitude'

    for indx, row in data.iterrows():
        popup = f"""
            <div style="padding: 5px; width: 200px">
                <p><strong>Name:</strong>\t {row['name'].title()}</p>
                <p><strong>Brand:</strong>\t {row['brand'].title()}</p>
                <p><strong>Type:</strong>\t {row['class_1'].title().replace("_", " ")}</p>
                <p><strong>Lab:</strong>\t {row['lab']}</p>
                <p><strong>Build size: </p>
                <img src="https://fablabs.io/assets/logo-78c5ba6a9895eaf5debdd08d9856b62703ebf0658507f6972742505cb1f75a7b.svg" style="max-width: 80px;"/>
            </div>
        """

        marker = Fablabs().machines.single_icon(
            location=[row.latitude, row["longitude"]],
            _color=MapGenerator.colors[index],
            popup=popup,
        )

        marker.add_to(group)
    machines_map.add_child(group)


marker_cluster_o = MarkerCluster(
    name='<i class="fas fa-square" style="color: #470063;"></i> Facilities',
    icon_create_function=Fablabs().facilities.cluster_icon,
    control=True,
    options={
        "spiderLegPolylineOptions": {"weight": 0.5, "color": "#FFF", "opacity": 0.5}
    },
).add_to(machines_map)

for index, row in Fablabs().facilities.data.iterrows():
    popup = f"""
            <div style="padding: 5px; width: 200px">
                <p><strong>Name:</strong>\t {str(row['name']).title()}</p>
                <p><strong>City:</strong>\t {str(row['city']).title()}</p>
                <p><strong>Capabilities:</strong>\t {str(row['capabilities']).title().replace("_", " ")}</p>

                <img src="https://fablabs.io/assets/logo-78c5ba6a9895eaf5debdd08d9856b62703ebf0658507f6972742505cb1f75a7b.svg" style="max-width: 80px;"/>
            </div>
        """

    marker = Fablabs().facilities.single_icon(
        location=[row.latitude, row["longitude"]], _color=MapGenerator.colors[0], popup=popup
    ).add_to(marker_cluster_o)
marker_cluster_o.add_to(machines_map)

logo_url = (
    "https://github.com/kny5/data_reports/raw/main/assets/img/iopa_logo_okw_sm.png"
)
logo_size = (10, 10)
icon = folium.features.CustomIcon(logo_url, icon_size=logo_size)
span = 1
float_image = FloatImage(
    logo_url, bottom=span, left=span, width=logo_size[0], height=logo_size[1]
)
machines_map.add_child(float_image)

loc_ctrl = LocateControl(zindex=50)
machines_map.add_child(loc_ctrl)


cluster = MarkerCluster(
    name='<i class="fas fa-circle" style="color: #EF476F;"></i> People',
    icon_create_function=Gig().people.cluster_icon,
    control=True,
).add_to(machines_map)

for index, data in Gig().people.data.iterrows():

    data["loc_data"] = json.loads(data["loc_data"].replace("'", '"'))

    popup_html = f"""
    <div style="align-items: left;">
        <img src="{data['image']}" alt="{data['name']}" style="width:100%;border-radius:50%;max-width:150px;">
        <h4 style="text-align:center">{data['name']}</h4>
        <p><strong>Location: </strong>{data['location_translated']}</p>
        <p><strong>Initiative: </strong>{str(data['initiative'])[:40]}</p>
        <p><a href="{data['url']}" target="_blank">View Profile</a></p>
    </div>
    """

    popup = folium.Popup(popup_html)
    try:

        marker = folium.CircleMarker(
            location=(float(data["loc_data"]["lat"]), float(data["loc_data"]["lon"])),
            radius=10,
            fill_color="#EA6690",
            opacity=0.4,
            color="#EA6690",
            weight=1,
            popup=popup,
        )
        marker.add_to(cluster)

    except KeyError:
        pass


map_control = folium.LayerControl(collapsed=False, autoZIndex=False)
machines_map.add_child(map_control)

machines_map.save("output/mapof_machines.html")
