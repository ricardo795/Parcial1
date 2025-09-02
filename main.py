from Aparato import Aparato
from utilidades import mostrar_resultados

def main():
    print("Registro de aparatos eléctricos")
    tarifa = float(input("Ingrese la tarifa por kWh ($): "))
    aparatos = []

    while True:
        nombre = input("Nombre del aparato (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        potencia = float(input("Potencia del aparato (Watts): "))
        horas = float(input("Horas de uso diario: "))
        aparato = Aparato(nombre, potencia, horas, tarifa)
        aparatos.append(aparato)
        print("Aparato registrado.\n")

    aparatos.sort(key=lambda x: x.consumo_kwh, reverse=True)
    mostrar_resultados(aparatos)

if __name__ == "__main__":
    main()