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
function fotoCaballo(c, clase){
  const ruta = RUTA + 'img/caballos/' + c.slug + '/';
  const cara = (c.fotos && c.fotos.length)
    ? '<img src="' + ruta + c.fotos[0] + '" alt="' + c.nombre + ', caballo PRE de Yeguada Tres Tréboles">'
    : marcador(c.nombre);

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
      ((c.fotos && c.fotos.length)
        ? '<img src="' + RUTA + 'img/caballos/' + c.slug + '/' + c.fotos[0] + '" alt="' + c.nombre + '">'
        : marcador(c.nombre)) +
      '</div><h3>' + c.nombre + '</h3><div class="fe">' + fechaLarga(c.nacimiento) + '</div></a>')
    .join('');
}

/* Ejemplares en venta */
function pintarVenta(id){
  const caja = document.getElementById(id); if (!caja) return;
  caja.innerHTML = CABALLOS.filter(c => c.enVenta && !c.vendido)
    .sort((a,b) => new Date(b.nacimiento) - new Date(a.nacimiento))
    .map(c => '<a class="venta-card" href="' + RUTA + 'caballos/' + c.slug + '.html">' +
      '<div class="marco">' +
        ((c.fotos && c.fotos.length)
          ? '<img src="' + RUTA + 'img/caballos/' + c.slug + '/' + c.fotos[0] + '" alt="' + c.nombre + '">'
          : marcador(c.nombre)) +
      '</div><div class="cuerpo"><span class="tag-venta">Disponible</span>' +
      '<h3>' + c.nombre + '</h3>' +
      '<div class="meta">' + (c.sexo === 'M' ? 'Macho' : 'Hembra') + ' PRE · ' +
        (c.capa || 'capa pendiente') + ' · ' + anio(c.nacimiento) + '</div>' +
      '<div class="precio">Precio a consultar</div></div></a>')
    .join('');
}

/* Cuenta de ejemplares por grupo, para el menú y las tarjetas */
function contar(grupo){
  if (grupo === 'en-venta') return CABALLOS.filter(c => c.enVenta && !c.vendido).length;
  return CABALLOS.filter(c => c.grupo === grupo).length;
}

/* ---------- Rejilla de caballos con filtros ---------- */
let FILTROS = {grupo:'todos', capa:'todos', sexo:'todos'};

function pasaFiltro(c){
  if (FILTROS.grupo !== 'todos'){
    if (FILTROS.grupo === 'en-venta'){ if (!c.enVenta || c.vendido) return false; }
    else if (c.grupo !== FILTROS.grupo) return false;
  }
  if (FILTROS.capa !== 'todos' && c.capa !== FILTROS.capa) return false;
  if (FILTROS.sexo !== 'todos' && c.sexo !== FILTROS.sexo) return false;
  return true;
}

const CLASE_CAPA = {'Castaña':'c-castana','Negra':'c-negra','Torda':'c-torda','Bayo':'c-bayo'};

