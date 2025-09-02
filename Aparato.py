class Aparato:
    def __init__(self, nombre, potencia_watts, horas_uso, tarifa_kwh):
        self.nombre = nombre
        self.potencia_watts = potencia_watts
        self.horas_uso = horas_uso
        self.tarifa_kwh = tarifa_kwh
        self.consumo_kwh = self.calcular_consumo()
        self.costo = self.calcular_costo()

    def calcular_consumo(self):
        return (self.potencia_watts * self.horas_uso * 30) / 1000

    def calcular_costo(self):
        return self.consumo_kwh * self.tarifa_kwh