/* =========================================================
   Yeguada Tres Tréboles — comportamiento común
   Este archivo lo usan todas las páginas. Se encarga de:
     · la cabecera fija que cambia al bajar
     · el menú de móvil
     · pintar los bloques que salen de datos/caballos.js
   ========================================================= */

/* ---------- Cabecera ---------- */
(function cabecera(){
  const top   = document.getElementById('top');
  const marca = document.getElementById('i-marca');
  if (!top) return;

  function pintar(){
    const solido = window.scrollY > 90 || document.body.classList.contains('sin-hero');
    top.classList.toggle('solido', solido);
    if (marca) marca.src = RUTA + 'img/marca/' + (solido ? 'marca-negro.png' : 'marca-blanco.png');
  }
  window.addEventListener('scroll', pintar, {passive:true});
  pintar();

  const btn = document.getElementById('btn-menu');
  if (btn){
    btn.addEventListener('click', () => {
      const abierto = document.body.classList.toggle('menu-abierto');
      btn.setAttribute('aria-expanded', String(abierto));
    });
    document.querySelectorAll('#panel a').forEach(a =>
      a.addEventListener('click', () => document.body.classList.remove('menu-abierto')));
  }
})();

/* ---------- Utilidades de caballos ---------- */
const GRUPOS = {
  'semental':'Semental', 'yegua':'Yegua de cría',
  'nacido-aqui':'Nacido en la yeguada', 'venta':'En venta'
};

/* Cómo se describe el caballo bajo su nombre en la ficha.
   Para los nacidos aquí no vale "Nacido en la yeguada PRE": se dice qué es. */
function etiquetaGrupo(c){
  if (c.grupo === 'semental') return 'Semental PRE';
  if (c.grupo === 'yegua')    return 'Yegua de cría PRE';
  if (mesesDesde(c.nacimiento) < 48) return (c.sexo === 'M' ? 'Potro PRE' : 'Potra PRE');
  return (c.sexo === 'M' ? 'Caballo PRE' : 'Yegua PRE');
}

const porSlug = s => CABALLOS.find(c => c.slug === s);
const anio    = iso => new Date(iso).getFullYear();
const fechaLarga = iso => new Date(iso)
  .toLocaleDateString('es-ES',{day:'numeric',month:'long',year:'numeric'});

/* Edad en meses hasta que cumple el año; a partir de ahí, en años. */
function mesesDesde(iso){
  const n = new Date(iso), h = new Date();
  let m = (h.getFullYear() - n.getFullYear()) * 12 + (h.getMonth() - n.getMonth());
  if (h.getDate() < n.getDate()) m--;
  return Math.max(0, m);
}

function edad(iso){
  const m = mesesDesde(iso);
  if (m === 0)  return 'recién nacido';
  if (m === 1)  return '1 mes';
  if (m < 12)   return m + ' meses';
  const a = Math.floor(m / 12);
  return a + (a === 1 ? ' año' : ' años');
}

/* Marcador para los caballos que todavía no tienen foto */
function marcador(nombre){
  return '<div class="marcador">' +
    '<img class="mk" src="' + RUTA + 'img/marca/marca-blanco.png" alt="">' +
    '<span>' + nombre + '</span><small>Foto pendiente</small></div>';
}

/* La foto del caballo. Si tiene carta genealógica, la foto se voltea al pasar
   por encima (o al tocarla en móvil) y enseña el documento por detrás. */
/* Los marcos son apaisados (la franja de la ficha) o cuadrados (las tarjetas).
   Cuando la foto no tiene la misma forma que su hueco hay que elegir: o se
   recorta para llenarlo, o se enseña entera y se rellena el resto con la
   misma foto desenfocada.

   Se mira cuánto se perdería al recortar, EN LOS DOS SENTIDOS. Da igual que
   la foto sea vertical u horizontal: lo que importa es la diferencia de forma
   con el hueco. La portada de Nerva (1358x988) es apaisada, pero en la franja
   de la ficha se le comía un tercio por arriba y por abajo, y en la tarjeta
   cuadrada se le comía la cabeza por un lado. */
function ajustarVertical(img){
  const caja = img.closest('.foto, .marco');
  if (!caja) return;
  const r = caja.getBoundingClientRect();
  if (!r.width || !r.height || !img.naturalWidth) return;
  const foto = img.naturalWidth / img.naturalHeight;
  const hueco = r.width / r.height;
  /* Cuánto queda de la foto si se recorta: 1 = misma forma, 0.7 = se pierde
     el 30%. Hasta un 15% se recorta, que llena mejor; más allá se enseña
     entera, porque a partir de ahí el recorte se lleva la cabeza o las patas. */
  if (Math.min(foto, hueco) / Math.max(foto, hueco) < 0.85)
    caja.classList.add('vertical');
}

