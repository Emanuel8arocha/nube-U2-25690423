import requests, time

t0 = time.perf_counter()
r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu", timeout=10)
ms = (time.perf_counter() - t0) * 1000
r.raise_for_status()

datos = r.json()
habilidades = [a["ability"]["name"] for a in datos["abilities"]]

print(r.status_code, f"{ms:.0f} ms", len(r.content), "bytes")
print("Nombre:", datos["name"])
print("Altura:", datos["height"])
print("Habilidades:", habilidades)
