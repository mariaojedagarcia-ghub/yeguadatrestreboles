#!/usr/bin/env python3
"""Contenido de cada página. Ejecutar:  python3 construir.py"""
from generar import pagina, REDES

# ============================== PORTADA ==============================
PORTADA = '''
<div class="hero">
  <div class="hero-img" style="background-image:url('img/portada/hero.jpg')"></div>
  <video class="hero-video" autoplay muted loop playsinline preload="auto"
         poster="video/sierra-poster.jpg" aria-hidden="true">
    <source src="video/sierra.mp4" type="video/mp4">
    <source src="video/sierra.webm" type="video/webm">
  </video>
  <div class="hero-velo"></div>
  <div class="wrap"><div class="hero-txt">
    <div class="sobre">Urbanización 7 Fincas · Córdoba</div>
    <h1>Yeguada<br>Tres Tréboles</h1>
    <p>Cría de caballos de Pura Raza Española en la sierra de Córdoba.</p>
    <div class="botones">
      <a class="btn btn-solido" href="la-yeguada.html">Conocer la yeguada</a>
      <a class="btn btn-linea" href="caballos.html">Ver nuestros caballos</a>
    </div>
  </div></div>
</div>

<section><div class="wrap dos">
  <div>
    <div class="et">La Yeguada</div>
    <h2 class="tit">Un proyecto que crece con cada potro</h2>
    <p class="lead">Somos una pequeña ganadería de Pura Raza Española en la sierra de Córdoba.
      Empezamos con un semental y dos yeguas, y cada año nacen aquí nuevos potros.</p>
    <a class="mas" href="la-yeguada.html">Conocer nuestra historia →</a>
  </div>
  <div class="foto-marco"><img src="img/yeguada/finca.jpg" alt="La finca de Yeguada Tres Tréboles en la sierra de Córdoba"></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="et">Nuestros caballos</div>
  <h2 class="tit">Sementales, yeguas de cría<br>y potros nacidos aquí</h2>
  <div class="tres">
    <a class="grupo" href="sementales.html"><img src="img/caballos/provinciano-sm-iii/portada.jpg" alt="Sementales PRE">
      <div class="capa"></div><div class="txt"><div class="n" data-cuenta="semental"></div><h3>Sementales</h3>
      <p>Los caballos sobre los que construimos nuestra línea.</p></div></a>
    <a class="grupo" href="yeguas.html"><img src="img/portada/yeguas.jpg" alt="Yeguas de cría PRE con sus potros en el campo">
      <div class="capa"></div><div class="txt"><div class="n" data-cuenta="yegua"></div><h3>Yeguas de cría</h3>
      <p>El corazón de la yeguada.</p></div></a>
    <a class="grupo" href="nacidos-en-la-yeguada.html"><img src="img/nacidos.jpg" alt="Potros PRE nacidos en la yeguada">
      <div class="capa"></div><div class="txt"><div class="n" data-cuenta="nacido-aqui"></div><h3>Nacidos aquí</h3>
      <p>Nuestra cría propia, año a año.</p></div></a>
  </div>
</div></section>

<div class="franja" style="background-image:url('img/portada/franja.jpg')">
  <div class="velo"></div>
  <div class="cita">Criamos donde vivimos: en la sierra de Córdoba.
    <span class="pie">Urbanización 7 Fincas · Córdoba</span></div>
</div>

<section class="fondo-papel"><div class="wrap">
  <div class="et">Lo último</div>
  <h2 class="tit">Últimos nacimientos</h2>
  <p class="lead">Cada año que pasa, la yeguada es un poco más nuestra.</p>
  <div class="nac" id="nac"></div>
</div></section>

<section class="premio"><div class="wrap dos">
  <div class="foto-marco"><img src="img/caballos/faraona-mfe/portada.jpg"
      alt="Faraona MFE, subcampeona de Europa FIECVAL 2026"></div>
  <div>
    <div class="medalla">Subcampeona de Europa · FIECVAL 2026</div>
    <div class="et">Faraona MFE</div>
    <h2 class="tit">Nuestra yegua<br>más laureada</h2>
    <p>Subcampeona en FIECVAL 2026 y campeona del mundo en la cobra de cinco de SICAB 2025.
      Antes había ganado en Equus Socuéllamos y Equus Villamanta compitiendo con nuestro nombre.</p>
    <p>Y este año ha sido madre de Saeta, nacida aquí.</p>
    <a class="mas" href="caballos/faraona-mfe.html">Ver su palmarés completo →</a>
  </div>
</div></section>

<section class="pre"><div class="wrap">
  <img class="marca-pre" src="img/marca/marca-negro.png" alt="">
  <h2 class="tit">Pura Raza Española</h2>
  <p>Yeguada Tres Tréboles nace con la ilusión de criar y disfrutar del Pura Raza Española,
    cuidando cada ejemplar y construyendo nuestro proyecto paso a paso.</p>
  <p class="nota">Todos nuestros ejemplares están inscritos en el Libro Genealógico del caballo de Pura Raza Española.</p>
</div></section>

<section class="fondo-papel"><div class="wrap">
  <div class="et">Disponibles</div>
  <h2 class="tit">Ejemplares en venta</h2>
  <div class="venta-lista" id="venta"></div>
</div></section>

<section class="rutas"><div class="wrap dos">
  <div>
    <div class="et">También ofrecemos</div>
    <h2 class="tit">Rutas a caballo<br>por la sierra</h2>
    <p class="lead">Salir a caballo por los caminos de la sierra, entre encinas y con la sierra
      de Córdoba delante. Rutas guiadas para quien quiera conocer este entorno desde el mejor sitio posible.</p>
    <a class="mas" href="rutas.html">Ver las rutas →</a>
  </div>
  <div class="foto-marco"><img src="img/servicios/rutas-02.jpg" alt="Rutas a caballo por la sierra de Córdoba"></div>
</div></section>

<section style="padding-top:0"><div class="wrap dos">
  <div class="foto-marco"><img src="img/servicios/semilibertad-01.jpg"
      alt="Caballos en pupilaje en semilibertad en la finca de Villaharta"></div>
  <div>
    <div class="et">Y también</div>
    <h2 class="tit">Pupilaje<br>en picadero o en campo</h2>
    <p class="lead">Cuidamos el caballo de otros como cuidamos los nuestros: en nuestras
      instalaciones del picadero, o en semilibertad en nuestra finca de Villaharta, en campo
      abierto y en manada.</p>
    <a class="mas" href="pupilaje.html">Ver el pupilaje →</a>
  </div>
</div></section>

<section class="contacto"><div class="wrap">
  <h2 class="tit">¿Hablamos?</h2>
  <p>Si te interesa alguno de nuestros caballos, quieres cubrir tu yegua con uno de nuestros
    sementales o te apetece salir de ruta, escríbenos sin compromiso.</p>
  <div class="vias-contacto">
    <a class="via rell" href="https://wa.me/34666438378" target="_blank" rel="noopener">WhatsApp</a>
    <a class="via" href="tel:+34666438378">Llamar 666 43 83 78</a>
    
  </div>
</div></section>
'''