/* La foto de un caballo, en dos capas: la de verdad y una copia de fondo que
   solo se usa (desenfocada) cuando la foto es vertical y no llena el marco. */
function imagenCaballo(c, alt){
  if (!(c.fotos && c.fotos.length)) return marcador(c.nombre);
  const src = RUTA + 'img/caballos/' + c.slug + '/' + c.fotos[0];
  return '<img class="fondo" src="' + src + '" alt="" aria-hidden="true">' +
         '<img class="principal" src="' + src + '" loading="lazy"' +
         ' onload="ajustarVertical(this)" alt="' + (alt || c.nombre) + '">';
}

function fotoCaballo(c, clase){
  const ruta = RUTA + 'img/caballos/' + c.slug + '/';
  const cara = imagenCaballo(c, c.nombre + ', caballo PRE de Yeguada Tres Tréboles');

  if (!c.genealogia) return '<div class="foto ' + (clase||'') + '">' + cara + '</div>';

  return '<div class="foto voltea ' + (clase||'') + '" tabindex="0">' +
      '<div class="giro">' +
        '<div class="cara-a">' + cara + '</div>' +
        '<div class="cara-b">' +
          '<img src="' + ruta + c.genealogia + '" alt="Carta genealógica de ' + c.nombre + '">' +
        '</div>' +
      '</div>' +
      '<span class="pista">Ver su carta genealógica</span>' +
    '</div>';
}

/* ---------- Bloques de la portada ---------- */

/* Últimos nacimientos: siempre los cuatro más jóvenes */
function pintarNacimientos(id, n){
  const caja = document.getElementById(id); if (!caja) return;
  caja.innerHTML = CABALLOS.slice()
    .sort((a,b) => new Date(b.nacimiento) - new Date(a.nacimiento))
    .slice(0, n || 4)
    .map(c => '<a href="' + RUTA + 'caballos/' + c.slug + '.html"><div class="marco">' +
      imagenCaballo(c) +
      '</div><h3>' + c.nombre + '</h3><div class="fe">' + fechaLarga(c.nacimiento) + '</div></a>')
    .join('');
}

/* Ejemplares en venta */
function pintarVenta(id){
  const caja = document.getElementById(id); if (!caja) return;
  caja.innerHTML = CABALLOS.filter(c => c.enVenta && !c.vendido)
    .sort((a,b) => new Date(b.nacimiento) - new Date(a.nacimiento))
    .map(c => '<a class="venta-card" href="' + RUTA + 'caballos/' + c.slug + '.html">' +
      '<div class="marco">' + imagenCaballo(c) + '</div><div class="cuerpo"><span class="tag-venta">Disponible</span>' +
      '<h3>' + c.nombre + '</h3>' +
      '<div class="meta">' + (c.sexo === 'M' ? 'Macho' : 'Hembra') + ' PRE · ' +
        (c.capa || 'capa pendiente') + ' · ' + anio(c.nacimiento) + '</div>' +
      '<div class="precio">' + (c.precio ? euros(c.precio) : 'Precio a consultar') +
      '</div></div></a>')
    .join('');
}

/* Cuenta de ejemplares por grupo, para el menú y las tarjetas */
function contar(grupo){
  if (grupo === 'en-venta') return CABALLOS.filter(c => c.enVenta && !c.vendido).length;
  return CABALLOS.filter(c => c.grupo === grupo).length;
}

/* ---------- Rejilla de caballos con filtros ---------- */
let FILTROS = {grupo:'todos', capa:'todos', sexo:'todos'};

/* Las capas diluidas (bayo, palomino, perlino...) son variantes del mismo
   fenómeno: un gen de dilución sobre la capa de base. En el filtro van juntas
   bajo "Diluida"; en la ficha cada caballo sigue mostrando su capa exacta. */
const CAPAS_DILUIDAS = ['Bayo','Baya','Palomino','Palomina','Perlino','Perlina',
                        'Cremello','Isabelo','Isabela'];

function pasaFiltro(c){
  if (FILTROS.grupo !== 'todos'){
    if (FILTROS.grupo === 'en-venta'){ if (!c.enVenta || c.vendido) return false; }
    else if (c.grupo !== FILTROS.grupo) return false;
  }
  if (FILTROS.capa !== 'todos'){
    if (FILTROS.capa === 'Diluida'){ if (CAPAS_DILUIDAS.indexOf(c.capa) === -1) return false; }
    else if (c.capa !== FILTROS.capa) return false;
  }
  if (FILTROS.sexo !== 'todos' && c.sexo !== FILTROS.sexo) return false;
  return true;
}

const CLASE_CAPA = {'Castaña':'c-castana','Negra':'c-negra','Torda':'c-torda','Bayo':'c-bayo',
  'Baya':'c-bayo','Alazana':'c-alazana','Palomina':'c-palomina','Perlina':'c-perlina'};

