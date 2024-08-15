class Pelicula:
    def __init__(self,id,usuario,titulo,titulo_original,url_image,genero,fecha_estreno,direccion,sinopsis) -> None:
        self.id = id
        self.usuario = usuario
        self.titulo = titulo
        self.titulo_original = titulo_original
        self.url_image = url_image
        self.genero = genero
        self.fecha_estreno = fecha_estreno
        self.direccion = direccion
        self.sinopsis = sinopsis
    def __str__(self) -> str:
        return f"{self.titulo}|{self.fecha_estreno}|{self.direccion}"

if __name__ == "__main__":
    pelicula = Pelicula(1,"FMCG","Matrix","The Matrix","url.jpg","Ciencia Ficción","1999-12-01","Watchoswki sisters","Un mundo alterno")
    print(pelicula)