pagina('index.html',
       'Yeguada Tres Tréboles — Cría de caballos PRE en Córdoba',
       'Pequeña ganadería de caballos de Pura Raza Española en la sierra de Córdoba. Cría, sementales, cubriciones y ejemplares en venta.',
       PORTADA,
       scripts="<script>pintarNacimientos('nac',4); pintarVenta('venta');</script>")


# ============================== LA YEGUADA ==============================
YEGUADA = '''
<div class="cab-pagina">
  <div class="foto-fondo" style="background-image:url('img/portada/franja.jpg')"></div>
  <div class="velo"></div>
  <div class="wrap"><div class="txt">
    <div class="migas">Yeguada Tres Tréboles</div>
    <h1>La Yeguada</h1>
    <p>Una ganadería familiar de Pura Raza Española en la sierra de Córdoba.</p>
  </div></div>
</div>

<section><div class="wrap dos">
  <div class="prosa">
    <div class="et">Nuestra historia</div>
    <h2 class="tit" style="margin-bottom:28px">Origen<br>de la yeguada</h2>
    <p>Yeguada Tres Tréboles nace de la afición de Pedro Navarro, vinculado al mundo del caballo
      desde niño. Durante años esa afición se limitó a tener caballos de montura en casa; con el
      tiempo derivó en un proyecto de cría en el que hoy participa toda la familia.</p>
    <p>La cría comenzó con Provinciano SM III, el semental sobre el que se ha construido la línea
      de la casa. A él siguieron Nerva Navero y NR Malusa, las dos primeras yeguas de vientre, y
      más adelante Faraona MFE, procedente de la ganadería de María Fernanda de la Escalera.</p>
    <p>La yeguada la compone en la actualidad una veintena de ejemplares de Pura Raza Española,
      todos inscritos en el Libro Genealógico de la raza, buena parte de ellos nacidos aquí.</p>
  </div>
  <div class="foto-marco"><img src="img/yeguada/familia.jpg"
    alt="La familia de Yeguada Tres Tréboles montando a caballo por la sierra de Córdoba"></div>
</div></section>

<section class="fondo-papel hierro"><div class="wrap dos">
  <div class="foto-marco"><img src="img/yeguada/hierro.jpg"
    alt="El hierro de Yeguada Tres Tréboles: tres tréboles en forma de corazón con el número tres"></div>
  <div class="prosa">
    <div class="et">El nombre y el hierro</div>
    <h2 class="tit" style="margin-bottom:26px">Tres Tréboles</h2>
    <p class="destacado">"Yo he sido siempre aficionado al caballo, tengo tres niños,
      por eso la ganadería se llama Tres Tréboles."</p>
    <p>El sueño era de Pedro, pero el nombre es de ellos. Y a estas alturas los caballos ya son
      de todos. Por eso esto no es un negocio de paso, sino algo que queremos que dure.</p>
    <p>De ahí sale el hierro: una hoja por cada hijo, en forma de corazón, y el tres en el
      centro. Es el hierro con el que la yeguada figura en el Libro Genealógico.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="et">Cómo criamos</div>
  <h2 class="tit">Dos formas de criar</h2>
  <p class="lead">Conviven en la yeguada y se complementan: una sostiene el día a día,
    la otra nos permite llegar más lejos.</p>
  <div class="vias">
    <div class="via-card">
      <div class="num">1</div>
      <h3>Método tradicional</h3>
      <p>Cubrición al natural a nuestras yeguas, unas veces con Provinciano y otras con
        sementales de élite de la raza. Cada año hay que decidir qué yegua va con cuál, y
        es la decisión que marca cómo será la yeguada dentro de cinco años: se mira la
        morfología, el movimiento y qué puede aportar cada cruce. Y la capa, que para
        nosotros no es un detalle.</p>
      <p>Los potros que salen de estos cruces nacen y se crían aquí, en la sierra.</p>
    </div>
    <div class="via-card">
      <div class="num">2</div>
      <h3>Transferencia de embriones</h3>
      <p>De nuestras mejores yeguas extraemos embriones que gesta una yegua receptora.
        Suele asociarse a las ganaderías grandes, pero es justo al revés:</p>
      <ul>
        <li>De una yegua superior podemos sacar varios embriones en un año y probar varios sementales.</li>
        <li>La yegua no se queda preñada, así que puede seguir compitiendo.</li>
      </ul>
    </div>
  </div>
  <div class="prosa centrado" style="margin-top:56px">
    <p class="destacado">"Para cualquier ganadero pequeñito es una manera de mejorar mucho
      la calidad de su yeguada, recortar años."</p>
  </div>
</div></section>


<section class="prensa"><div class="wrap">
  <div class="et">En los medios</div>
  <h2 class="tit">Canal Sur nos visitó</h2>
  <div class="prensa-caja">
    <div>
      <p>El programa <em>TodoCaballo</em> vino hasta la sierra para conocer la yeguada,
        ver una transferencia de embriones y salir a dar un paseo a caballo con nosotros.</p>
      <p class="ref">TodoCaballo · Canal Sur · marzo de 2026</p>
    </div>
    <a class="btn-prensa" href="https://www.canalsur.es/television/todo-caballo/yeguada-3-treboles-comparte-familia_1_1390242.html"
       target="_blank" rel="noopener">Ver el reportaje →</a>
  </div>
</div></section>

<section class="fondo-papel"><div class="wrap dos">
  <div class="prosa">
    <div class="et">La capa</div>
    <h2 class="tit" style="margin-bottom:26px">Castaña y negra</h2>
    <p class="destacado">"Hemos intentado apostar por la capa castaña y la negra,
      que es lo que siempre me ha gustado."</p>
    <p>No es casualidad: son las dos capas hacia las que dirigimos los cruces. La castaña es
      la más frecuente en la yeguada y la negra aparece con regularidad, unas veces por parte
      de padre y otras de madre.</p>
  </div>
  <div class="foto-marco"><img src="img/caballos/provinciano-sm-iii/portada.jpg"
    alt="Provinciano SM III, semental PRE de capa negra">
    <span class="credito">Foto: Salvador Giménez Fotografía</span></div>
</div></section>

<section class="pre"><div class="wrap">
  <img class="marca-pre" src="img/marca/marca-negro.png" alt="">
  <h2 class="tit">Pura Raza Española</h2>
  <p>Yeguada Tres Tréboles nace con la ilusión de criar y disfrutar del Pura Raza Española,
    cuidando cada ejemplar y construyendo nuestro proyecto paso a paso.</p>
  <p class="nota">Todos nuestros ejemplares están inscritos en el Libro Genealógico del caballo
    de Pura Raza Española. En la ficha de cada caballo puedes ver su carta genealógica.</p>
</div></section>

<section><div class="wrap dos">
  <div>
    <div class="et">Dónde estamos</div>
    <h2 class="tit">Urbanización<br>7 Fincas</h2>
    <p class="lead">En pleno corazón de la sierra de Córdoba, en la zona de Santa María de
      Trassierra, entre encinas y caminos. Los caballos viven donde vivimos nosotros.</p>
    <p class="lead" style="font-size:16.5px;color:var(--suave)">Se visita con cita previa.
      Si quieres conocer la yeguada, escríbenos.</p>
    <a class="mas" href="contacto.html">Cómo llegar →</a>
  </div>
  <div class="mapa">
    <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de Yeguada Tres Tréboles"
      src="https://maps.google.com/maps?q=W4PM%2BP7%2C%2014192%20Santa%20Mar%C3%ADa%20de%20Trassierra%2C%20C%C3%B3rdoba&amp;z=15&amp;output=embed"></iframe>
  </div>
</div></section>

<section class="contacto"><div class="wrap">
  <h2 class="tit">¿Quieres conocernos?</h2>
  <p>Estaremos encantados de enseñarte la yeguada y nuestros caballos.</p>
  <div class="vias-contacto">
    <a class="via rell" href="https://wa.me/34666438378" target="_blank" rel="noopener">WhatsApp</a>
    <a class="via" href="tel:+34666438378">Llamar 666 43 83 78</a>
  </div>
</div></section>
'''

