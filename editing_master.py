import os
from PIL import Image

# Pfad zum Eingabeordner mit den Bildern
input_folder = "/pfad/zum/eingabeordner"

# Pfad zum Bild 'image2' mit 10% Transparenz
image2_path = "/pfad/zum/image2.png"

# Pfad zum Ausgabeordner für die bearbeiteten Bilder
output_folder = "/pfad/zum/ausgabeordner/Fertig bearbeitet"

# Überprüfen und Erstellen des Ausgabeordners, falls er nicht existiert
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Liste aller Dateien im Eingabeordner
file_list = os.listdir(input_folder)

# Schleife über alle Dateien im Eingabeordner
for file_name in file_list:
    # Pfad zur aktuellen Datei
    file_path = os.path.join(input_folder, file_name)
    
    # Überprüfen, ob es sich um eine Bilddatei handelt
    if file_path.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
        # Öffnen des Eingabebildes
        image = Image.open(file_path)
        
        # Skalieren des Bildes auf 1280x960
        resized_image = image.resize((1280, 960))
        
        # Öffnen von image2 mit 10% Transparenz
        image2 = Image.open(image2_path).convert("RGBA")
        image2 = image2.resize(resized_image.size)
        
        # Erstellen eines Bildes mit 10% Transparenz von image2
        overlay = Image.new("RGBA", resized_image.size)
        alpha = int(0.1 * 255)  # Transparenzwert (10% transparent)
        overlay_with_alpha = image2.copy()
        overlay_with_alpha.putalpha(alpha)
        overlay.paste(overlay_with_alpha, (0, 0), mask=overlay_with_alpha)
        
        # Zusammenführen der beiden Bilder
        merged_image = Image.alpha_composite(resized_image.convert("RGBA"), overlay)
        
        # Speichern des bearbeiteten Bildes im Ausgabeordner mit Originalnamen als .jpg
        output_path = os.path.join(output_folder, file_name.split(".")[0] + ".jpg")
        merged_image.save(output_path, "JPEG")