function tarjetaCaballo(c){
  const cl = CLASE_CAPA[c.capa] || 'c-none';
  const tags = [];
  if (c.enVenta && !c.vendido) tags.push('<span class="tag venta">En venta</span>');
  if (c.vendido) tags.push('<span class="tag">Vendido</span>');
  if (c.palmares && c.palmares.length) tags.push('<span class="tag hito">' + c.palmares[0].titulo + '</span>');
  else if (c.hito) tags.push('<span class="tag hito">' + c.hito + '</span>');

  const foto = imagenCaballo(c, c.nombre + ', caballo PRE');

  return '<a class="tarjeta" href="' + RUTA + 'caballos/' + c.slug + '.html">' +
    '<div class="foto">' + foto +
      (tags.length ? '<div class="etiquetas">' + tags.join('') + '</div>' : '') + '</div>' +
    '<div class="cuerpo"><h3>' + c.nombre + '</h3>' +
    '<div class="meta">' + GRUPOS[c.grupo] + ' · ' + anio(c.nacimiento) + ' · ' + edad(c.nacimiento) + '</div>' +
    '<div class="capa-linea"><span class="punto ' + cl + '"></span>' +
      (c.capa ? c.capa : 'Capa pendiente') + '</div>' +
    /* El precio, debajo de la capa, solo en los que están a la venta. */
    (c.enVenta && !c.vendido && c.precio
      ? '<div class="precio-tarjeta">' + euros(c.precio) + '</div>' : '') +
    '</div></a>';
}

/* 1500 → "1.500 €", con el punto de los miles como se escribe en español.
   Se escribe a mano en vez de con toLocaleString porque no todos los
   navegadores traen los datos del idioma y algunos devuelven "1500". */
function euros(n){
  return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ' €';
}

/* Los botones de "Ver los hijos de..." se pintan desde los mismos datos y en
   el mismo orden que las tarjetas de arriba. Escritos a mano se desordenaban
   en cuanto cambiaba el orden de la rejilla. */
function pintarEnlacesHijos(id){
  const caja = document.getElementById(id); if (!caja) return;
  caja.innerHTML = CABALLOS.filter(c => c.cubriciones)
    .sort((a,b) => new Date(b.nacimiento) - new Date(a.nacimiento))
    .map(c => '<a class="ver-arbol" href="' + RUTA + 'hijos-de-' + c.slug + '.html">' +
      'Ver los hijos de ' + c.nombre.split(' ')[0] + '</a>')
    .join('');
}

function pintarRejilla(id, base){
  const caja = document.getElementById(id); if (!caja) return;
  const lista = CABALLOS.filter(c => (!base || base(c)) && pasaFiltro(c))
    .sort((a,b) => new Date(b.nacimiento) - new Date(a.nacimiento));
  caja.innerHTML = lista.map(tarjetaCaballo).join('');

  const cuenta = document.getElementById('recuento');
  if (cuenta){
    const n = lista.length, t = CABALLOS.filter(c => !base || base(c)).length;
    cuenta.textContent = n === 0 ? 'Ningún ejemplar con estos filtros'
      : n === t ? n + (n === 1 ? ' ejemplar' : ' ejemplares')
      : n + ' de ' + t + ' ejemplares';
  }
}

function activarFiltros(id, base){
  document.querySelectorAll('.fila-filtro').forEach(fila => {
    const clave = fila.dataset.filtro;
    const chips = fila.querySelectorAll('.chip');

    /* En el móvil los botones no caben en una línea y se descolocan: ahí se
       enseña un desplegable con las mismas opciones (lo decide el CSS). Los
       dos mandos son el mismo filtro, así que se mantienen sincronizados. */
    const sel = document.createElement('select');
    sel.className = 'sel-f';
    sel.setAttribute('aria-label', (fila.querySelector('.et-f') || {}).textContent || clave);
    chips.forEach(b => {
      const o = document.createElement('option');
      o.value = b.dataset.valor;
      o.textContent = b.textContent.trim();
      o.selected = b.getAttribute('aria-pressed') === 'true';
      sel.appendChild(o);
    });
    fila.appendChild(sel);

    const aplicar = valor => {
      FILTROS[clave] = valor;
      chips.forEach(x => x.setAttribute('aria-pressed', String(x.dataset.valor === valor)));
      if (sel.value !== valor) sel.value = valor;
      pintarRejilla(id, base);
    };

    fila.addEventListener('click', e => {
      const b = e.target.closest('.chip'); if (!b) return;
      aplicar(b.dataset.valor);
    });
    sel.addEventListener('change', () => aplicar(sel.value));
  });
  pintarRejilla(id, base);
}