pagina('la-yeguada.html',
       'La Yeguada — Ganadería de Pura Raza Española en Córdoba | Tres Tréboles',
       'La historia de Yeguada Tres Tréboles: una ganadería familiar de caballos de Pura Raza Española en la sierra de Córdoba. Cría propia y transferencia de embriones.',
       YEGUADA)


# ============================== BLOQUES REUTILIZABLES ==============================
def cab(titulo, bajada, migas, foto="img/portada/franja.jpg"):
    return f'''
<div class="cab-pagina">
  <div class="foto-fondo" style="background-image:url('{foto}')"></div>
  <div class="velo"></div>
  <div class="wrap"><div class="txt">
    <div class="migas">{migas}</div>
    <h1>{titulo}</h1>
    <p>{bajada}</p>
  </div></div>
</div>'''

CONTACTO_FRANJA = '''
<section class="contacto"><div class="wrap">
  <h2 class="tit">¿Hablamos?</h2>
  <p>Escríbenos sin compromiso. Estaremos encantados de enseñarte la yeguada.</p>
  <div class="vias-contacto">
    <a class="via rell" href="https://wa.me/34666438378" target="_blank" rel="noopener">WhatsApp</a>
    <a class="via" href="tel:+34666438378">Llamar 666 43 83 78</a>
  </div>
</div></section>'''

FILTROS = '''
    <div class="filtros">
      <div class="fila-filtro" data-filtro="capa">
        <span class="et-f">Capa</span>
        <button class="chip" data-valor="todos" aria-pressed="true">Todas</button>
        <button class="chip" data-valor="Castaña" aria-pressed="false">Castaña</button>
        <button class="chip" data-valor="Negra" aria-pressed="false">Negra</button>
        <button class="chip" data-valor="Torda" aria-pressed="false">Torda</button>
        <button class="chip" data-valor="Bayo" aria-pressed="false">Bayo</button>
      </div>
      <div class="fila-filtro" data-filtro="sexo">
        <span class="et-f">Sexo</span>
        <button class="chip" data-valor="todos" aria-pressed="true">Todos</button>
        <button class="chip" data-valor="M" aria-pressed="false">Machos</button>
        <button class="chip" data-valor="H" aria-pressed="false">Hembras</button>
      </div>
      <div class="recuento" id="recuento"></div>
    </div>'''


def pagina_grupo(archivo, titulo, h1, bajada, intro, base_js, meta):
    cuerpo = cab(h1, bajada, 'Nuestros caballos') + f'''
<section><div class="wrap">
  <p class="lead" style="max-width:66ch;margin-top:0">{intro}</p>
  {FILTROS}
  <div class="rejilla" id="rejilla"></div>
</div></section>
{CONTACTO_FRANJA}'''
    pagina(archivo, titulo, meta, cuerpo,
           scripts=f"<script>activarFiltros('rejilla', {base_js});</script>")


