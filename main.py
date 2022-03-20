#Importacion de libreria
from deep_translator import GoogleTranslator;

#Metodo para traducir un determinado texto
def translate(texto):
    traductor = GoogleTranslator(source="es", target="en");
    traduccion = traductor.translate(texto)
    return traduccion;

#Menu basico para introducir texto
print('Hola');
print('¿Que texto te gustaria traducir a ingles el dia de hoy?');
texto = input();
print("El resultado es: " + translate(texto));
