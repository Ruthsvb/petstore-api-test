# Prueba técnica de carga - Petstore API

Este proyecto corresponde a una prueba técnica para el equipo de Pruebas de Carga del cliente BFCL.  
La idea fue simular el comportamiento de varios usuarios haciendo peticiones `POST` a la [Petstore Swagger API](https://petstore.swagger.io/) usando **Locust** como herramienta principal para medir el rendimiento.

## Que herramientas se usaron 

- **Lenguaje:** Python 
- **Herramienta de carga:** Locust  
- **Librería para requests:** Requests  
- **Entorno:** Virtualenv (`.venv`)

 También podríamos haber usado JavaScript con Node.js para estas pruebas, pero por tiempo y familiaridad se optó por Python.

---

## Endopoints

Se decidió no probar solo un endpoint, sino simular un flujo un poco más completo:

1. `POST /pet`: Crear una mascota  
2. `POST /store/order`: Crear una orden de pedido  
3. `POST /user`: Crear un usuario

Para cada uno se preparó su archivo `.json` con los datos necesarios, que están dentro del directorio `/data`.

---

## Código

- `petstore_api.py`: Módulo que contiene los métodos que hacen las llamadas `POST` a los endpoints. Cada uno carga su JSON desde `/data`.
- `locustfile.py`: Archivo principal para ejecutar la prueba de carga. Aquí se usa Locust para simular el comportamiento de un usuario que hace las tres peticiones anteriores.

---

## Cómo ejecutar la prueba de carga

1. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

2. Ejecuta Locust desde la raíz del proyecto:

```bash
locust
```

3. Se tu navegador en [http://localhost:8089]

4. Ingresa los parámetros de la prueba (usuarios, spawn rate, etc.) y haz clic en “Start swarming”.

---

## Resultados

Una vez finalizada la prueba, se puede descargar un reporte en HTML directamente desde la UI de Locust.  


---

## Consideraciones finales

En un principio, el proyecto se inició en la rama `main` y se creó una estructura pensada para pruebas unitarias, con carpetas por entidad (`pet`, `order`, `user`).  
Sin embargo, por temas de tiempo y enfoque del ejercicio, esas pruebas no se desarrollaron.

Para mantener todo ordenado y más realista, se creó una nueva rama llamada:

```
feature/pruebas-carga
```

Ahí se hizo limpieza del proyecto, se eliminaron carpetas innecesarias y se centralizó toda la lógica en un solo archivo (`petstore_api.py`), junto con el `locustfile.py`.


---

Cualquier feedback es bienvenido. ¡Gracias por revisar!