/* ---------- Ficha individual ---------- */
function pintarFicha(slug){
  const c = porSlug(slug); if (!c) return;
  const caja = document.getElementById('ficha'); if (!caja) return;
  const dato = v => v ? v : '<span class="pendiente">Pendiente</span>';
  const nombreCorto = c.nombre.split(' ')[0];

  const rama = (rol, nombre, sl) => {
    if (!nombre) return '<div class="rama"><div class="r">' + rol + '</div>' +
      '<div class="v pendiente">Pendiente</div></div>';
    const cuerpo = '<div class="r">' + rol + '</div><div class="v">' + nombre + '</div>' +
      (sl ? '<div class="link">Ver su ficha →</div>' : '');
    return sl ? '<a class="rama" href="' + RUTA + 'caballos/' + sl + '.html">' + cuerpo + '</a>'
              : '<div class="rama">' + cuerpo + '</div>';
  };

  const hijos = (c.descendencia || []).map(porSlug).filter(Boolean)
    .sort((a,b) => new Date(a.nacimiento) - new Date(b.nacimiento));

  /* Si está disponible para cubrición, se dice claro y se lleva al servicio. */
  const bloqueCubricion = c.cubriciones ? (
    '<section class="seccion-ficha"><div class="bloque aviso-cubricion">' +
      '<div class="et">Cubriciones</div>' +
      '<p class="tit-cub">' + nombreCorto + ' está disponible para cubrir tu yegua</p>' +
      (c.precioCubricion
        ? '<p class="precio-suelto">' + c.precioCubricion + ' € por cubrición</p>' : '') +
      '<p>El canon se paga una sola vez, hasta que la yegua quede preñada. La extracción ' +
        'veterinaria y el envío, si hacen falta, se cobran aparte.</p>' +
      '<a class="cta" href="' + RUTA + 'cubriciones.html">Ver el servicio de cubriciones</a>' +
    '</div></section>') : '';

  const bloqueHijos = hijos.length ? (
    '<section class="seccion-ficha"><div class="bloque"><h2>Descendencia en la yeguada</h2>' +
    '<div class="hijos">' + hijos.map(h =>
      '<a class="rama" href="' + RUTA + 'caballos/' + h.slug + '.html">' +
      '<div class="r">' + fechaLarga(h.nacimiento) + '</div>' +
      '<div class="v">' + h.nombre + '</div><div class="link">Ver su ficha →</div></a>').join('') +
    '</div></div></section>') : '';

  /* Todos los hijos inscritos en el Libro Genealógico, sean nuestros o no.
     Solo nombre, año, capa y el otro progenitor: ni microchip ni carta. */
  const reg = c.hijosReg || [];
  const otroTitulo = c.sexo === 'H' ? 'Padre' : 'Madre';

  /* De quién es hoy cada cría. No hace falta saber el nombre del titular para
     dejar claro lo importante: si no está en la yeguada, no es nuestro. */
  function titularDe(h){
    const nuestro = h.slug ? porSlug(h.slug) : null;
    if (nuestro && !nuestro.vendido)
      return '<span class="es-nuestro">Tres Tréboles</span>';
    if (h.titular) return h.titular;
    return '<span class="es-ajeno">Otra ganadería</span>';
  }

  const enCasa = reg.filter(h => { const n = h.slug ? porSlug(h.slug) : null;
                                   return n && !n.vendido; }).length;
  const bloqueReg = reg.length ? (
    '<section class="seccion-ficha"><div class="bloque">' +
    '<h2>Descendencia inscrita</h2>' +
    '<p class="pie-lg">' + reg.length + ' hijos inscritos.</p>' +
    '<div class="tabla-hijos con-titular">' +
      '<div class="fila cab"><span>Año</span><span>Nombre</span><span>Capa</span><span>' +
        otroTitulo + '</span><span>Titular</span></div>' +
      reg.map(h => '<div class="fila">' +
        '<span class="anio">' + h.anio + '</span>' +
        '<span class="nom">' + (h.slug
          ? '<a href="' + RUTA + 'caballos/' + h.slug + '.html">' + h.nombre + '</a>'
          : h.nombre) + '</span>' +
        '<span class="cap"><span class="punto ' + (CLASE_CAPA[h.capa] || 'c-none') + '"></span>' +
          h.capa + '</span>' +
        '<span class="otro">' + h.otro + '</span>' +
        '<span class="tit">' + titularDe(h) + '</span></div>').join('') +
    '</div></div></section>') : '';

  let palmares = '';
  if (c.palmares && c.palmares.length){
    const anios = [...new Set(c.palmares.map(p => p.anio))].sort((a,b) => b - a);
    palmares = '<section class="seccion-ficha"><div class="bloque"><h2>Palmarés</h2>' +
      anios.map(a =>
        '<div class="palmares-anio"><div class="anio">' + a + '</div>' +
        c.palmares.filter(p => p.anio === a)
          .sort((x,y) => x.puesto - y.puesto)
          .map(p =>
            '<div class="resultado' + (p.puesto <= 3 ? ' destaca' : '') + '">' +
              '<span class="puesto">' + p.puesto + 'º</span>' +
              '<span class="conc"><strong>' + p.concurso + '</strong>' +
                (p.titulo ? '<em>' + p.titulo + '</em>' : '') +
                (p.nota ? '<small>' + p.nota + '</small>' : '') + '</span>' +
              '<span class="punt">' + (p.puntos || '') + '</span>' +
            '</div>').join('') +
        '</div>').join('') +
      '</div></section>';
  }

  const galeria = construirGaleria(c);

  caja.innerHTML =
    '<a class="volver" href="' + RUTA + 'caballos.html">← Volver a nuestros caballos</a>' +
    '<div class="ficha-hero">' + fotoCaballo(c) + '</div>' +
    (c.creditoPortada ? '<div class="credito-pie">Foto: ' + c.creditoPortada + '</div>' : '') +
    '<div class="ficha-cab"><h1>' + c.nombre + '</h1><div class="sub">' +
      [etiquetaGrupo(c), c.capa || 'capa pendiente',
       anio(c.nacimiento) + ' · ' + edad(c.nacimiento)].join(' · ') + '</div>' +
      (c.nota ? '<p class="nota-ficha">' + c.nota + '</p>' : '') + '</div>' +

    /* El bloque "Sobre X" solo aparece si hay algo que contar de ese caballo.
       Si no, los datos ocupan todo el ancho y no queda un hueco vacío. */
    '<div class="ficha-cols' + (c.texto ? '' : ' sola') + '">' +
      (c.texto
        ? '<div class="bloque"><h2>Sobre ' + nombreCorto + '</h2>' +
          '<div class="texto-ficha">' + c.texto + '</div>' +
          '<a class="cta" href="' + RUTA + 'contacto.html">Consultar sobre ' +
            nombreCorto + '</a></div>'
        : '') +
      '<div class="bloque"><h2>Datos</h2><ul class="datos">' +
        '<li><span>Nacimiento</span><span>' + fechaLarga(c.nacimiento) + '</span></li>' +
        '<li><span>Edad</span><span>' + edad(c.nacimiento) + '</span></li>' +
        '<li><span>Sexo</span><span>' + (c.sexo === 'M' ? 'Macho' : 'Hembra') + '</span></li>' +
        '<li><span>Capa</span><span>' + dato(c.capa) + '</span></li>' +
        (c.lugarNacimiento ? '<li><span>Lugar de nacimiento</span><span>' + c.lugarNacimiento + '</span></li>' : '') +
        (c.criador ? '<li><span>Ganadería criadora</span><span>' + c.criador + '</span></li>' : '') +
        (c.hijosLG ? '<li><span>Hijos inscritos</span><span>' + c.hijosLG +
            ' en el Libro Genealógico</span></li>' : '') +
        (c.cubriciones ? '<li><span>Cubriciones</span><span><a href="' + RUTA +
            'cubriciones.html">Disponible</a></span></li>' : '') +
        (c.enVenta && !c.vendido ? '<li><span>Disponibilidad</span><span>En venta</span></li>' : '') +
        (c.enVenta && !c.vendido && c.precio
          ? '<li><span>Precio</span><span>' + euros(c.precio) + '</span></li>' : '') +
        (c.vendido ? '<li><span>Situación</span><span>Ya no está en la yeguada</span></li>' : '') +
      '</ul>' +
      (c.texto ? '' : '<a class="cta" href="' + RUTA + 'contacto.html">Consultar sobre ' +
        nombreCorto + '</a>') + '</div>' +
    '</div>' +

    palmares +

    '<section class="seccion-ficha"><div class="bloque"><h2>Genealogía</h2><div class="arbol">' +
      rama('Padre', c.padre, c.padreSlug) + rama('Madre', c.madre, c.madreSlug) +
    '</div>' +
    (c.arbol ? '<button class="ver-arbol" onclick="abrirArbol(\'' + c.slug + '\')">' +
        'Ver árbol genealógico completo</button>' +
        '' : '') +
    '</div></section>' +

    bloqueCubricion +
    bloqueHijos +
    bloqueReg +

    '<section class="seccion-ficha"><div class="bloque"><h2>Galería</h2>' + galeria +
      (c.credito ? '<div class="credito-pie" style="text-align:left;margin-top:14px">' +
        'Algunas fotos: ' + c.credito + '</div>' : '') + '</div></section>';
}