# ============================== ÍNDICE DE CABALLOS ==============================
INDICE = cab('Nuestros caballos',
             'Nuestros caballos de Pura Raza Española, todos inscritos en el Libro Genealógico de la raza.',
             'Yeguada Tres Tréboles') + '''
<section><div class="wrap">
  <div class="filtros">
    <div class="fila-filtro" data-filtro="grupo">
      <span class="et-f">Grupo</span>
      <button class="chip" data-valor="todos" aria-pressed="true">Todos</button>
      <button class="chip" data-valor="semental" aria-pressed="false">Sementales</button>
      <button class="chip" data-valor="yegua" aria-pressed="false">Yeguas de cría</button>
      <button class="chip" data-valor="nacido-aqui" aria-pressed="false">Nacidos aquí</button>
      <button class="chip" data-valor="en-venta" aria-pressed="false">En venta</button>
    </div>
    <div class="fila-filtro" data-filtro="capa">
      <span class="et-f">Capa</span>
      <button class="chip" data-valor="todos" aria-pressed="true">Todas</button>
      <button class="chip" data-valor="Castaña" aria-pressed="false">Castaña</button>
      <button class="chip" data-valor="Negra" aria-pressed="false">Negra</button>
      <button class="chip" data-valor="Torda" aria-pressed="false">Torda</button>
      <button class="chip" data-valor="Bayo" aria-pressed="false">Bayo</button>
    </div>
    <div class="fila-filtro" data-filtro="sexo">
      <span class="et-f">Sexo</span>
      <button class="chip" data-valor="todos" aria-pressed="true">Todos</button>
      <button class="chip" data-valor="M" aria-pressed="false">Machos</button>
      <button class="chip" data-valor="H" aria-pressed="false">Hembras</button>
    </div>
    <div class="recuento" id="recuento"></div>
  </div>
  <div class="rejilla" id="rejilla"></div>
</div></section>
''' + CONTACTO_FRANJA

pagina('caballos.html', 'Nuestros caballos PRE | Yeguada Tres Tréboles',
       'Los caballos de Pura Raza Española de Yeguada Tres Tréboles: sementales, yeguas de cría, potros nacidos en la yeguada y ejemplares en venta.',
       INDICE, scripts="<script>activarFiltros('rejilla', null);</script>")

pagina_grupo('sementales.html', 'Sementales PRE | Yeguada Tres Tréboles', 'Sementales',
             'Los caballos sobre los que construimos nuestra línea.',
             'Provinciano es el semental con el que empezó la cría de la yeguada y padre de casi todos nuestros potros. Tatami es la apuesta joven. Ambos están disponibles para cubrición.',
             "c => c.grupo === 'semental'",
             'Sementales de Pura Raza Española de Yeguada Tres Tréboles, en Córdoba. Disponibles para cubrición.')

pagina_grupo('yeguas.html', 'Yeguas de cría PRE | Yeguada Tres Tréboles', 'Yeguas de cría',
             'El corazón de la yeguada.',
             'De ellas sale todo lo demás. Nerva, Malusa, Utrera y Faraona ya han criado aquí; el resto son la base de los próximos años. Varias proceden de la ganadería María Fernanda de la Escalera.',
             "c => c.grupo === 'yegua'",
             'Yeguas de cría de Pura Raza Española de Yeguada Tres Tréboles, en la sierra de Córdoba.')

pagina_grupo('nacidos-en-la-yeguada.html', 'Potros nacidos en la yeguada | Tres Tréboles',
             'Nacidos en la yeguada', 'Nuestra cría propia, año a año.',
             'Los potros nacidos en la yeguada, de nuestras yeguas y nuestros sementales. Llevan el nombre de la casa y son la razón de todo esto. Algunos siguen aquí y otros ya han salido a otras manos; todos nacieron en esta finca.',
             "c => c.grupo === 'nacido-aqui'",
             'Potros PRE nacidos en Yeguada Tres Tréboles, en la sierra de Córdoba. Cría propia de Pura Raza Española.')


# ============================== EN VENTA ==============================
VENTA = cab('Ejemplares en venta', 'Caballos de Pura Raza Española disponibles.', 'Yeguada Tres Tréboles') + '''
<section><div class="wrap">
  <p class="lead" style="max-width:66ch;margin-top:0">Todos nuestros ejemplares están inscritos en el
    Libro Genealógico del PRE y se entregan con su documentación en regla. El precio no se publica:
    escríbenos y hablamos.</p>
  <div class="rejilla" id="rejilla"></div>
</div></section>
''' + CONTACTO_FRANJA

pagina('en-venta.html', 'Caballos PRE en venta | Yeguada Tres Tréboles',
       'Caballos de Pura Raza Española en venta en Yeguada Tres Tréboles, Córdoba. Potros y yeguas inscritos en el Libro Genealógico del PRE.',
       VENTA, scripts="<script>pintarRejilla('rejilla', c => c.enVenta && !c.vendido);</script>")


# ============================== CUBRICIONES ==============================
CUBRICIONES = cab('Cubriciones', 'Nuestros sementales, disponibles para tu yegua.', 'Servicios') + '''
<section><div class="wrap">
  <p class="lead" style="max-width:66ch;margin-top:0">Ofrecemos nuestros sementales para cubrición.
    Son los mismos caballos con los que criamos nosotros: lo que ves en nuestros potros es lo que
    puedes esperar.</p>
  <div class="rejilla" id="rejilla"></div>
  <div class="enlaces-hijos">
    <a class="ver-arbol" href="hijos-de-provinciano-sm-iii.html">Ver los hijos de Provinciano</a>
    <a class="ver-arbol" href="hijos-de-tatami-jmg.html">Ver los hijos de Tatami</a>
  </div>
</div></section>

<section class="fondo-papel"><div class="wrap">
  <div class="et">Condiciones</div>
  <h2 class="tit">Cómo funciona</h2>
  <div class="vias">
    <div class="via-card">
      <h3>Modalidades</h3>
      <p class="pendiente">Pendiente de definir: monta natural, inseminación en fresco o refrigerado.</p>
    </div>
    <div class="via-card">
      <h3>Tarifas y garantía</h3>
      <p class="pendiente">Pendiente de definir: precio de la cubrición, garantía de preñez y gastos
        de mantenimiento si la yegua se queda en la yeguada.</p>
    </div>
  </div>
  <p class="lead" style="margin-top:34px">Si tu yegua viene a cubrición, puede quedarse con
    nosotros el tiempo que necesite: <a href="pupilaje-picadero.html">ver el pupilaje en
    picadero</a>.</p>
  <p class="lead" style="margin-top:34px"><em>Esta página no debería publicarse hasta tener las
    condiciones cerradas.</em></p>
</div></section>
''' + CONTACTO_FRANJA

pagina('cubriciones.html', 'Cubriciones PRE en Córdoba | Yeguada Tres Tréboles',
       'Cubriciones con sementales de Pura Raza Española en Córdoba. Provinciano SM III y Tatami JMG, de Yeguada Tres Tréboles.',
       CUBRICIONES, scripts="<script>pintarRejilla('rejilla', c => c.cubriciones);</script>")


