# Ejercicio 01: APIs REST

## Tabla de resultados

| API / Endpoint | Método | Código | Tiempo (ms) | Bytes |
| :--- | :---: | :---: | :---: | :---: |
| JSONPlaceholder (Listar posts) | GET | 200 | 300 ms | 27520 B |
| JSONPlaceholder (Crear post) | POST | 201 | 341 ms | 35 B |
| PokéAPI (Pikachu) | GET | 200 | 255 ms | 300521 B |
| OpenWeatherMap (Cd. Valles) | GET | 200 | 315 ms | 108 B |
| Recurso Inexistente | GET | 404 | 205 ms | 2 B |
| Sin Clave / Clave inválida | GET | 401 | 250 ms | 108 B |

---

## Errores provocados

* **404 (Not Found):** Consulté el post 999999 en JSONPlaceholder que no existe. La API regresó código 404 y un JSON vacío `{}` de 2 bytes.
* **401 (Unauthorized):** Mandé la petición a OpenWeatherMap con una API Key inventada (`INVALIDA`). Me regresó el código 401 avisando que la llave no es válida.

---

## Respuestas a las preguntas

* **¿Qué parte de la respuesta realmente usaste?**
  De la PokéAPI solo tomé los nombres de las habilidades de Pikachu, que en el resultado fueron `['static', 'lightning-rod']`.

* **¿Qué porcentaje de los bytes recibidos fue innecesario?**
  La respuesta de PokéAPI pesó 300,521 bytes (unos 300 KB) porque trae muchísima información como sprites, estadísticas, movimientos y juegos. Como los nombres de las habilidades ocupan menos de 100 bytes, más del 99.9% de lo que bajó no se utilizó.