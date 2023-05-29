import requests
from geopy.distance import geodesic

# Mengambil data peluncuran terakhir dari API SpaceX
response = requests.get("https://api.spacexdata.com/v4/launches")
latest_launches = response.json()

# Mengurutkan peluncuran terbaru berdasarkan tanggal
latest_launches.sort(key=lambda x: x["date_utc"], reverse=True)

# Mengambil 20 peluncuran terakhir
recent_launches = latest_launches[:20]

# Mengambil data launchpad dari API SpaceX
response = requests.get("https://api.spacexdata.com/v4/launchpads")
launchpads = response.json()

# Loop melalui 20 peluncuran terakhir
for launch in recent_launches:
    launchpad_id = launch["launchpad"]
    launch_date = launch["date_utc"]

    # Temukan nama lengkap dan koordinat launchpad
    launchpad_name = ""
    launchpad_latitude = ""
    launchpad_longitude = ""
    for launchpad in launchpads:
        if launchpad["id"] == launchpad_id:
            launchpad_name = launchpad["full_name"]
            launchpad_latitude = launchpad["latitude"]
            launchpad_longitude = launchpad["longitude"]
            break

    # Meneruskan nama lengkap ke API geocoding Mapbox
    mapbox_api_key = "pk.eyJ1IjoibGluY3hsbiIsImEiOiJjbDluMHppMjIwMTR5NDBtejl3NjNueGdyIn0.DLAhnub2hn2okIq0gwCJEw"
    geocoding_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{launchpad_name}.json?access_token={mapbox_api_key}"
    response = requests.get(geocoding_url)
    data = response.json()

    # Mendapatkan garis bujur dan lintang dari hasil geocoding Mapbox
    if data["features"]:
        place_name = data["features"][0]["place_name"]
        place_latitude = data["features"][0]["center"][1]
        place_longitude = data["features"][0]["center"][0]

        # Menghitung jarak dalam kilometer antara koordinat launchpad
        # dan koordinat hasil geocoding Mapbox
        launchpad_coords = (launchpad_latitude, launchpad_longitude)
        place_coords = (place_latitude, place_longitude)
        distance_km = geodesic(launchpad_coords, place_coords).kilometers

        print("Tanggal Peluncuran:", launch_date)
        print("Nama Lengkap Launchpad:", launchpad_name)
        print("Perbedaan Jarak (km):", distance_km)
        print("-------------------------------------")
    else:
        print(f"Tidak dapat menemukan hasil geocoding untuk {launchpad_name}.")
