from PIL import Image, ImageDraw, ImageFont

# Crie uma nova imagem com fundo branco
img = Image.new('RGB', (200, 100), color = (255, 255, 255))

# Inicialize o objeto de desenho
d = ImageDraw.Draw(img)

# Defina a fonte (você pode precisar ajustar o caminho para a fonte)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

# Adicione texto à imagem
d.text((10, 40), "Login", font=font, fill=(0, 0, 0))

# Salve a imagem na pasta de trabalho
img.save('/home/lucas/Documentos/Repositorio/Python/PaineisEmPython/PainelTkinter/Login/img.png')