/* ---------- Visor del árbol genealógico ---------- */
function abrirArbol(slug){
  const c = porSlug(slug); if (!c || !c.arbol) return;
  const visor = document.createElement('div');
  visor.className = 'visor';
  visor.innerHTML =
    '<button class="cerrar" aria-label="Cerrar">✕</button>' +
    '<div class="visor-cab"><strong>' + c.nombre + '</strong>' +
      '<span>Árbol genealógico · Libro Genealógico del PRE</span></div>' +
    '<div class="visor-img"><img src="' + RUTA + 'img/caballos/' + c.slug + '/' + c.arbol +
      '" alt="Árbol genealógico de ' + c.nombre + '"></div>';
  document.body.appendChild(visor);
  document.body.style.overflow = 'hidden';
  requestAnimationFrame(() => visor.classList.add('abierto'));

  const cerrar = () => { visor.remove(); document.body.style.overflow = ''; };
  visor.querySelector('.cerrar').onclick = cerrar;
  visor.onclick = e => { if (e.target === visor) cerrar(); };
  document.addEventListener('keydown', function esc(e){
    if (e.key === 'Escape'){ cerrar(); document.removeEventListener('keydown', esc); }
  });

  // pinchar sobre la imagen amplía y permite arrastrar
  const img = visor.querySelector('img');
  img.onclick = () => visor.classList.toggle('ampliado');
}

