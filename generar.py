#!/usr/bin/env python3
"""
Generador del sitio de Yeguada Tres Tréboles.

La cabecera y el pie son idénticos en todas las páginas. En vez de copiarlos
a mano en cada .html (y arriesgarse a que se desincronicen), se definen aquí
una sola vez y este script escribe las páginas completas.

    python3 generar.py

Genera HTML plano: no hace falta ni servidor ni dependencias para verlo.
"""
import os, json, re, hashlib

_AQUI = os.path.dirname(os.path.abspath(__file__))
# El sitio puede estar en esta misma carpeta o dentro de una subcarpeta 'sitio'
RAIZ = _AQUI if os.path.exists(os.path.join(_AQUI, 'datos', 'caballos.js')) else os.path.join(_AQUI, 'sitio')

# Cada entrada del menú: (texto, enlace, submenú o None)
# El submenú es una lista de (texto, enlace, clave de recuento o None)
SUB_CABALLOS = [
    ('Sementales',            'sementales.html',            'semental'),
    ('Yeguas de cría',        'yeguas.html',                'yegua'),
    ('Nacidos en la yeguada', 'nacidos-en-la-yeguada.html', 'nacido-aqui'),
]
SUB_PUPILAJE = [
    ('En picadero',     'pupilaje-picadero.html',     None),
    ('En semilibertad', 'pupilaje-semilibertad.html', None),
]

# Los cuatro servicios van juntos en un solo desplegable: si cada uno ocupa
# su sitio arriba, el menú no cabe en un portátil.
SUB_SERVICIOS = [
    ('Cubriciones',              'cubriciones.html',           None),
    ('Pupilaje en picadero',     'pupilaje-picadero.html',     None),
    ('Pupilaje en semilibertad', 'pupilaje-semilibertad.html', None),
    ('Rutas a caballo',          'rutas.html',                 None),
    ('Clases de iniciación',     'clases.html',                None),
]

MENU = [
    ('Inicio',            'index.html',       None),
    ('La Yeguada',        'la-yeguada.html',  None),
    ('Nuestros caballos', 'caballos.html',    SUB_CABALLOS),
    ('Servicios',         'servicios.html',   SUB_SERVICIOS),
    ('En venta',          'en-venta.html',    None),
]
SUB = SUB_CABALLOS

TREBOL_SVG = ('<svg viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="1.6">'
              '<path d="M1 1.5 6 6.5 11 1.5"/></svg>')

# ---------------------------------------------------------------- redes
# Para añadir otra red: su icono en ICONO y su línea en REDES.
ICONO = {
    'instagram': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7">'
                 '<rect x="2.5" y="2.5" width="19" height="19" rx="5.4"/>'
                 '<circle cx="12" cy="12" r="4.2"/>'
                 '<circle cx="17.6" cy="6.4" r="1.15" fill="currentColor" stroke="none"/></svg>',
    'tiktok':    '<svg viewBox="0 0 24 24" fill="currentColor">'
                 '<path d="M16.6 2h-2.9v13.3a2.6 2.6 0 1 1-2.1-2.55V9.8a5.7 5.7 0 1 0 5.2 5.68V9.1a6.7 6.7 0'
                 ' 0 0 4.05 1.36V7.55A3.9 3.9 0 0 1 16.6 3.9V2Z"/></svg>',
    'facebook':  '<svg viewBox="0 0 24 24" fill="currentColor">'
                 '<path d="M14.2 22v-8.2h2.8l.42-3.23H14.2V8.5c0-.94.26-1.57 1.6-1.57h1.72V4.04A23 23 0 0 0'
                 ' 15 3.9c-2.48 0-4.18 1.51-4.18 4.3v2.37H8v3.23h2.82V22h3.38Z"/></svg>',
}

# (nombre de la red, dirección, icono, cómo se nos llama allí)
REDES = [
    ('Instagram', 'https://www.instagram.com/tres_treboles_pre/', 'instagram',
     '@tres_treboles_pre'),
    ('TikTok',    'https://www.tiktok.com/@tres_treboles_pre',    'tiktok',
     '@tres_treboles_pre'),
    ('Facebook',  'https://www.facebook.com/p/Yeguada-Tres-Tr%C3%A9boles-61558266903852/',
     'facebook',  'Yeguada Tres Tréboles'),
]


def redes_html(clase='redes'):
    if not REDES:
        return ''
    enlaces = ''.join(
        f'<a href="{url}" target="_blank" rel="noopener" aria-label="{nombre}" title="{nombre}">'
        f'{ICONO[icono]}</a>' for nombre, url, icono, _ in REDES)
    return f'<div class="{clase}">{enlaces}</div>'


