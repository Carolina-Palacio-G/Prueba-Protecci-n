def clasificar_estudiante():
    print("Bienvenido, por favor ingrese sus notas.\n")
    
    # Validación de notas
    def obtener_nota_valida(nota_num):
        while True:
            try:
                nota = float(input("Por favor ingrese la nota {} (Los valores de las notas deben ir desde: 0 a 5): ".format(nota_num)))
                if 0 <= nota <= 5:
                    return nota
                else:
                    print("Nota inválida. Los valores de las notas deben ir desde: 0 a 5.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

    # Solicitar las cuatro notas
    nota_1 = obtener_nota_valida(1)
    nota_2 = obtener_nota_valida(2)
    nota_3 = obtener_nota_valida(3)

    # Calcular la nota definitiva basada en porcentajes
    porcentaje_1 = nota_1 * 0.25
    porcentaje_2 = nota_2 * 0.35
    porcentaje_3 = nota_3 * 0.40
    nota_final = porcentaje_1 + porcentaje_2 + porcentaje_3 

    # Clasificar según la nota final
    if nota_final >= 4.5:
        categoria = "Sobresaliente"
    elif 3.5 <= nota_final < 4.5:
        categoria = "Bueno"
    elif 3.0 <= nota_final < 3.5:
        categoria = "Regular"
    else:
        categoria = "Deficiente"

    # Mostrar resultados
    print("Resultados:")
    print("Notas ingresadas:", nota_1, nota_2, nota_3)
    print("Nota definitiva:", round(nota_final, 2))  # Redondear a 2 decimales
    print("Categoría:", categoria)

clasificar_estudiante()