/* ---------- Hijos de un semental ---------- */
/* Junta los que han nacido en la yeguada (de datos/caballos.js) con los
   nacidos fuera (de datos/descendencia.js) y los pinta ordenados por fecha. */
function pintarHijos(slugPadre, id){
  const caja = document.getElementById(id); if (!caja) return;

  const enCasa = CABALLOS.filter(c => c.padreSlug === slugPadre)
    .map(c => ({
      nombre: c.nombre, nacimiento: c.nacimiento, sexo: c.sexo, capa: c.capa,
      madre: c.madre, ganaderia: 'Yeguada Tres Tréboles', enCasa: true,
      slug: c.slug, foto: (c.fotos && c.fotos.length) ? c.fotos[0] : null
    }));

  const fuera = (typeof DESCENDENCIA_EXTERNA === 'undefined' ? [] : DESCENDENCIA_EXTERNA)
    .filter(h => h.padre === slugPadre)
    .map(h => Object.assign({}, h, {enCasa: false, slug: null}));

  const todos = enCasa.concat(fuera)
    .sort((a, b) => new Date(b.nacimiento) - new Date(a.nacimiento));

  const padre = porSlug(slugPadre);
  const cuenta = document.getElementById('recuento');
  if (cuenta){
    const lg = padre && padre.hijosLG
      ? padre.hijosLG + ' hijos inscritos en el Libro Genealógico · ' : '';
    const nacidos = enCasa.length + fuera.filter(h => h.nacidoAqui).length;
    const otras   = fuera.filter(h => !h.nacidoAqui).length;
    cuenta.textContent = todos.length === 0
      ? lg + 'todavía no hay ninguno con ficha en la web'
      : lg + todos.length + ' en esta página · ' + nacidos + ' nacidos en la yeguada' +
        (otras ? ' · ' + otras + ' en otras ganaderías' : '');
  }

  if (!todos.length){
    caja.innerHTML = '<div class="vacio">Todavía no hay hijos registrados en la web. ' +
      'Los que vayan naciendo aparecerán aquí.</div>';
    return;
  }

  caja.innerHTML = todos.map(h => {
    const cl = CLASE_CAPA[h.capa] || 'c-none';
    const img = h.enCasa
      ? (h.foto ? '<img src="' + RUTA + 'img/caballos/' + h.slug + '/' + h.foto + '" alt="' + h.nombre + '">'
                : marcador(h.nombre))
      : (h.foto ? '<img src="' + RUTA + 'img/descendencia/' + h.foto + '" alt="' + h.nombre + '">'
                : marcador(h.nombre));

    const cuerpo =
      '<div class="foto">' + img +
        '<div class="etiquetas">' +
          (h.enCasa || h.nacidoAqui ? '<span class="tag">Nacido aquí</span>' : '') +
          (!h.enCasa && h.ganaderia ? '<span class="tag fuera">' + h.ganaderia + '</span>' : '') +
          (!h.enCasa && !h.ganaderia ? '<span class="tag fuera">Otra ganadería</span>' : '') +
        '</div>' +
      '</div>' +
      '<div class="cuerpo"><h3>' + h.nombre + '</h3>' +
      '<div class="meta">' + (h.sexo === 'M' ? 'Macho' : 'Hembra') + ' · ' +
        anio(h.nacimiento) + ' · ' + edad(h.nacimiento) + '</div>' +
      (h.madre ? '<div class="meta">Madre: ' + h.madre + '</div>' : '') +
      (h.nota ? '<div class="meta nota">' + h.nota + '</div>' : '') +
      '<div class="capa-linea"><span class="punto ' + cl + '"></span>' +
        (h.capa || 'Capa pendiente') + '</div></div>';

    return h.slug
      ? '<a class="tarjeta" href="' + RUTA + 'caballos/' + h.slug + '.html">' + cuerpo + '</a>'
      : '<div class="tarjeta sin-enlace">' + cuerpo + '</div>';
  }).join('');
}


