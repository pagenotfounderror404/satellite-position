import requests

position=requests.get(url="http://api.open-notify.org/iss-now.json")
print(position.status_code)
position.raise_for_status()

data=position.json()["iss_position"]
longitude=data["longitude"]
latitude=data["latitude"]
exact_position=(longitude,latitude)
print(exact_position)