# ============================== RUTAS ==============================
RUTAS = cab('Rutas a caballo', 'Por los caminos de la sierra de Córdoba.', 'Servicios',
            'img/servicios/rutas-04.jpg') + '''
<section><div class="wrap dos">
  <div class="prosa">
    <div class="et">Las rutas</div>
    <h2 class="tit" style="margin-bottom:26px">Conocer la sierra<br>desde el mejor sitio</h2>
    <p>Salir a caballo entre encinas, con la sierra de Córdoba delante y sin más ruido que el de
      los cascos. Rutas guiadas por los caminos que recorremos todos los días, con nuestros
      propios caballos y acompañados en todo momento.</p>
    <p>No hace falta ser jinete: adaptamos el caballo y el recorrido a quien viene. Para los que
      ya montan, la sierra da para mucho más.</p>
    <p class="pendiente">Pendiente de indicar: modalidades, duración, recorrido, nivel de monta
      necesario, edad mínima, qué incluye y precios.</p>
  </div>
  <div class="foto-marco"><img src="img/servicios/rutas-01.jpg" alt="Parada durante una ruta a caballo por la sierra de Córdoba"></div>
</div></section>

<section class="fondo-papel"><div class="wrap">
  <div class="et">Por los caminos</div>
  <h2 class="tit">Así son las salidas</h2>
  <div id="galeria-rutas"></div>
</div></section>

<section><div class="wrap centrado prosa">
  <p><em>Antes de publicar esta página hay que confirmar la situación respecto a la normativa
    de turismo activo de Andalucía y el seguro de responsabilidad civil.</em></p>
</div></section>
''' + CONTACTO_FRANJA

MEDIA_RUTAS = """<script>pintarCarrusel('galeria-rutas', [
  {tipo:'video', archivo:'video/rutas.mp4',              poster:'video/rutas-poster.jpg',           pie:'De ruta por la sierra'},
  {tipo:'foto',  archivo:'img/servicios/rutas-04.jpg',   pie:'Al paso por el campo'},
  {tipo:'video', archivo:'img/servicios/rutas-v3.mp4',   poster:'img/servicios/rutas-v3-poster.jpg', pie:'Desde el aire'},
  {tipo:'foto',  archivo:'img/servicios/rutas-02.jpg',   pie:'La sierra de Córdoba'},
  {tipo:'video', archivo:'img/servicios/rutas-v2.mp4',   poster:'img/servicios/rutas-v2-poster.jpg', pie:'Por el camino'},
  {tipo:'foto',  archivo:'img/servicios/rutas-03.jpg',   pie:'Entre encinas'},
  {tipo:'video', archivo:'img/servicios/rutas-v1.mp4',   poster:'img/servicios/rutas-v1-poster.jpg', pie:'En marcha'},
  {tipo:'foto',  archivo:'img/servicios/rutas-01.jpg',   pie:'Un alto en el camino'},
  {tipo:'foto',  archivo:'img/servicios/rutas-05.jpg',   pie:'Por la sierra'},
  {tipo:'video', archivo:'img/servicios/rutas-v5.mp4',  poster:'img/servicios/rutas-v5-poster.jpg', pie:'Al paso'},
  {tipo:'foto',  archivo:'img/servicios/rutas-06.jpg',   pie:'Camino arriba'},
  {tipo:'video', archivo:'img/servicios/rutas-v4.mp4',   poster:'img/servicios/rutas-v4-poster.jpg', pie:'Saliendo de la finca'}
]);</script>"""

pagina('rutas.html', 'Rutas a caballo por la sierra de Córdoba | Tres Tréboles',
       'Rutas guiadas a caballo por la sierra de Córdoba, desde Yeguada Tres Tréboles.',
       RUTAS, scripts=MEDIA_RUTAS)


# ============================== CLASES DE INICIACIÓN ==============================
CLASES = cab('Clases de iniciación', 'Aprender a montar desde cero, en la sierra de Córdoba.',
             'Servicios', 'img/servicios/picadero-02.jpg') + """
<section><div class="wrap dos">
  <div class="prosa">
    <div class="et">Las clases</div>
    <h2 class="tit" style="margin-bottom:26px">Empezar de cero,<br>sin prisa</h2>
    <p>Clases de iniciación para niños y adultos que nunca han montado. Se aprende con
      nuestros caballos, en nuestro picadero, y se empieza por donde hay que empezar:
      acercarse al caballo, cepillarlo, entender cómo funciona y perderle el respeto justo.</p>
    <p>No hace falta traer nada ni saber nada. Solo son clases de iniciación: cuando alguien
      pasa de ahí, lo natural es salir al campo con nosotros de ruta.</p>
    <p class="pendiente">Pendiente de indicar: duración y frecuencia de las clases, edad mínima,
      si son individuales o en grupo, qué hay que traer y precios.</p>
  </div>
  <div class="foto-marco"><img src="img/servicios/clases-03.jpg"
    alt="Clase de iniciación a caballo en el picadero de Yeguada Tres Tréboles"></div>
</div></section>

<section class="fondo-papel"><div class="wrap">
  <div class="et">En el picadero</div>
  <h2 class="tit">Así son las clases</h2>
  <div id="galeria-clases"></div>
</div></section>

<section><div class="wrap centrado prosa">
  <p><em>Antes de publicar esta página hay que confirmar la parte legal: seguro de
    responsabilidad civil y titulación necesaria para impartir clases.</em></p>
</div></section>
""" + CONTACTO_FRANJA

MEDIA_CLASES = """<script>pintarCarrusel('galeria-clases', [
  {tipo:'foto', archivo:'img/servicios/clases-03.jpg',   pie:'Siempre acompañados'},
  {tipo:'foto', archivo:'img/servicios/clases-01.jpg',   pie:'Primeros pasos, con casco'},
  {tipo:'foto', archivo:'img/servicios/clases-02.jpg',   pie:'En la pista'},
  {tipo:'foto', archivo:'img/servicios/clases-04.jpg',   pie:'Clase al atardecer'},
  {tipo:'foto', archivo:'img/servicios/picadero-02.jpg', pie:'El picadero'}
]);</script>"""

