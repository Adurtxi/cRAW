import glob, os

from shutil import copyfile, move

# Crear carpeta
def createFolder(pathWithFolder):
    try:
        os.mkdir(pathWithFolder)
    except OSError:
        print ('Error al crear la carpeta', 'red')

# Copiar archivo
def copyFile(path, destination, fileName):
    copyfile(path + '/' + fileName, destination + '/' + fileName)

# Conseguir los archivos
def getFiles(path, ext, pathWithFolder, folder):
    os.chdir(path)

    filesQuantity = len(glob.glob(ext))

    print('\nArchivos encontrados:', filesQuantity, folder, '\n')

    count = 0

    for file in glob.glob(ext):
        count = count + 1
        print('\n  ', count, ' /', filesQuantity, end="\r")

        copyFile(path, pathWithFolder + '/' + folder, file)

# Función principal
def generateFolders(config, useDefaults):

    print ('\n**************************************** Paso 1 ****************************************')

    # Guardar en otra ruta 
    if (useDefaults == 0):
        path = str(input('\nIntroduce la ruta donde quieres crear la carpeta: ')) 
    else:
        path = config['path']
        sdPath = config['sdPath']

    # Nombre de la carpeta
    folderName = str(input('\nIntroduce el nombre de la carpeta: ')) 

    # Crear carpetas
    pathWithFolder = path + '/' + folderName

    createFolder(pathWithFolder)

    createFolder(pathWithFolder + config['jpgPath'])
    createFolder(pathWithFolder + config['rawPath'])
    createFolder(pathWithFolder + config['mp4Path'])

    # Ruta de SD alternativa
    if (useDefaults == 0):
        print ('\n**************************************** Paso 2 ****************************************')

        sdPath = str(input('\nIntroduce la ruta de la SD: ')) 
   
    # Coger los archivos
    getFiles(sdPath + config['sdJPGPath'], '*' + config['jpgExtension'], pathWithFolder, 'JPG')
    getFiles(sdPath + config['sdRAWPath'], '*' + config['rawExtension'], pathWithFolder, 'RAW')
    getFiles(sdPath + config['sdMP4Path'], '*' + config['mp4Extension'], pathWithFolder, 'MP4')

    print ('\n\n******************** IMAGENES COPIADAS CORRECTAMENTE ********************')  
