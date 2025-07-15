from preguntas import (
    cargar_preguntas_ejemplo,
    cargar_pregunta_java,
    cargar_pregunta_python,
    cargar_preguntas_txt,
)
from calificaciones import mostrar_calificaciones


def empezar_test():
    print("---------------------------")
    print("Selecciona el cuestionario:")
    print("--- 1 --- Python")
    print("--- 2 --- Java")
    print("--- 3 --- HTML/CSS")
    print("--- 4 --- Ejemplo de prueba")
    print("---------------------------")

    opcion = input("Tu elección: ").strip()

    if opcion == "1":
        preguntas = cargar_pregunta_python("datos_externos/preguntas_python.json")
    elif opcion == "2":
        preguntas = cargar_pregunta_java("datos_externos/pregunta_java.json")
    elif opcion == "3":
        preguntas = cargar_preguntas_txt("datos_externos/preguntas_htm_css.txt")
    elif opcion == "4":
        preguntas = cargar_preguntas_ejemplo()
    else:
        print("Opción no válida")
        return

    correctas = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta = input("Elige tu respuesta (A, B, C, o D): ").strip().upper()
        if respuesta == pregunta["respuesta_ok"].upper():
            print("Correcto")
            correctas += 1
        else:
            print("Fallo")

    if len(preguntas) == 0:
        print("No se cargaron preguntas, revisalo.")
    else:
        mostrar_calificaciones(correctas, len(preguntas))
