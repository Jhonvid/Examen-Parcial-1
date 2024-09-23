def cal_agua_gen(agua_ini, n_gen):

    org = 2
    agua_por_org = agua_ini

    for gen in range(1, n_gen + 1):
        org *= 2
        agua_por_org = agua_ini / org  

    return agua_por_org

while True:
    agua_ini = float(input("Ingresa la cantidad inicial de agua (en litros) en la generación 0: "))
    if 0 < agua_ini:
        break
    else:
        print("No existe la cantidad de agua negativa, intente de nuevo")

while True:
    n_gen = int(input("Ingresa el número de generaciones (máximo 50): "))
    if 0 <= n_gen <= 50:
        break
    else:
        print("El número máximo de generaciones es 50. Por favor, ingresa un valor válido.")

resultado = cal_agua_gen(agua_ini, n_gen)
print(f"Cantidad de agua que le corresponde a un organismo después de {n_gen} generacion&es: {resultado}")