pagina('clases.html', 'Clases de iniciación a caballo en Córdoba | Tres Tréboles',
       'Clases de iniciación a la monta para niños y adultos en la sierra de Córdoba, '
       'en el picadero de Yeguada Tres Tréboles.',
       CLASES, scripts=MEDIA_CLASES)


# ============================== SERVICIOS (índice) ==============================
SERVICIOS = cab('Servicios', 'Todo lo que hacemos, además de criar.', 'Yeguada Tres Tréboles',
                'img/servicios/rutas-04.jpg') + """
<section><div class="wrap">
  <p class="lead" style="max-width:66ch;margin-top:0">La yeguada es lo primero, pero no lo único.
    Estos son los servicios que ofrecemos, todos con nuestros caballos y en nuestras
    instalaciones de la sierra de Córdoba.</p>

  <div class="vias" style="margin-top:50px">
    <div class="via-card">
      <h3>Cubriciones</h3>
      <p>Nuestros sementales para tu yegua. Los mismos con los que criamos nosotros.</p>
      <p><a class="mas" href="cubriciones.html">Ver las cubriciones →</a></p>
    </div>
    <div class="via-card">
      <h3>Pupilaje</h3>
      <p>Guardamos y cuidamos tu caballo: en el picadero, o en semilibertad en nuestra
        finca de Villaharta.</p>
      <p><a class="mas" href="pupilaje.html">Ver el pupilaje →</a></p>
    </div>
    <div class="via-card">
      <h3>Rutas a caballo</h3>
      <p>Salidas guiadas por los caminos de la sierra, con nuestros caballos.</p>
      <p><a class="mas" href="rutas.html">Ver las rutas →</a></p>
    </div>
    <div class="via-card">
      <h3>Clases de iniciación</h3>
      <p>Para niños y adultos que empiezan de cero, en nuestro picadero.</p>
      <p><a class="mas" href="clases.html">Ver las clases →</a></p>
    </div>
  </div>
</div></section>
""" + CONTACTO_FRANJA

pagina('servicios.html', 'Servicios | Yeguada Tres Tréboles',
       'Cubriciones, pupilaje, rutas a caballo y clases de iniciación en Yeguada Tres Tréboles, '
       'en la sierra de Córdoba.',
       SERVICIOS)


# ============================== PUPILAJE ==============================
NOTA_PRECIOS = ('<p class="pendiente">Pendiente de indicar: tarifas mensuales, qué incluye cada '
                'modalidad y condiciones de entrada.</p>')

PUPILAJE = cab('Pupilaje', 'Tu caballo, cuidado como si fuera nuestro.', 'Servicios',
               'img/servicios/semilibertad-01.jpg') + '''
<section><div class="wrap">
  <p class="lead" style="max-width:66ch;margin-top:0">Guardamos y cuidamos el caballo de otros
    en dos modalidades muy distintas, para que cada uno esté donde mejor le venga: en nuestras
    instalaciones del picadero, o en semilibertad en nuestra finca de Villaharta, en campo
    abierto y en manada.</p>

  <div class="vias">
    <div class="via-card">
      <h3>En picadero</h3>
      <p>En nuestras instalaciones de la sierra de Córdoba. Cuadra y pista, para quien no tiene
        dónde guardar su caballo y quiere venir a montarlo cuando quiera, y para las yeguas
        que vienen a cubrición.</p>
      <p><a class="mas" href="pupilaje-picadero.html">Ver el pupilaje en picadero →</a></p>
    </div>
    <div class="via-card">
      <h3>En semilibertad</h3>
      <p>En nuestra finca de Villaharta. El caballo vive en campo, en grupo, moviéndose todo el
        día. La opción más natural para descanso, recría y yeguas de vientre.</p>
      <p><a class="mas" href="pupilaje-semilibertad.html">Ver el pupilaje en semilibertad →</a></p>
    </div>
  </div>

  ''' + NOTA_PRECIOS + '''
</div></section>
''' + CONTACTO_FRANJA

pagina('pupilaje.html', 'Pupilaje de caballos en Córdoba | Yeguada Tres Tréboles',
       'Pupilaje de caballos en Córdoba: en picadero, en nuestras instalaciones, o en semilibertad '
       'en nuestra finca de Villaharta. Yeguada Tres Tréboles.',
       PUPILAJE)


PICADERO = cab('Pupilaje en picadero', 'En nuestras instalaciones, en la sierra de Córdoba.',
               'Servicios · Pupilaje', 'img/servicios/picadero-01.jpg') + '''
<section><div class="wrap dos">
  <div class="prosa">
    <div class="et">En nuestras instalaciones</div>
    <h2 class="tit" style="margin-bottom:26px">Un sitio para tu caballo,<br>a un rato de Córdoba</h2>
    <p>El caballo se queda con nosotros en el picadero, en la Urbanización 7 Fincas. Nos
      encargamos de tenerlo bien: su cuadra, su comida y su sitio, cuidado como cuidamos
      los nuestros.</p>
    <p>Es la solución para quien no tiene dónde guardar su caballo y quiere venir a montarlo
      cuando le apetezca, sin depender de nadie. También para las yeguas que vienen a que las
      cubra nuestro semental y se quedan aquí el tiempo que necesiten.</p>
    <ul class="datos" style="margin-top:26px">
      <li><span>Dónde</span><span>Urbanización 7 Fincas · Córdoba</span></li>
      <li><span>Modalidad</span><span>Cuadra y pista</span></li>
      <li><span>Para</span><span>Guardar tu caballo · Yeguas de cubrición</span></li>
    </ul>
  </div>
  <div class="foto-marco"><img src="img/servicios/picadero-02.jpg" alt="Instalaciones del picadero de Yeguada Tres Tréboles"></div>
</div></section>

<section class="fondo-papel"><div class="wrap">
  <div class="et">Las instalaciones</div>
  <h2 class="tit">Dónde estarían</h2>
  <div id="galeria-picadero"></div>
  ''' + NOTA_PRECIOS + '''
</div></section>
''' + CONTACTO_FRANJA

MEDIA_PICADERO = """<script>pintarCarrusel('galeria-picadero', [
  {tipo:'foto', archivo:'img/servicios/picadero-01.jpg', pie:'Las instalaciones desde el aire'},
  {tipo:'foto', archivo:'img/servicios/picadero-02.jpg', pie:'La pista'},
  {tipo:'foto', archivo:'img/servicios/picadero-03.jpg', pie:'La finca'}
]);</script>"""