/* ---------- Galería de fotos y vídeos ---------- */
/* MEDIA guarda, para cada ficha, la lista de piezas en el orden en que se ven,
   para que el visor pueda pasar de una a otra. */
let MEDIA = [];

function construirGaleria(c){
  const ruta = RUTA + 'img/caballos/' + c.slug + '/';
  MEDIA = [];

  /* Van TODAS las fotos de la carpeta, la portada incluida. Arriba se ve
     recortada en franja: aquí se puede abrir entera. Así lo que hay en
     img/caballos/<slug>/ es exactamente lo que se ve en la galería. */
  (c.fotos || []).forEach(f => MEDIA.push({tipo:'foto', src: ruta + f, nombre: c.nombre}));
  (c.videos || []).forEach(v => MEDIA.push({
    tipo:'video',
    src: ruta + (typeof v === 'string' ? v : v.archivo),
    poster: (typeof v === 'object' && v.poster) ? ruta + v.poster : null,
    nombre: c.nombre
  }));

  if (!MEDIA.length){
    return '<div class="vacio">Todavía no hay fotos ni vídeos de ' + c.nombre +
      '. En cuanto se dejen en <code>img/caballos/' + c.slug + '/</code> aparecerán aquí solos.</div>';
  }

  return '<div class="galeria">' + MEDIA.map((m, i) => {
    if (m.tipo === 'foto'){
      return '<button class="pieza" onclick="abrirMedia(' + i + ')" aria-label="Ampliar foto">' +
        '<img src="' + m.src + '" alt="' + m.nombre + '" loading="lazy"></button>';
    }
    const fondo = m.poster
      ? '<img src="' + m.poster + '" alt="' + m.nombre + '" loading="lazy">'
      : '<video src="' + m.src + '#t=0.5" preload="metadata" muted playsinline></video>';
    return '<button class="pieza video" onclick="abrirMedia(' + i + ')" aria-label="Ver vídeo">' +
      fondo + '<span class="play"><svg viewBox="0 0 24 24" fill="currentColor">' +
      '<path d="M8 5.5v13l11-6.5z"/></svg></span></button>';
  }).join('') + '</div>';
}

/* Carrusel para las páginas de servicios (rutas, pupilaje…).
   Se le pasa el id del contenedor y una lista de piezas:
     {tipo:'foto'|'video', archivo:'ruta/al/archivo', poster:'…', pie:'texto'}
   Las rutas son relativas a la raíz del sitio.

   Piezas cuadradas que se deslizan de una en una. Se maneja con las flechas,
   arrastrando el dedo en el móvil o con el teclado. Al pulsar una se abre
   grande en el visor. */
function pintarCarrusel(id, piezas){
  const caja = document.getElementById(id);
  if (!caja) return;

  MEDIA = piezas.map(p => ({
    tipo: p.tipo || 'foto',
    src: RUTA + p.archivo,
    poster: p.poster ? RUTA + p.poster : null,
    nombre: p.pie || ''
  }));

  const tarjetas = MEDIA.map((m, i) => {
    const pie = m.nombre ? '<span class="pie-pieza">' + m.nombre + '</span>' : '';
    if (m.tipo === 'foto'){
      return '<button class="pieza" onclick="abrirMedia(' + i + ')" aria-label="Ampliar foto">' +
        '<img src="' + m.src + '" alt="' + m.nombre + '" loading="lazy">' + pie + '</button>';
    }
    const fondo = m.poster
      ? '<img src="' + m.poster + '" alt="' + m.nombre + '" loading="lazy">'
      : '<video src="' + m.src + '#t=0.5" preload="metadata" muted playsinline></video>';
    return '<button class="pieza video" onclick="abrirMedia(' + i + ')" aria-label="Ver vídeo">' +
      fondo + '<span class="play"><svg viewBox="0 0 24 24" fill="currentColor">' +
      '<path d="M8 5.5v13l11-6.5z"/></svg></span>' + pie + '</button>';
  }).join('');

  caja.className = 'carrusel';
  caja.innerHTML =
    '<div class="pista" tabindex="0">' + tarjetas + '</div>' +
    '<button class="flecha ant" aria-label="Anterior">‹</button>' +
    '<button class="flecha sig" aria-label="Siguiente">›</button>';

  const pista = caja.querySelector('.pista');
  const ant   = caja.querySelector('.flecha.ant');
  const sig   = caja.querySelector('.flecha.sig');

  const paso = () => {
    const p = pista.querySelector('.pieza');
    return p ? p.getBoundingClientRect().width + 16 : 300;   // 16 = hueco entre piezas
  };
  const mover = d => pista.scrollBy({left: d * paso(), behavior: 'smooth'});

  ant.onclick = () => mover(-1);
  sig.onclick = () => mover(1);
  pista.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight'){ e.preventDefault(); mover(1); }
    if (e.key === 'ArrowLeft'){  e.preventDefault(); mover(-1); }
  });

  /* Las flechas se apagan al llegar a los extremos */
  function estado(){
    const fin = pista.scrollWidth - pista.clientWidth - 2;
    ant.classList.toggle('apagada', pista.scrollLeft <= 2);
    sig.classList.toggle('apagada', pista.scrollLeft >= fin);
    caja.classList.toggle('sin-flechas', pista.scrollWidth <= pista.clientWidth + 2);
  }
  pista.addEventListener('scroll', estado, {passive:true});
  window.addEventListener('resize', estado);
  estado();
}

