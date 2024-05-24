def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Convertir cadena a binario")
        print("2. Convertir binario a cadena")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            Cadena = input("Ingrese una cadena: ")
            Binario = string_to_binary(Cadena)
            print(f"Representación binaria: {Binario}")
        
        elif opcion == '2':
            Binario = input("Ingrese una secuencia de binarios (separados por espacio): ")
            Cadena = binary_to_string(Binario)
            print(f"Cadena resultante: {Cadena}")
        
        elif opcion == '3':
            print("Adios")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()