pagina('pupilaje-picadero.html', 'Pupilaje en picadero en Córdoba | Yeguada Tres Tréboles',
       'Pupilaje de caballos en picadero en Córdoba: guardamos tu caballo en nuestras instalaciones '
       'y vienes a montarlo cuando quieras. También yeguas de cubrición. Yeguada Tres Tréboles.',
       PICADERO, scripts=MEDIA_PICADERO)


SEMILIBERTAD = cab('Pupilaje en semilibertad', 'En nuestra finca de Villaharta.',
                   'Servicios · Pupilaje', 'img/servicios/semilibertad-02.jpg') + '''
<section><div class="wrap dos">
  <div class="prosa">
    <div class="et">Villaharta</div>
    <h2 class="tit" style="margin-bottom:26px">Vivir en el campo,<br>como debe ser</h2>
    <p>En nuestra finca de Villaharta, en pleno valle del Guadiato, los caballos viven en
      semilibertad: en campo abierto, en manada y moviéndose durante todo el día.</p>
    <p>Es la forma de vida que mejor les sienta. Se nota en las patas, en la cabeza y en el
      carácter. Lo usamos con nuestras propias yeguas y con los potros, y lo ofrecemos también
      a quien quiera dar un descanso a su caballo, criar o recriar en condiciones naturales.</p>
    <ul class="datos" style="margin-top:26px">
      <li><span>Dónde</span><span>Finca en Villaharta · Córdoba</span></li>
      <li><span>Modalidad</span><span>Campo abierto, en manada</span></li>
      <li><span>Para</span><span>Descanso, recría, yeguas de vientre</span></li>
    </ul>
  </div>
  <div class="foto-marco"><img src="img/servicios/semilibertad-03.jpg" alt="Caballos en semilibertad en la finca de Villaharta"></div>
</div></section>

<section class="fondo-papel"><div class="wrap">
  <div class="et">La finca</div>
  <h2 class="tit">Villaharta</h2>
  <div id="galeria-semi"></div>
  ''' + NOTA_PRECIOS + '''
</div></section>
''' + CONTACTO_FRANJA

MEDIA_SEMI = """<script>pintarCarrusel('galeria-semi', [
  {tipo:'foto', archivo:'img/servicios/semilibertad-01.jpg', pie:'La finca de Villaharta'},
  {tipo:'foto', archivo:'img/servicios/semilibertad-02.jpg', pie:'En manada, en campo abierto'},
  {tipo:'foto', archivo:'img/servicios/semilibertad-03.jpg', pie:'Vida en semilibertad'}
]);</script>"""

pagina('pupilaje-semilibertad.html', 'Pupilaje en semilibertad en Villaharta | Tres Tréboles',
       'Pupilaje de caballos en semilibertad en nuestra finca de Villaharta, Córdoba. '
       'Campo abierto y vida en manada. Yeguada Tres Tréboles.',
       SEMILIBERTAD, scripts=MEDIA_SEMI)


# ============================== CONTACTO ==============================
CONTACTO = cab('Contacto', 'Estaremos encantados de enseñarte la yeguada.', 'Yeguada Tres Tréboles') + '''
<section><div class="wrap dos">
  <div class="prosa">
    <div class="et">Escríbenos</div>
    <h2 class="tit" style="margin-bottom:26px">Hablamos<br>cuando quieras</h2>
    <p>Si te interesa alguno de nuestros caballos, quieres cubrir tu yegua con uno de nuestros
      sementales o te apetece salir de ruta, escríbenos sin compromiso.</p>
    <p>La yeguada se visita con cita previa.</p>
    <ul class="datos" style="margin-top:30px">
      <li><span>Teléfono</span><span><a href="tel:+34666438378">666 43 83 78</a></span></li>
      <li><span>WhatsApp</span><span><a href="https://wa.me/34666438378" target="_blank" rel="noopener">666 43 83 78</a></span></li>
      <li><span>Dirección</span><span>Urbanización 7 Fincas<br>W4PM+P7, 14192<br>Santa María de Trassierra, Córdoba</span></li>
''' + ''.join(
      f'<li><span>{n}</span><span><a href="{u}" target="_blank" rel="noopener">'
      f'{q}</a></span></li>' for n, u, _, q in REDES) + '''
    </ul>
  </div>
  <div>
    <form class="formulario" onsubmit="return false">
      <label>Nombre<input type="text" name="nombre" required></label>
      <label>Email<input type="email" name="email" required></label>
      <label>Teléfono<input type="tel" name="telefono"></label>
      <label>Motivo
        <select name="motivo">
          <option>Comprar un caballo</option>
          <option>Cubrición</option>
          <option>Rutas a caballo</option>
          <option>Información general</option>
        </select>
      </label>
      <label>Mensaje<textarea name="mensaje" rows="5"></textarea></label>
      <button class="cta" type="submit">Enviar</button>
      <p class="falta-form">El formulario todavía no envía: falta conectarlo a un servicio de correo.</p>
    </form>
  </div>
</div></section>

<section class="fondo-papel"><div class="wrap">
  <div class="et">Dónde estamos</div>
  <h2 class="tit" style="margin-bottom:14px">Urbanización 7 Fincas</h2>
  <p class="lead" style="margin:0 0 30px">W4PM+P7, 14192 Santa María de Trassierra, Córdoba</p>
  <div class="mapa">
    <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de Yeguada Tres Tréboles"
      src="https://maps.google.com/maps?q=W4PM%2BP7%2C%2014192%20Santa%20Mar%C3%ADa%20de%20Trassierra%2C%20C%C3%B3rdoba&amp;z=15&amp;output=embed"></iframe>
  </div>
</div></section>
'''

pagina('contacto.html', 'Contacto | Yeguada Tres Tréboles',
       'Contacta con Yeguada Tres Tréboles, ganadería de caballos PRE en la Urbanización 7 Fincas, Córdoba.',
       CONTACTO)


