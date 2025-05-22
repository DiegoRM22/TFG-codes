import os
from PIL import Image

def crop_center(img, crop_width, crop_height):
    """
    Recorta un rectángulo desde el centro de la imagen.
    """
    img_width, img_height = img.size
    left = (img_width - crop_width) // 2
    top = (img_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    return img.crop((left, top, right, bottom))

def process_images(input_dir, output_dir, crop_width, crop_height):
    """
    Procesa todas las imágenes de input_dir, recortando y guardando en output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                img = Image.open(input_path)
                cropped_img = crop_center(img, crop_width, crop_height)
                cropped_img.save(output_path)
                print(f"Imagen recortada y guardada: {output_path}")
            except Exception as e:
                print(f"Error con {filename}: {e}")

# CONFIGURACIÓN
input_folders = ["unhealthy-cropped-images/C", "unhealthy-cropped-images/CD", "unhealthy-cropped-images/CU", "unhealthy-cropped-images/L", "unhealthy-cropped-images/LD", 
                 "unhealthy-cropped-images/LU", "unhealthy-cropped-images/R", "unhealthy-cropped-images/RD", "unhealthy-cropped-images/RU"]       # <-- Cambia esto
output_folder = "manual-cropped-eyes/unhealthy2"    # <-- Cambia esto
recorte_ancho = 800   # ancho del recorte
recorte_alto = 350     # alto del recorte

# EJECUTAR
for input_folder in input_folders:
  process_images(input_folder, output_folder, recorte_ancho, recorte_alto)
