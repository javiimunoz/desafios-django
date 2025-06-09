## Rutas-implementadas-semana-2
1. `/`  
   - Tipo: Fija  
   - Función: `inicio`  
   - Salida: ""Hola, mi web de Django""

2. `/saludo/<nombre>/`  
   - Tipo: Con parámetro de texto  
   - Función: `saludo_personalizado`  
   - Ejemplo: `/saludo/Juan/`  
   - Salida: "Hola, "nombre"! Qué tal?"

3. `/edad/<edad>/`  
   - Tipo: Con parámetro numérico  
   - Función: `mostrar_edad`  
   - Ejemplo: `/edad/30/`  
   - Salida: "Tu edad es: 30 años."

## Funcionamiento de las rutas

- `/mi_web/saludar`  
  Muestra un saludo fijo: "Hola, mi web de Django".

- `/mi_web/saludo/<nombre>/`  
  Muestra un saludo personalizado usando el nombre recibido en la URL.  
  Ejemplo: `/mi_web/saludo/Juan/` responde con "Hola, Juan!"

- `/mi_web/edad/<edad>/`  
  Muestra la edad recibida como parámetro en la URL.  
  Ejemplo: `/mi_web/edad/30/` responde con "Tu edad es: 30 años."

## Archivos usados

- `mi_web/views.py`: Define las respuestas.
- `mi_web/urls.py`: Define las rutas de la app.
- `miweb/urls.py`: Redirige al archivo de rutas de la app.