/* Nombre anterior, por si alguna página todavía lo usa */
const pintarGaleria = pintarCarrusel;

function abrirMedia(i){
  let idx = i;
  const visor = document.createElement('div');
  visor.className = 'visor visor-media';
  visor.innerHTML =
    '<button class="cerrar" aria-label="Cerrar">✕</button>' +
    (MEDIA.length > 1 ? '<button class="nav ant" aria-label="Anterior">‹</button>' +
                        '<button class="nav sig" aria-label="Siguiente">›</button>' : '') +
    '<div class="visor-img"></div>' +
    '<div class="visor-pie"></div>';
  document.body.appendChild(visor);
  document.body.style.overflow = 'hidden';
  requestAnimationFrame(() => visor.classList.add('abierto'));

  const caja = visor.querySelector('.visor-img');
  const pie  = visor.querySelector('.visor-pie');

  function pintar(){
    const m = MEDIA[idx];
    caja.innerHTML = m.tipo === 'foto'
      ? '<img src="' + m.src + '" alt="' + m.nombre + '">'
      : '<video src="' + m.src + '" controls autoplay playsinline muted loop' +
        (m.poster ? ' poster="' + m.poster + '"' : '') + '></video>';
    pie.textContent = m.nombre + (MEDIA.length > 1 ? '  ·  ' + (idx + 1) + ' de ' + MEDIA.length : '');
  }
  const mover = d => { idx = (idx + d + MEDIA.length) % MEDIA.length; pintar(); };
  pintar();

  const cerrar = () => { visor.remove(); document.body.style.overflow = ''; document.removeEventListener('keydown', teclas); };
  function teclas(e){
    if (e.key === 'Escape') cerrar();
    if (e.key === 'ArrowRight') mover(1);
    if (e.key === 'ArrowLeft')  mover(-1);
  }
  document.addEventListener('keydown', teclas);
  visor.querySelector('.cerrar').onclick = cerrar;
  visor.onclick = e => { if (e.target === visor || e.target === caja) cerrar(); };
  const ant = visor.querySelector('.ant'), sig = visor.querySelector('.sig');
  if (ant) ant.onclick = e => { e.stopPropagation(); mover(-1); };
  if (sig) sig.onclick = e => { e.stopPropagation(); mover(1); };
}


/* Las tarjetas de la portada dicen cuántos hay, leyéndolo de los datos */
document.querySelectorAll('[data-cuenta]').forEach(el => {
  const n = contar(el.dataset.cuenta);
  el.textContent = n + (n === 1 ? ' ejemplar' : ' ejemplares');
});


/* Los vídeos de fondo (la sierra en la portada, las yeguas en su cabecera)
   solo se enseñan cuando están reproduciéndose de verdad.

   En el móvil la reproducción automática se bloquea a menudo: con el modo de
   ahorro de energía del iPhone, con el ahorro de datos o si el sistema pide
   menos animación. Cuando eso pasa, Safari dibuja un botón de play enorme en
   medio del vídeo. Dejándolo invisible hasta que suena el evento 'playing',
   lo que se ve es la foto de debajo y no ese botón. */
(function videosDeFondo(){
  document.querySelectorAll('.hero-video, .video-fondo').forEach(v => {
    v.muted = true;                 // hace falta para poder arrancar solo
    v.setAttribute('muted', '');
    v.playsInline = true;
    const mostrar  = () => v.classList.add('visible');
    const esconder = () => v.classList.remove('visible');
    /* Ojo: con el atributo autoplay el vídeo puede haber arrancado ya antes
       de que este script llegue a ejecutarse, y entonces el aviso 'playing'
       ya ha pasado. Por eso además de escucharlo se mira si está en marcha. */
    const revisar = () => { if (!v.paused && v.readyState >= 2) mostrar(); };
    v.addEventListener('playing', mostrar);
    v.addEventListener('timeupdate', revisar, {passive:true});
    revisar();
    const p = v.play();
    if (p && p.then) p.then(mostrar, esconder);
  });
})();
