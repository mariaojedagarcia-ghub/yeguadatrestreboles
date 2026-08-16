#!/usr/bin/env python3
"""
Convierte el PDF del árbol genealógico que exporta el LG PRE en la imagen
que usa la web, difuminando el número de microchip.

    python3 procesar_arbol.py Utrera.pdf utrera-hm

Deja el resultado en img/caballos/<slug>/arbol.jpg
"""
import subprocess, sys, os, re, tempfile
from PIL import Image, ImageFilter, ImageDraw


def imagen_del_pdf(pdf, dpi=200):
    """Saca la imagen del PDF. Si la incrustada es mayor, se queda con esa."""
    tmp = tempfile.mkdtemp()
    subprocess.run(['pdfimages', '-png', pdf, os.path.join(tmp, 'x')], check=True)
    sueltas = sorted(f for f in os.listdir(tmp) if f.endswith('.png'))
    mejor = None
    if sueltas:
        mejor = Image.open(os.path.join(tmp, sueltas[0]))
    # rasterizado a dpi, por si diera más resolución
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), pdf, os.path.join(tmp, 'r')], check=True)
    raster = sorted(f for f in os.listdir(tmp) if f.startswith('r') and f.endswith('.png'))
    if raster:
        im = Image.open(os.path.join(tmp, raster[0]))
        if mejor is None or im.size[0] > mejor.size[0]:
            mejor = im
    return mejor.convert('RGB')


def tapar_microchip(im):
    """Localiza la fila MICROCHIP por OCR y difumina el número."""
    tmp = tempfile.mktemp(suffix='.png')
    im.save(tmp)
    tsv = subprocess.run(['tesseract', tmp, 'stdout', '--psm', '11', 'tsv'],
                         capture_output=True, text=True).stdout
    os.remove(tmp)

    palabras = []
    for linea in tsv.strip().split('\n')[1:]:
        p = linea.split('\t')
        if len(p) >= 12 and p[11].strip():
            palabras.append((p[11].strip(), *(int(p[i]) for i in (6, 7, 8, 9))))

    etiqueta = next((w for w in palabras if re.fullmatch(r'MICROCHIP:?', w[0], re.I)), None)
    if not etiqueta:
        return im, False
    _, ex, ey, ew, eh = etiqueta
    centro = ey + eh / 2

    # el valor: una cifra larga en la misma fila, a la derecha de la etiqueta
    # el valor: la cifra larga más a la izquierda, en la misma fila y a la
    # derecha de la etiqueta (más a la derecha están los códigos del árbol)
    cifras = [w for w in palabras
              if re.fullmatch(r'\d{9,25}', w[0])
              and w[1] > ex
              and abs((w[2] + w[4] / 2) - centro) < 12]
    if not cifras:
        return im, False
    valor = min(cifras, key=lambda c: c[1])

    x0, y0 = valor[1] - 8, valor[2] - 6
    x1, y1 = valor[1] + valor[3] + 8, valor[2] + valor[4] + 6

    region = im.crop((x0, y0, x1, y1))
    im.paste(region.filter(ImageFilter.GaussianBlur(10)), (x0, y0))
    d = ImageDraw.Draw(im)
    d.text((x0 + 6, y0 + max(0, (y1 - y0 - eh) / 2)), 'no publicado', fill=(120, 115, 105))
    return im, True


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    pdf, slug = sys.argv[1], sys.argv[2]
    destino = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'img', 'caballos', slug)
    os.makedirs(destino, exist_ok=True)

    im = imagen_del_pdf(pdf)
    im, tapado = tapar_microchip(im)
    salida = os.path.join(destino, 'arbol.jpg')
    im.save(salida, 'JPEG', quality=88, optimize=True, progressive=True)

    print(f'{slug}: {im.size[0]}x{im.size[1]} -> {salida}')
    print('microchip difuminado' if tapado else '⚠ no se encontró la fila del microchip: revísalo a mano')


if __name__ == '__main__':
    main()
