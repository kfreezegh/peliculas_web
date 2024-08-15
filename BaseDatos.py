from Peliculas import Pelicula
import csv

class BaseDatos:
    def __init__(self,archivo:str):
        self.base = {}
        registros = self.carga_archivo_csv(archivo)
        for r in registros:
            pelicula = Pelicula(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8])
            self.base[r[2]] = pelicula

    def desplegar (self):
        for titulo,pelicula in self.base.items():
            print(f"{titulo}|{pelicula.fecha_estreno}|{pelicula.direccion}")

    def get_titulos(self):
        lista = [ (k,self.base[k]) for k in sorted(self.base)]
        return lista
        
    def carga_archivo_csv(self,archivo:str)->list:
        #aqui va el codigo
        lista_registros = []
        with open(archivo,"r",encoding="utf-8") as a:
            reader = csv.reader(a)
            for renglon in reader:         
                lista_registros.append(renglon)
        return lista_registros
        

if __name__ == "__main__":
    bd = BaseDatos("peliculas_web/peliculas.csv")
    bd.desplegar()
    lista = bd.get_titulos()
    print(lista)
