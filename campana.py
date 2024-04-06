class campana():
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date,anuncio) -> None:
        self.__nombre =nombre
        self.__fecha_inicio = fecha_inicio
        self.___fecha_termino = fecha_termino
        self.__anuncio =anuncio

        def __str__(self):
            return f"""
            Campaña: {self.__nombre}
            Anuncio: {self.__anuncio} Video {cant_display} Display, {cant_social} Social
            """