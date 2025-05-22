import os
from PIL import Image

def recortar_cuadricula(imagen, size, rows, columns):
    subimages = []

    for row in range(rows):
        for column in range(columns):
            # Calcular los límites del recorte
            left = column * size
            top = row * size
            right = left + size
            low = top + size
            
            # Recortar la subimagen
            subimage = imagen.crop((left, top, right, low))
            subimages.append(subimage)

    return subimages

# Configuración inicial
ROWS = 3   # Número de rows
COLUMNS = 3  # Número de columns
INPUT_DIR = "unhealthy_images"  # Directorio de entrada

total_images = 0
# Procesar cada imagen en el directorio de entrada
for archivo in os.listdir(INPUT_DIR):
    total_images += 1
    if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
        ruta_imagen = os.path.join(INPUT_DIR, archivo)
        imagen_original = Image.open(ruta_imagen)

        SIZE = imagen_original.size[0] / COLUMNS

        print(f"tamaño de la imagen: {imagen_original.size}")
        print(f"formato de la imagen: {imagen_original.format}")

        # Recortar las imágenes
        imagenes_recortadas = recortar_cuadricula(imagen_original, SIZE, ROWS, COLUMNS)

        folder_names = ["RU", "CU", "LU", "R", "C", "L", "RD", "CD", "LD"]

        # Guardar las imágenes recortadas
        for idx, img in enumerate(imagenes_recortadas):
            # Guardar la imagen en la carpeta correspondiente
            save_name = f"{archivo + '_' + folder_names[idx]}.jpg"
            # Si el directorio no existe, crearlo
            directory = f"unhealthy-cropped-images/{folder_names[idx]}"
            if not os.path.exists(directory):
                os.makedirs(directory)
            img.save(f"{directory}/{save_name}")
            # img.save(f"all_images/{save_name}")

print(f"Total de imágenes procesadas: {total_images}")