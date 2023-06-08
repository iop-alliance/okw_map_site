import pandas as pd
from folium import DivIcon, Marker


class People:
    def __init__(self, data: object) -> object:
        self.data = data

    with open('dev/cluster_icon_cr.js') as file:
        cluster_icon = file.read()


class Machinery:
    def __init__(self, data: object) -> object:
        self.data = data

    with open('dev/cluster_icon_tr.js') as file:
        cluster_icon = file.read()

    def single_icon(self, location, popup, _color):
        icon_size = "20"  # Adjust the size of the icon as needed
        icon_html = """
        <svg height="{size}" width="{size}" viewBox="0 0 {size} {size}">
            <polygon points="0,0 {half_size},{size} {size},0" style="fill: {color};  fill-opacity: 0.4;"></polygon>
        </svg>
        """.format(
            size=icon_size, half_size=int(icon_size) // 2, color=_color
        )
        icon = DivIcon(html=icon_html)
        marker = Marker(location=location, icon=icon, popup=popup)
        return marker



class Facilities:
    def __init__(self, data: object) -> object:
        self.data = data

    with open('dev/cluster_icon_sq.js') as file:
        cluster_icon = file.read()

    def single_icon(self, location, popup, _color):
        icon_size = "20"  # Adjust the size of the icon as needed
        icon_html = """
        <svg height="{size}" width="{size}" viewBox="0 0 {size} {size}">
            <rect x="0" y="0" width="{size}" height="{size}" style="fill: {color}; fill-opacity: 0.4;"></rect>
        </svg>
        """.format(
            size=icon_size, color=_color
        )
        icon = DivIcon(html=icon_html)
        marker = Marker(location=location, icon=icon, popup=popup)
        return marker


class Regions:
    def __init__(self):
        pass


class Fablabs:
    color = '#0000FF'
    def __init__(self):
        self.facilities = Facilities(pd.read_csv("dev/fablabs.csv", encoding="latin-1")
                                     .drop(columns=["Unnamed: 0", "address_notes"])
                                     .dropna(subset=["latitude", "longitude"]))

        self.machines = Machinery(pd.read_csv("dev/geomachines.csv")
            .drop(columns=["city", "county", "Unnamed: 0"])
            .dropna(subset=["latitude", "longitude"])
        )


class Gig:
    color = '#FF0000'
    def __init__(self):
        self.people = People(pd.read_csv("dev/gig_people.csv", encoding="latin-1"))

