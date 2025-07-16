import json

def cargar_preguntas_ejemplo():
    return [{"pregunta":"¿Cómo me llamo?",
             "opciones":["A) Manolo","B) Rubén","C) Carlos","D) Kiko"],
             "respuesta_ok": "B"},
            {"pregunta":"¿Cómo me apellido?",
             "opciones":["A) López","B) Suarez","C) Pérez","D) Urrutia"],
             "respuesta_ok":"A"}]

def cargar_pregunta_java(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta} no tiene formato JSON válido")
        return []

def cargar_pregunta_python(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta} no es válido")
        return []

def cargar_preguntas_txt(ruta):
    preguntas = []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        bloques = contenido.strip().split("\n\n")  # Separa bloques por línea en blanco doble

        for bloque in bloques:
            lineas = bloque.strip().split("\n")
            if len(lineas) < 6:
                continue  # Bloques incompletos se saltan

            pregunta = lineas[0].strip()
            opciones = [lineas[i].strip() for i in range(1, 5)]
            respuesta_linea = lineas[5].strip()

            if "Respuesta correcta:" in respuesta_linea:
                respuesta_ok = respuesta_linea.split(":")[1].strip().upper()
            else:
                continue  # si no se encuentra la línea con la respuesta

            preguntas.append({
                "pregunta": pregunta,
                "opciones": opciones,
                "respuesta_ok": respuesta_ok
            })
    except FileNotFoundError:
        print(f"--- ERROR --- ->No se encontró el archivo '{ruta}'.<-")
    except Exception as e:
        print(f"--- ERROR --- ->Al leer el archivo '{ruta}' no es válido. Detalle: {e}")

    return preguntas
