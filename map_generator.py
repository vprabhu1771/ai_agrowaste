import folium
import json
import webbrowser

def show_nearby_ngos(waste_type):
    with open('data/ngos.json', 'r', encoding='utf-8') as f:
        ngos = json.load(f)

    # Center map at a default rural location
    m = folium.Map(location=[10.7905, 78.7047], zoom_start=7)

    for ngo in ngos:
        if waste_type in ngo["accepted_waste"]:
            folium.Marker(
                location=[ngo["lat"], ngo["lon"]],
                popup=f"{ngo['name']} ({ngo['contact']})",
                icon=folium.Icon(color='green')
            ).add_to(m)

    m.save("ngo_map.html")
    webbrowser.open("ngo_map.html")
