

class Suma():

    def __init__(self,clave_departamento=None,descripcion=None,A=None,R=None,B=None):
        self.clave_departamento=clave_departamento
        self.descripcion=descripcion
        self.A=A
        self.R=R
        self.B=B

    def to_JSON(self):
        return{
            'clave_departamento': self.clave_departamento,
            'descripcion': self.descripcion,
            'A': self.A,
            'R': self.R,
            'B': self.B
        }