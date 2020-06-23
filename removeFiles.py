import glob, os

from termcolor import colored

def getFiles(path, ext, type):
    os.chdir(path)

    filesQuantity = len(glob.glob(ext))

    print('\n', type, 'encotrados:', filesQuantity)

    return glob.glob(ext)

def removeFiles(config):
    # Ruta de la carpeta
    path = str(input('\nIntroduce la ruta de la carpeta que contenga la carpeta JPG Y RAW: ')) 

    raws = getFiles(path + config['rawPath'], config['rawExtension'], 'RAWs')
    jpgs = getFiles(path + config['jpgPath'], config['jpgExtension'], 'JPGs')

    imgsToDelete = []
    
    for raw in raws:
        imgsToDelete.append(raw.partition('.')[0])

    for jpg in jpgs:
        imgsToDelete.remove(jpg.partition('.')[0])

    delete = int(input('\nPulsa 1 para borrar los archivos o 0 para salir: ')) 

    if (delete == 1):
        for imgToDelete in imgsToDelete:
            file = path + '/RAW/' + imgToDelete + '.ARW'
            
            if os.path.exists(file):
                os.remove(file) 

        print (colored('\n******************** IMAGENES RAW ELIMINADOS CORRECTAMENTE ********************', 'green'))