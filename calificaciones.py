def mostrar_calificaciones(correctas, total):
    calificaciones_porciento = (correctas/total)*100
    print("=== CALIFICACIONES ===")
    print(f"Correctas: {correctas}/{total}({calificaciones_porciento:.2f}%)")
    if calificaciones_porciento == 100:
        print("Matrícula de Honor")
    elif calificaciones_porciento >= 90:
        print("Sobresaliente")
    elif calificaciones_porciento >= 70:
        print("Notable")
    elif calificaciones_porciento >= 60:
        print("Bien")
    elif calificaciones_porciento >= 51:
        print("Suficiente")
    else:
        print("Insuficiente (Debes de repetir el test hasta aprobar)")