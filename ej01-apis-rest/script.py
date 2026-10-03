import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# PUNTO 1: JSONPlaceholder
# ==========================================
print("=== PUNTO 1: JSONPlaceholder ===")

t0 = time.perf_counter()
res_get = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=10)
ms_get = (time.perf_counter() - t0) * 1000

print(f"[GET] Código: {res_get.status_code}")
print(f"[GET] Tiempo: {ms_get:.0f} ms")
print(f"[GET] Tamaño: {len(res_get.content)} bytes")

payload = {"title": "hola", "body": "desde python", "userId": 1}
t0 = time.perf_counter()
res_post = requests.post(
    "https://jsonplaceholder.typicode.com/posts", json=payload, timeout=10
)
ms_post = (time.perf_counter() - t0) * 1000

print(f"[POST] Código: {res_post.status_code}")
print(f"[POST] Tiempo: {ms_post:.0f} ms")
print(f"[POST] Tamaño: {len(res_post.content)} bytes")

# ==========================================
# PUNTO 2: PokéAPI
# ==========================================
print("\n=== PUNTO 2: PokéAPI ===")

t0 = time.perf_counter()
res_poke = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu", timeout=10)
ms_poke = (time.perf_counter() - t0) * 1000

res_poke.raise_for_status()
datos_poke = res_poke.json()

nombre = datos_poke["name"]
altura = datos_poke["height"]
habilidades = [a["ability"]["name"] for a in datos_poke["abilities"]]

print(f"[GET] Código: {res_poke.status_code}")
print(f"[GET] Tiempo: {ms_poke:.0f} ms")
print(f"[GET] Tamaño: {len(res_poke.content)} bytes")
print(f"Nombre: {nombre}")
print(f"Altura: {altura}")
print(f"Habilidades: {habilidades}")

# ==========================================
# PUNTO 3: OpenWeatherMap
# ==========================================
print("\n=== PUNTO 3: OpenWeatherMap ===")

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    print("Error: No se encontró la OPENWEATHER_API_KEY en el archivo .env")
else:
    url_clima = f"https://api.openweathermap.org/data/2.5/weather?q=Ciudad Valles,MX&appid={api_key}&units=metric&lang=es"

    t0 = time.perf_counter()
    res_clima = requests.get(url_clima, timeout=10)
    ms_clima = (time.perf_counter() - t0) * 1000

    print(f"[GET] Código: {res_clima.status_code}")
    print(f"[GET] Tiempo: {ms_clima:.0f} ms")
    print(f"[GET] Tamaño: {len(res_clima.content)} bytes")

    if res_clima.status_code == 200:
        datos_clima = res_clima.json()
        temp = datos_clima["main"]["temp"]
        desc = datos_clima["weather"][0]["description"]
        print(f"Ciudad: {datos_clima['name']}")
        print(f"Temperatura: {temp}°C")
        print(f"Descripción: {desc}")

# ==========================================
# PUNTO 4: Provocar errores (404 y 401)
# ==========================================
print("\n=== PUNTO 4: Provocar errores (404 y 401) ===")

t0 = time.perf_counter()
res_404 = requests.get(
    "https://pokeapi.co/api/v2/pokemon/pokemon-que-no-existe", timeout=10
)
ms_404 = (time.perf_counter() - t0) * 1000

print(f"[404] Código: {res_404.status_code}")
print(f"[404] Tiempo: {ms_404:.0f} ms")
print(f"[404] Tamaño: {len(res_404.content)} bytes")

t0 = time.perf_counter()
res_401 = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=Ciudad Valles&appid=CLAVE_INVALIDA",
    timeout=10,
)
ms_401 = (time.perf_counter() - t0) * 1000

print(f"[401] Código: {res_401.status_code}")
print(f"[401] Tiempo: {ms_401:.0f} ms")
print(f"[401] Tamaño: {len(res_401.content)} bytes")