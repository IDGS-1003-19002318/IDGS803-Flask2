class Resistencia():
    def __init__(self, *args):
        super(Resistencia, self).__init__(*args)
        
        self._resistencias = []
        
    def add_resistencia(self, resistencia):
        self._resistencias.append(resistencia)
        
    def get_resistencias(self):
        return self._resistencias
    
    def get_resistencia(self, index):
        return self._resistencias[index]
    
    def get_resistencia_total(self):
        resistencia_total = 0
        
        for resistencia in self._resistencias:
            resistencia_total += resistencia.get_resistencia()
            
        return resistencia_total
    
    def get_maxima_corriente(self):
        return self.get_resistencia_total() / 10
    
    def get_maxima_potencia(self):
        return self.get_maxima_corriente() * 220
    
    def get_minima_resistencia(self):
        return self.get_resistencia_total() / 0.1