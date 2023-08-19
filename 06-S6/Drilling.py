usuarios = {'001':'Marca','002':'Mónica','003':'Jacob'} 
mensaje = 'La clave 004 no está en el diccionario'
id_usuario = '004'
try:        #intenta hacer esto
    print(usuarios[id_usuario])
except KeyError: #Oh no!
    print(mensaje)
    usuarios[id_usuario]= None #le asignamos valor al error
print(usuarios)
    