from test import empezar_test

def mostrar_menu():
    print("-------------------------------------")
    print("=== MENU ====")
    print("*** 1 *** Comenzar cuestionario")
    print("*** 2 *** Salir")
    print("_____________________________________")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            empezar_test()
        elif opcion == "2":
            print("Vuelve cuando quieras y mejora tus conocimientos")
            break
        else:
            print("Esta opción no es válida")

if __name__=="__main__":
    main()