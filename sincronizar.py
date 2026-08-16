#!/usr/bin/env python3
"""
Mira qué hay dentro de img/caballos/ y actualiza datos/caballos.js.

    python3 sincronizar.py

Así no hay que escribir a mano los nombres de las fotos: se dejan los
archivos en la carpeta del caballo y este script los recoge.

QUÉ BUSCA EN CADA CARPETA
    portada.jpg           la foto principal (va siempre la primera)
    01.jpg, 02.jpg ...    el resto de fotos, por orden alfabético
    arbol.jpg             el árbol genealógico
    *.mp4                 vídeos
    <video>-poster.jpg    la miniatura de ese vídeo, si existe

Después conviene ejecutar:  python3 construir.py
"""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = AQUI if os.path.exists(os.path.join(AQUI, 'datos', 'caballos.js')) else os.path.join(AQUI, 'sitio')
DATOS = os.path.join(RAIZ, 'datos', 'caballos.js')

IMG = ('.jpg', '.jpeg', '.png', '.webp')
VID = ('.mp4', '.webm')

ACENTOS = str.maketrans('áàäâãéèëêíìïîóòöôõúùüûñçÁÀÄÂÃÉÈËÊÍÌÏÎÓÒÖÔÕÚÙÜÛÑÇ',
                        'aaaaaeeeeiiiiooooouuuuncAAAAAEEEEIIIIOOOOOUUUUNC')


def nombre_limpio(f):
    """Todo en minúsculas, sin acentos, sin espacios ni caracteres raros.

    macOS no distingue mayúsculas de minúsculas, pero los servidores web sí:
    una foto guardada como 'Portada.jpg' y enlazada como 'portada.jpg' funciona
    en el Mac y da error 404 una vez publicada. Por eso se normaliza aquí.
    """
    base, ext = os.path.splitext(f)
    base = base.translate(ACENTOS).lower()
    base = re.sub(r'[^a-z0-9]+', '-', base).strip('-') or 'foto'
    return base + ext.lower()


def normalizar_nombres(carpeta):
    """Renombra los archivos de la carpeta al nombre limpio. Devuelve los cambios."""
    hechos = []
    for f in sorted(os.listdir(carpeta)):
        if f.startswith('.'):
            continue
        nuevo = nombre_limpio(f)
        if nuevo == f:
            continue
        origen, destino = os.path.join(carpeta, f), os.path.join(carpeta, nuevo)
        # si ya existe otro archivo con el nombre bueno (y no es este mismo,
        # que en macOS es el mismo archivo), no se toca nada
        if os.path.exists(destino) and not os.path.samefile(origen, destino):
            print(f'  ! {f}: ya existe {nuevo}, lo dejo como está')
            continue
        # dos pasos: en macOS un renombrado que solo cambia mayúsculas se ignora
        puente = os.path.join(carpeta, '__tmp__' + nuevo)
        os.rename(origen, puente)
        os.rename(puente, destino)
        hechos.append(f'{f} → {nuevo}')
    return hechos


def main():
    bruto = open(DATOS, encoding='utf-8').read()
    cabecera = bruto.split('const CABALLOS =')[0]
    caballos = json.loads(bruto[bruto.index('['): bruto.rindex(']') + 1])

    # Dejar en minúsculas los nombres de archivo, SOLO en las carpetas que este
    # script explora solo (img/caballos/<slug>/). En las demás —img/portada,
    # img/yeguada, img/servicios, img/marca, video— las rutas están escritas a
    # mano en construir.py: renombrar ahí rompería los enlaces sin avisar.
    renombrados = []
    base = os.path.join(RAIZ, 'img', 'caballos')
    if os.path.isdir(base):
        for d in sorted(os.listdir(base)):
            carp = os.path.join(base, d)
            if os.path.isdir(carp):
                renombrados += normalizar_nombres(carp)
    if renombrados:
        print('Renombrados (los servidores web distinguen mayúsculas):')
        for r in renombrados:
            print('  ' + r)
        print()

    cambios = []
    for c in caballos:
        carpeta = os.path.join(RAIZ, 'img', 'caballos', c['slug'])
        if not os.path.isdir(carpeta):
            continue
        # se ignoran los archivos vacíos (restos de copias)
        archivos = sorted(f for f in os.listdir(carpeta)
                          if os.path.getsize(os.path.join(carpeta, f)) > 0)

        # fotos: portada primero, después el resto (sin árbol ni pósters)
        fotos = [f for f in archivos
                 if f.lower().endswith(IMG)
                 and f != 'arbol.jpg'
                 and not f.endswith('-poster.jpg')]
        # la portada puede llamarse portada.jpg, Portada.png, PORTADA.JPEG...
        portadas = [f for f in fotos if os.path.splitext(f)[0].lower() == 'portada']
        if portadas:
            # si hay varias, manda portada.jpg y las demás se descartan
            elegida = next((f for f in portadas if f == 'portada.jpg'), portadas[0])
            for f in portadas:
                fotos.remove(f)
            fotos.insert(0, elegida)

        # vídeos, cada uno con su póster si lo hay
        videos = []
        for v in [f for f in archivos if f.lower().endswith(VID)]:
            poster = os.path.splitext(v)[0] + '-poster.jpg'
            videos.append({'archivo': v,
                           'poster': poster if poster in archivos else None})

        arbol = 'arbol.jpg' if 'arbol.jpg' in archivos else None

        antes = (c.get('fotos'), c.get('videos'), c.get('arbol'))
        c['fotos'], c['videos'], c['arbol'] = fotos, videos, arbol
        if antes != (fotos, videos, arbol):
            cambios.append(f"  {c['nombre']}: {len(fotos)} foto(s), {len(videos)} vídeo(s)"
                           + (', árbol' if arbol else ''))

    for c in caballos:
        c.setdefault('videos', [])

    open(DATOS, 'w', encoding='utf-8').write(
        cabecera + 'const CABALLOS = ' + json.dumps(caballos, ensure_ascii=False, indent=2) + ';\n')

    if cambios:
        print('Actualizado:')
        print('\n'.join(cambios))
    else:
        print('Todo estaba ya al día.')
    print('\nAhora ejecuta:  python3 construir.py')


if __name__ == '__main__':
    main()
