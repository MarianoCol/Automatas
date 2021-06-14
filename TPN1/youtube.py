import re

regex = re.compile(r'(?:https?:\/\/)?(?:[0-9A-Z-]+\.)?(?:youtube|youtu|youtube-nocookie)\.(?:com|be)\/(?:watch\?v=|watch\?.+&v=|embed\/|v\/|.+\?v=)?([^&=\n%\?]{11})')

URL = input("Ingrese URL del video: ")

if(regex.search(URL)):
    print("ID correcto")
else:
    print("ID incorrecto")