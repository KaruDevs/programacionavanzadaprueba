class Anuncio():
    def ___init__(self, 
                  ancho:int, 
                  alto: int, 
                  url_archivos:str, 
                  url_click:str, 
                  sub_tipo: str):
        self.__ancho =ancho if ancho > 0 else 1
        self.__alto =alto if alto > 0 else 1
        self.__url_archivos :str =url_archivos
        self.__url_click: str =url_click
        self.sub_tipo: str = sub_tipo

class Video(Anuncio):
    FORMATO = "Video"
    Subtipos = ("instream", "outstream")
    def __init__(self,ancho:int, 
                  alto: int, 
                  url_archivos:str, 
                  url_click:str, 
                  sub_tipo: str,
                  duracion:int):
        super ().__init__(1,1,url_archivos,url_click,sub_tipo)
        self.__duracion = duracion if duracion >0 else 5

class Display (Anuncio):
    FORMATO ="Display"
    SUBTIPOS =("tradicional", "native")
    def __init__(self,ancho:int, 
                  alto: int, 
                  url_archivos:str, 
                  url_click:str, 
                  sub_tipo: str,
                  duracion:int):
        super ().__init__(ancho,alto,url_archivos,url_click,sub_tipo)

class Social():
    FORMATO ="Social"
    Subtipos= ("facebook", "lindekin")
    def __init__(self,ancho:int, 
                  alto: int, 
                  url_archivos:str, 
                  url_click:str, 
                  sub_tipo: str,
                  duracion:int):
        super ().__init__(ancho,alto,url_archivos,url_click,sub_tipo)
  