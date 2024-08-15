import csv

class Usuario:
    def __init__(self,id,nombre,email,password):
        self.id      = id
        self.nombre  = nombre
        self.email   = email
        self.password= password
    def __str__(self):
        return f"{self.id:8}|{self.nombre:25}|{self.email:28}|{self.password}"

class BaseUsuarios:
    def __init__(self,archivo):
        self.base = {}
        lista_registros = self.carga_archivo_csv(archivo)
        for registro in lista_registros:
            id       = registro[0]
            nombre   = registro[1]
            email    = registro[2]
            password = registro[3]
            user = Usuario(id, nombre, email, password)
            self.base[email]= user
    
    def authenticate(self,user_email,pwd):
        return_value = False
        if user_email in self.base:
            if self.base[user_email].password == pwd:
                return_value = True
        return return_value
    
    def get_usuario(self, email):
        if email in self.base:
            return self.base[email]
        else:
            return None
        
    def carga_archivo_csv(self,archivo:str)->list:
        #aqui va el codigo
        lista_registros = []
        with open(archivo,"r",encoding="utf-8") as a:
            reader = csv.reader(a)
            #next(reader)
            for renglon in reader:         
                lista_registros.append(renglon)
        return lista_registros
    def despliega(self):
        for email,usuario in self.base.items():
            print(usuario)

if __name__ == "__main__":
    bu = BaseUsuarios("peliculas_web/usuarios.csv")
    bu.despliega()
    print(bu.authenticate("federico.cirett@unison.mx", "12345"))