def cuentas():
    """Lee los caballos de datos/caballos.js (quitándole la envoltura de JavaScript)."""
    bruto = open(os.path.join(RAIZ, 'datos', 'caballos.js'), encoding='utf-8').read()
    datos = json.loads(bruto[bruto.index('['): bruto.rindex(']') + 1])
    c = {g: sum(1 for x in datos if x['grupo'] == g) for g in ('semental', 'yegua', 'nacido-aqui', 'venta')}
    c['total'] = len(datos)
    c['en-venta'] = sum(1 for x in datos if x.get('enVenta') and not x.get('vendido'))
    return c


def cabecera(activa, ruta):
    n = cuentas()
    enlaces = []
    for texto, href, sub in MENU:
        cls = ' class="activo"' if href == activa else ''
        if sub:
            items = ''.join(
                f'<a href="{ruta}{sh}"><strong>{st}</strong>'
                + (f'<span>{n[sg]}</span>' if sg else '') + '</a>'
                for st, sh, sg in sub)
            enlaces.append(
                '<div class="desplegable">'
                f'<button type="button">{texto} {TREBOL_SVG}</button>'
                f'<div class="sub">{items}<div class="sep"></div>'
                f'<a href="{ruta}{href}"><strong>Ver todo</strong></a></div></div>')
        else:
            enlaces.append(f'<a href="{ruta}{href}"{cls}>{texto}</a>')

    partes = []
    for texto, href, sub in MENU:
        partes.append(f'<a href="{ruta}{href}">{texto}</a>')
        if sub:
            for st, sh, sg in sub:
                partes.append(f'<a class="sangria" href="{ruta}{sh}">{st}'
                              + (f'<small>{n[sg]}</small>' if sg else '') + '</a>')
    panel = ''.join(partes)

    return f'''<header class="top" id="top"><div class="wrap top-inner">
  <a class="marca" href="{ruta}index.html">
    <img class="isotipo" id="i-marca" src="{ruta}img/marca/marca-blanco.png" alt="Logotipo de Yeguada Tres Tréboles">
    <span class="marca-txt"><span class="n">Tres Tréboles</span><span class="s">Yeguada · Córdoba</span></span>
  </a>
  <nav class="principal">{''.join(enlaces)}</nav>
  <a class="btn-nav" href="{ruta}contacto.html">Contacto</a>
  <button class="hamburguesa" id="btn-menu" aria-label="Abrir menú" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</div></header>

<div class="panel" id="panel">{panel}<a href="{ruta}contacto.html">Contacto</a></div>'''


def pie(ruta):
    return f'''<footer class="pie"><div class="wrap pie-cols">
  <div class="pie-logo"><img src="{ruta}img/marca/logo-completo-blanco.png" alt="Yeguada Tres Tréboles">
    <div>Urbanización 7 Fincas · Córdoba<br><a href="tel:+34666438378">666 43 83 78</a></div></div>
  <div><strong>Pura Raza Española</strong><br>Inscritos en el Libro Genealógico del PRE
    {redes_html()}</div>
  <div><a href="{ruta}aviso-legal.html">Aviso legal</a> · <a href="{ruta}privacidad.html">Privacidad</a>
    · <a href="{ruta}cookies.html">Cookies</a></div>
</div></footer>'''


_VERSIONES = {}


def v(relativo):
    """Devuelve '?v=abc12345' a partir del contenido del archivo.

    El navegador guarda en caché el CSS, el JS y los datos. Si se publica una
    versión nueva con el mismo nombre, sigue enseñando la vieja: por eso una
    foto recién añadida no aparece hasta vaciar la caché. Añadiendo al enlace
    una marca que cambia cuando cambia el archivo, el navegador se ve obligado
    a pedirlo otra vez. Los archivos que no cambian se siguen cacheando.
    """
    if relativo not in _VERSIONES:
        try:
            with open(os.path.join(RAIZ, relativo), 'rb') as f:
                _VERSIONES[relativo] = '?v=' + hashlib.md5(f.read()).hexdigest()[:8]
        except OSError:
            _VERSIONES[relativo] = ''
    return _VERSIONES[relativo]


def pagina(archivo, titulo, descripcion, cuerpo, ruta='', clase_body='', scripts=''):
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="icon" href="{ruta}img/marca/favicon-512.png">
<link rel="apple-touch-icon" href="{ruta}img/marca/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Karla:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ruta}css/estilo.css{v('css/estilo.css')}">
</head>
<body{(' class="' + clase_body + '"') if clase_body else ''}>

{cabecera(archivo, ruta)}

{cuerpo}

{pie(ruta)}

<script>const RUTA = '{ruta}';</script>
<script src="{ruta}datos/caballos.js{v('datos/caballos.js')}"></script>
<script src="{ruta}datos/descendencia.js{v('datos/descendencia.js')}"></script>
<script src="{ruta}js/principal.js{v('js/principal.js')}"></script>
{scripts}
</body>
</html>
'''
    destino = os.path.join(RAIZ, archivo)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, 'w', encoding='utf-8').write(html)
    return destino
