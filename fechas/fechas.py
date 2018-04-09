import os
import re
import json

class Fechas:
    """clase para las fechas del servicio web"""

    def __init__(self):
        try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
            if os.path.exists('fechas.json'):
                path='fechas.json'
            elif os.path.exists('/data/fechas.json'):
                path='/data/fechas.json'
            elif os.path.exists('./data/fechas.json'):
                path='./data/fechas.json'
            elif os.path.exists('../data/fechas.json'):
                path='../data/fechas.json'
            else:
                raise IOError("No se encuentra 'fechas.json'")
                
            with open(path) as data_file:
                self.fechas = json.load(data_file)
        except IOError as fallo:
            print("Error {:s} leyendo fechas.json".format( fallo ) )

    def todos_fechas(self):
        return self.fechas

    def cuantos(self):
        return len(self.fechas['fechas'])

    def uno(self,fecha_id):
        if fecha_id > len(self.fechas['fechas']) or fecha_id < 0:
            raise IndexError("Indice fuera de rango")
        return self.fechas['fechas'][fecha_id]

    def nuevo( self, filename, title, fecha ):
        if ( not type(filename) is str):
            raise TypeError( "El nombre del archivo debe ser una cadena" )
        if ( not type(title) is str):
            raise TypeError( "El título de la fecha debe ser una cadena" )
        if not re.match("\d+/\d+\d+", fecha) :
            raise ValueError( "El formato de la fecha es incorrecto" )
        existe = list(filter( lambda fecha: 'file' in fecha and fecha['file'] == filename, self.fechas['fechas'] ))
        if len(existe) > 0:
            raise ValueError( "Ese fichero ya existe")
        
        self.fechas['fechas'].append( {'file': filename,
                                     'title': title,
'fecha': fecha } )