# ============================== FICHAS ==============================
import json
from generar import cuentas, RAIZ
import os
_b = open(os.path.join(RAIZ, 'datos', 'caballos.js'), encoding='utf-8').read()
datos = json.loads(_b[_b.index('['): _b.rindex(']') + 1])
GRUPO_TXT = {'semental':'Semental', 'yegua':'Yegua de cría',
             'nacido-aqui':'Nacido en la yeguada', 'venta':'En venta'}

for c in datos:
    anio = c['nacimiento'][:4]
    sexo = 'macho' if c['sexo'] == 'M' else 'hembra'
    padres = ''
    if c.get('padre') and c.get('madre'):
        padres = f", hijo{'' if c['sexo']=='M' else 'a'} de {c['padre']} y {c['madre']}"
    meta = (f"{c['nombre']}, {sexo} de Pura Raza Española nacido en {anio}{padres}. "
            f"Yeguada Tres Tréboles, cría de PRE en Córdoba.")
    pagina(f"caballos/{c['slug']}.html",
           f"{c['nombre']} — Caballo PRE | Yeguada Tres Tréboles",
           meta,
           '<div class="wrap" id="ficha"></div>',
           ruta='../', clase_body='sin-hero',
           scripts=f"<script>pintarFicha('{c['slug']}');</script>")

print(f'Generadas {len(datos)} fichas + 9 páginas de sección.')

# ============================== HIJOS DE CADA SEMENTAL ==============================
SEMENTALES = [c for c in datos if c.get('cubriciones')]

for s in SEMENTALES:
    corto = s['nombre'].split(' ')[0]
    en_casa = [c for c in datos if c.get('padreSlug') == s['slug']]
    cuerpo = cab(f"Hijos de {corto}",
                 f"La descendencia de {s['nombre']}, dentro y fuera de la yeguada.",
                 s['nombre']) + f'''
<section><div class="wrap">
  <p class="lead" style="max-width:66ch;margin-top:0">A un semental se le juzga por sus hijos.
    Aquí están todos los de {corto}: los que han nacido en la yeguada y los que han nacido
    en casa de otros criadores que confiaron en él.</p>
  <div class="recuento" id="recuento" style="border-top:0;margin-top:26px"></div>
  <div class="rejilla" id="hijos" style="padding-top:20px"></div>
</div></section>

<section class="fondo-papel"><div class="wrap dos">
  <div>
    <div class="et">Cubriciones</div>
    <h2 class="tit">¿Quieres un hijo<br>de {corto}?</h2>
    <p class="lead">{s['nombre']} está disponible para cubrir. Escríbenos y te contamos
      condiciones y disponibilidad.</p>
    <a class="mas" href="cubriciones.html">Ver cubriciones →</a>
  </div>
  <div class="foto-marco"><img src="img/caballos/{s['slug']}/portada.jpg" alt="{s['nombre']}"
    onerror="this.style.display='none'"></div>
</div></section>
''' + CONTACTO_FRANJA

    pagina(f"hijos-de-{s['slug']}.html",
           f"Hijos de {s['nombre']} — Sementales PRE | Yeguada Tres Tréboles",
           f"Descendencia de {s['nombre']}, semental de Pura Raza Española de Yeguada Tres Tréboles, "
           f"en Córdoba. Potros nacidos en la yeguada y en otras ganaderías.",
           cuerpo,
           scripts=f"<script>pintarHijos('{s['slug']}', 'hijos');</script>")

print(f'Generadas {len(SEMENTALES)} páginas de descendencia.')


# ============================== COMPROBACIÓN FINAL ==============================
# Que ninguna página apunte a una imagen, un vídeo o una hoja de estilos que no
# existe. Un enlace roto no se nota al mirar el código: se nota cuando alguien
# abre la web y ve un hueco. Mejor que salte aquí.
def _existe_exacto(ruta):
    """¿Existe el archivo con EXACTAMENTE ese nombre?

    os.path.exists() no vale: macOS no distingue mayúsculas, así que da por
    bueno 'clases-02.jpg' cuando en el disco pone 'clases-02.JPG'. El servidor
    web sí distingue, y ahí la foto sale rota. Comparando contra el listado de
    la carpeta la diferencia se ve.
    """
    ruta = ruta.split('?')[0]
    carpeta, nombre = os.path.dirname(ruta), os.path.basename(ruta)
    try:
        return nombre in os.listdir(carpeta or '.')
    except OSError:
        return False


def _comprobar_archivos():
    import glob
    faltan = []
    patrones = (r'(?:src|href)="([^"#?:]+\.(?:jpg|jpeg|png|webp|mp4|webm|css|js))"',
                r"archivo:'([^']+)'", r"poster:'([^']+)'")
    for f in (glob.glob(os.path.join(RAIZ, '*.html'))
              + glob.glob(os.path.join(RAIZ, 'caballos', '*.html'))):
        base = os.path.dirname(f)
        txt = open(f, encoding='utf-8').read()
        for pat in patrones:
            for m in re.findall(pat, txt):
                if m.startswith(('http', '//')):
                    continue
                ruta = (os.path.join(RAIZ, m) if m.split('/')[0] in
                        ('img', 'video', 'css', 'js', 'datos')
                        else os.path.normpath(os.path.join(base, m)))
                if not _existe_exacto(ruta):
                    faltan.append((os.path.basename(f), m))

    # las fotos que salen de datos/caballos.js
    datos_js = json.loads(_b[_b.index('['): _b.rindex(']') + 1])
    for c in datos_js:
        carpeta = os.path.join(RAIZ, 'img', 'caballos', c['slug'])
        refs = list(c.get('fotos') or [])
        refs += [v['archivo'] for v in (c.get('videos') or [])]
        refs += [v['poster'] for v in (c.get('videos') or []) if v.get('poster')]
        if c.get('arbol'):
            refs.append(c['arbol'])
        for r in refs:
            if not _existe_exacto(os.path.join(carpeta, r)):
                faltan.append((c['nombre'], f"img/caballos/{c['slug']}/{r}"))

    faltan = sorted(set(faltan))
    if faltan:
        print(f'\n  ¡OJO! {len(faltan)} archivo(s) enlazados que no existen:')
        for donde, que in faltan:
            print(f'    {donde}  ->  {que}')
        print('  Esas imágenes saldrán rotas en la web.')
    else:
        print('Comprobado: no hay enlaces rotos a imágenes ni vídeos.')


import re
_comprobar_archivos()
