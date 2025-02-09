import os

PATH_IMG = "img.webp"

if not os.path.exists(PATH_IMG):
    print("Erro: o arquivo não existe")
else:
    print("O arquivo existe")
