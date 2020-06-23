import json

from generateFolders import generateFolders
from removeFiles import removeFiles
from exitProgram import exitProgram

print ('\n******************** BIENVENIDO A cRAW ********************')

print(*['', '¿Qué quieres hacer?', '', '1: Generar carpetas', '2: Borrar RAW', '3: Salir', ''], sep = '\n') 

action = int(input()) 

with open('config.json') as json_file:
    config = json.load(json_file)

    if (action == 1):
        print (*['', 'Pulsa para utilizar...', '0: Rutas nuevas', '1: Rutas ya configuradas', ''] , sep = '\n')
        configAction = int(input()) 

        if (configAction == 1):
            generateFolders(config['config'], 1)
        else:
            generateFolders(config['config'], 0)

    elif (action == 2):
        removeFiles(config['config'])

    elif (action == 3):
        exitProgram()