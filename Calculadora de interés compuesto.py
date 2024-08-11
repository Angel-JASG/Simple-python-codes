def cal_calor_futuro(inversion_inicial,tasa_interes,periodos):
    valor_futuro = inversion_inicial * (1 + tasa_interes / 100) ** periodos
    return valor_futuro

inversion_inicial = float(input("Ingrese la cantidad de la inversion inicial: "))
tasa_interes = float(input("Ingrese la tasa de interes anual (%): "))
periodos = int(input("Ingrese el numero de periodos de inversion: "))

valor_futuro = cal_calor_futuro(inversion_inicial,tasa_interes,periodos)


print("Cantidad inicial de inversion:",inversion_inicial,"$")
print("Tasa de interes anual:",tasa_interes,"%")
print("Numero de periodos de inversion:",periodos,"años")
print("El valor futuro de la inversion sera de: ", valor_futuro)