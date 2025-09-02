def mostrar_resultados(aparatos):
    print("\n--- Consumo y costo por aparato ---")
    print(f"{'Aparato':15} {'Consumo (kWh)':15} {'Costo ($)':10}")
    total_consumo = 0
    total_costo = 0
    for a in aparatos:
        print(f"{a.nombre:15} {a.consumo_kwh:15.2f} {a.costo:10.2f}")
        total_consumo += a.consumo_kwh
        total_costo += a.costo

    print("\nResumen mensual:")
    print(f"Consumo total: {total_consumo:.2f} kWh")
    print(f"Gasto total: ${total_costo:.2f}")