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
            lineas = f.readlines()

        for i in range(0, len(lineas), 6):
            bloque = lineas[i:i+6]
            if len(bloque) < 6:
                continue
            pregunta = bloque[0].strip()
            opciones = [bloque[j].strip() for j in range(1, 5)]
            respuesta_ok = bloque[5].strip().upper()
            preguntas.append({
                "pregunta": pregunta,
                "opciones": opciones,
                "respuesta_ok": respuesta_ok
            })
    except FileNotFoundError:
        print(f"--- ERROR --- ->No se encontró el archivo '{ruta}'.<-")
    except Exception as e:
        print(f"--- ERROR --- ->Al leer el archivo '{ruta}'no es válido.<-")

    return preguntas