function tarjetaCaballo(c){
  const cl = CLASE_CAPA[c.capa] || 'c-none';
  const tags = [];
  if (c.enVenta && !c.vendido) tags.push('<span class="tag venta">En venta</span>');
  if (c.vendido) tags.push('<span class="tag">Vendido</span>');
  if (c.palmares && c.palmares.length) tags.push('<span class="tag hito">' + c.palmares[0].titulo + '</span>');
  else if (c.hito) tags.push('<span class="tag hito">' + c.hito + '</span>');

  const foto = (c.fotos && c.fotos.length)
    ? '<img src="' + RUTA + 'img/caballos/' + c.slug + '/' + c.fotos[0] + '" alt="' + c.nombre + ', caballo PRE">'
    : marcador(c.nombre);

  return '<a class="tarjeta" href="' + RUTA + 'caballos/' + c.slug + '.html">' +
    '<div class="foto">' + foto +
      (tags.length ? '<div class="etiquetas">' + tags.join('') + '</div>' : '') + '</div>' +
    '<div class="cuerpo"><h3>' + c.nombre + '</h3>' +
    '<div class="meta">' + GRUPOS[c.grupo] + ' · ' + anio(c.nacimiento) + ' · ' + edad(c.nacimiento) + '</div>' +
    '<div class="capa-linea"><span class="punto ' + cl + '"></span>' +
      (c.capa ? c.capa : 'Capa pendiente') + '</div></div></a>';
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
    fila.addEventListener('click', e => {
      const b = e.target.closest('.chip'); if (!b) return;
      FILTROS[fila.dataset.filtro] = b.dataset.valor;
      fila.querySelectorAll('.chip').forEach(x => x.setAttribute('aria-pressed', String(x === b)));
      pintarRejilla(id, base);
    });
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

  const enlaceHijos = c.cubriciones
    ? '<a class="ver-arbol" href="' + RUTA + 'hijos-de-' + c.slug + '.html">' +
      'Ver todos los hijos de ' + nombreCorto + '</a>' : '';

  const bloqueHijos = (hijos.length || enlaceHijos) ? (
    '<section class="seccion-ficha"><div class="bloque"><h2>Descendencia</h2>' +
    '<div class="hijos">' + hijos.map(h =>
      '<a class="rama" href="' + RUTA + 'caballos/' + h.slug + '.html">' +
      '<div class="r">' + fechaLarga(h.nacimiento) + '</div>' +
      '<div class="v">' + h.nombre + '</div><div class="link">Ver su ficha →</div></a>').join('') +
    '</div>' + enlaceHijos + '</div></section>') : '';

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

    '<div class="ficha-cols">' +
      '<div class="bloque"><h2>Sobre ' + nombreCorto + '</h2>' +
        (c.texto ? '<div class="texto-ficha">' + c.texto + '</div>'
                 : '<div class="vacio">El texto de presentación está pendiente de escribir.</div>') +
        '<a class="cta" href="' + RUTA + 'contacto.html">Consultar sobre ' + nombreCorto + '</a></div>' +
      '<div class="bloque"><h2>Datos</h2><ul class="datos">' +
        '<li><span>Nacimiento</span><span>' + fechaLarga(c.nacimiento) + '</span></li>' +
        '<li><span>Edad</span><span>' + edad(c.nacimiento) + '</span></li>' +
        '<li><span>Sexo</span><span>' + (c.sexo === 'M' ? 'Macho' : 'Hembra') + '</span></li>' +
        '<li><span>Capa</span><span>' + dato(c.capa) + '</span></li>' +
        (c.lugarNacimiento ? '<li><span>Lugar de nacimiento</span><span>' + c.lugarNacimiento + '</span></li>' : '') +
        (c.criador ? '<li><span>Ganadería criadora</span><span>' + c.criador + '</span></li>' : '') +
        (c.hijosLG ? '<li><span>Hijos inscritos</span><span>' + c.hijosLG +
            ' en el Libro Genealógico</span></li>' : '') +
        (c.cubriciones ? '<li><span>Cubriciones</span><span>Disponible</span></li>' : '') +
        (c.enVenta && !c.vendido ? '<li><span>Disponibilidad</span><span>En venta</span></li>' : '') +
        (c.vendido ? '<li><span>Situación</span><span>Ya no está en la yeguada</span></li>' : '') +
      '</ul></div>' +
    '</div>' +

    palmares +

    '<section class="seccion-ficha"><div class="bloque"><h2>Genealogía</h2><div class="arbol">' +
      rama('Padre', c.padre, c.padreSlug) + rama('Madre', c.madre, c.madreSlug) +
    '</div>' +
    (c.arbol ? '<button class="ver-arbol" onclick="abrirArbol(\'' + c.slug + '\')">' +
        'Ver árbol genealógico completo</button>' +
        '<p class="pie-arbol">Del Libro Genealógico del caballo de Pura Raza Española</p>' : '') +
    '</div></section>' +

    bloqueHijos +

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

  (c.fotos || []).slice(1).forEach(f => MEDIA.push({tipo:'foto', src: ruta + f, nombre: c.nombre}));
  (c.videos || []).forEach(v => MEDIA.push({
    tipo:'video',
    src: ruta + (typeof v === 'string' ? v : v.archivo),
    poster: (typeof v === 'object' && v.poster) ? ruta + v.poster : null,
    nombre: c.nombre
  }));

  if (!MEDIA.length){
    return '<div class="vacio">Todavía no hay más fotos ni vídeos de ' + c.nombre +
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


/* El vídeo del hero aparece cuando ya puede reproducirse, para que no se
   vea un salto entre la foto y la primera imagen del vídeo. */
(function heroVideo(){
  const v = document.querySelector('.hero-video');
  if (!v) return;
  const mostrar = () => v.classList.add('visible');
  if (v.readyState >= 3) mostrar();
  v.addEventListener('canplay', mostrar, {once:true});
  // si el navegador bloquea la reproducción automática, se queda la foto
  const p = v.play();
  if (p && p.catch) p.catch(() => v.classList.remove('visible'));
})();
