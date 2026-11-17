#!/usr/bin/env python3
"""Genera las páginas de contenido de /oposiciones-tecnologia/ (examen 2025, supuestos, programación).

Uso: python3 _tools/generar_paginas.py   (desde la raíz del repositorio)
Cada página se escribe en <slug>/index.html y se añade al sitemap.xml.
"""
import html
import json
import os
import re

BASE = "https://informeperitoinformatico.es/oposiciones-tecnologia"
FECHA = "2026-11-17"
WA = "34649716627"
AUTOR = {"@type": "Person", "@id": BASE + "/#enrique", "name": "Enrique Delgado Huerta",
         "jobTitle": "Profesor de Enseñanza Secundaria, especialidad Tecnología", "url": BASE + "/"}
IMG = BASE + "/enrique-delgado-preparador-oposiciones-tecnologia.jpg"
EXAMEN_PDF = "https://www.comunidad.madrid/docs/assets/2025/06/24/rh03_257_2025_exa_590019.pdf"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

esc = html.escape


# ───────────────────────── contenido ─────────────────────────
PAGINAS = []

PAGINAS.append({
    "slug": "examen-practico-2025",
    "title": "Examen práctico Tecnología Madrid 2025 resuelto | Oposiciones",
    "desc": ("Prueba práctica de Tecnología (0590) de la Comunidad de Madrid 2025: las 8 cuestiones, "
             "puntuación y resolución paso a paso de las que se pueden resolver con el enunciado."),
    "h1": "Examen práctico de Tecnología de Madrid 2025, <em>resuelto y comentado</em>",
    "eyebrow": "Oposiciones 2025 · Cuerpo 0590 · Especialidad 019",
    "resumen": ("La prueba práctica de Tecnología de la Comunidad de Madrid de 2025 tuvo 8 cuestiones sobre 10 puntos: "
                "dibujo técnico, neumática e hidráulica, materiales y estructuras (1,5 puntos cada una) y máquinas térmicas, "
                "electrónica digital, corriente alterna y sistemas de control (1 punto cada una). Se permitía calculadora no "
                "programable y material de dibujo, y había que justificar todos los cálculos."),
    "cuerpo": f"""
<p>Este es el examen real de la <strong>primera prueba, parte A (práctica)</strong>, de las oposiciones de 2025 al Cuerpo de Profesores de Enseñanza Secundaria, especialidad Tecnología, en la Comunidad de Madrid. El enunciado oficial está publicado por la Consejería: <a href="{EXAMEN_PDF}" target="_blank" rel="noopener">descargar el PDF del examen</a>.</p>
<p>Resuelvo paso a paso las cuestiones cuyos datos están completos en el texto del enunciado. Las que dependen de una figura (la vista de dibujo, la viga, el cronograma del biestable y los diagramas de bloques) las explico con el método que pide el tribunal, porque sin la figura cualquier número sería inventado.</p>

<h2>Condiciones de la prueba</h2>
<ul>
<li><strong>8 cuestiones</strong>, puntuación especificada en cada una, calificación máxima de <strong>10 puntos</strong>.</li>
<li><strong>Material permitido:</strong> calculadora no programable, bolígrafo azul o negro y material de dibujo.</li>
<li>Todas las respuestas y cálculos deben estar <strong>debidamente justificados</strong>: un resultado sin desarrollo no puntúa completo.</li>
<li>La parte A pesa el <strong>70 %</strong> de la primera prueba y exige al menos un 2,5 para que cuente.</li>
</ul>

<table class="tabla">
<thead><tr><th>Cuestión</th><th>Bloque</th><th>Puntos</th></tr></thead>
<tbody>
<tr><td>1</td><td>Dibujo técnico</td><td>1,5</td></tr>
<tr><td>2</td><td>Neumática e hidráulica</td><td>1,5</td></tr>
<tr><td>3</td><td>Materiales</td><td>1,5</td></tr>
<tr><td>4</td><td>Estructuras</td><td>1,5</td></tr>
<tr><td>5</td><td>Máquinas térmicas</td><td>1</td></tr>
<tr><td>6</td><td>Electrónica digital</td><td>1</td></tr>
<tr><td>7</td><td>Corriente alterna</td><td>1</td></tr>
<tr><td>8</td><td>Sistemas de control</td><td>1</td></tr>
</tbody>
</table>

<h2 id="c1">Cuestión 1. Dibujo técnico (1,5 p)</h2>
<p class="enunciado">Dada una escala gráfica de 0–25–50 cm: a) calcular la escala numérica; b) dibujar a esa escala una vista de 45 × 30 cm con un corte de 15 × 10 cm en la esquina superior derecha y un círculo de radio 5 cm centrado a (10, 10) cm de la esquina inferior izquierda; c) acotar la vista.</p>
<p><strong>Método.</strong> La escala numérica es la relación entre la medida en el papel y la medida real, con las dos en la misma unidad: <span class="f">E = medida dibujada / medida real</span>. Se mide con la regla cuántos milímetros ocupan en el papel los 25 cm del primer tramo de la escala gráfica y se divide. Por ejemplo, si 25 cm reales ocupan 50 mm en el papel, E = 50 / 250 = 1/5 (escala 1:5).</p>
<p>Con la escala calculada se pasan todas las medidas al papel (a 1:5, la vista de 45 × 30 cm se dibuja de 90 × 60 mm, el corte de 30 × 20 mm y el círculo de 10 mm de radio con centro a 20 mm de cada borde). En la acotación se ponen siempre las <strong>medidas reales</strong>, no las del dibujo: es el error más frecuente y el tribunal lo penaliza.</p>

<h2 id="c2">Cuestión 2. Neumática e hidráulica (1,5 p)</h2>
<p class="enunciado">Dos manómetros en tuberías de 10 mm y 2 mm de diámetro marcan 3·10<sup>6</sup> Pa y 5·10<sup>5</sup> Pa. El aceite tiene una densidad de 0,9 kg/L. Calcular el caudal suponiendo conducción horizontal.</p>
<p><strong>Planteamiento.</strong> Conducción horizontal (z<sub>1</sub> = z<sub>2</sub>), así que se aplica Bernoulli sin término de altura y la ecuación de continuidad:</p>
<p class="f">p<sub>1</sub> + ½ ρ v<sub>1</sub>² = p<sub>2</sub> + ½ ρ v<sub>2</sub>²  ·  A<sub>1</sub> v<sub>1</sub> = A<sub>2</sub> v<sub>2</sub></p>
<p>De continuidad: v<sub>2</sub> = v<sub>1</sub> (d<sub>1</sub>/d<sub>2</sub>)² = v<sub>1</sub> (10/2)² = 25 v<sub>1</sub>.</p>
<p>Con ρ = 0,9 kg/L = 900 kg/m³ y Δp = 3·10<sup>6</sup> − 5·10<sup>5</sup> = 2,5·10<sup>6</sup> Pa:</p>
<p class="f">2,5·10<sup>6</sup> = ½ · 900 · v<sub>1</sub>² (25² − 1) = 280 800 v<sub>1</sub>²  →  v<sub>1</sub> ≈ 2,98 m/s ; v<sub>2</sub> ≈ 74,6 m/s</p>
<p class="f">Q = A<sub>1</sub> v<sub>1</sub> = π (0,005)² · 2,98 ≈ 2,34·10<sup>−4</sup> m³/s ≈ <strong>0,234 L/s ≈ 14,1 L/min</strong></p>
<p><strong>Claves de corrección:</strong> pasar la densidad a kg/m³, justificar por qué desaparece el término de altura y comprobar que la tubería estrecha es la de menor presión, como exige Bernoulli.</p>

<h2 id="c3">Cuestión 3. Materiales (1,5 p)</h2>
<p class="enunciado">a) Dibujar a mano alzada la curva del ensayo de tracción de un acero hipoeutectoide con 0,5 % de carbono, con sus puntos y ecuaciones más relevantes. b) Definir alotropía y citar un elemento alotrópico.</p>
<p><strong>a)</strong> En la gráfica tensión–deformación (σ–ε) deben aparecer:</p>
<ul>
<li><strong>Zona elástica</strong>, recta, donde se cumple la ley de Hooke: <span class="f">σ = E · ε</span>, con σ = F/S<sub>0</sub> y ε = ΔL/L<sub>0</sub>. Termina en el <strong>límite de proporcionalidad</strong> y, muy cerca, el <strong>límite elástico</strong>.</li>
<li><strong>Zona de fluencia</strong>: en los aceros de bajo y medio carbono aparece un escalón en el que el material se deforma sin aumentar la carga (límite superior e inferior de fluencia).</li>
<li><strong>Zona plástica con endurecimiento</strong> hasta la <strong>tensión de rotura o resistencia a la tracción</strong>, <span class="f">σ<sub>R</sub> = F<sub>máx</sub>/S<sub>0</sub></span>, el máximo de la curva.</li>
<li><strong>Estricción</strong>: la sección se reduce localmente, la curva de tensión nominal desciende y llega la <strong>rotura</strong>. Alargamiento a rotura: <span class="f">A % = (L<sub>u</sub> − L<sub>0</sub>)/L<sub>0</sub> · 100</span>.</li>
</ul>
<p>Con 0,5 % C (por debajo del 0,77 % eutectoide) la estructura es ferrita y perlita: más resistente y menos dúctil que un acero dulce, con fluencia menos marcada.</p>
<p><strong>b)</strong> <strong>Alotropía</strong> es la propiedad de un elemento químico de presentarse en estructuras cristalinas distintas según la temperatura o la presión. Ejemplos: el <strong>hierro</strong> (Fe α cúbico centrado en el cuerpo, Fe γ cúbico centrado en las caras y Fe δ) o el <strong>carbono</strong> (diamante y grafito).</p>

<h2 id="c4">Cuestión 4. Estructuras (1,5 p)</h2>
<p class="enunciado">Para una viga empotrada de 6 m de longitud: a) calcular las reacciones en el empotramiento; b) representar los diagramas de esfuerzo cortante y momento flector.</p>
<p><strong>Método</strong> (las cargas concretas están en la figura del examen):</p>
<ol>
<li>En el empotramiento hay <strong>tres reacciones</strong>: vertical R<sub>A</sub>, horizontal H<sub>A</sub> (nula si no hay cargas horizontales) y el <strong>momento de empotramiento</strong> M<sub>A</sub>.</li>
<li>Se plantean las ecuaciones de equilibrio: ΣF<sub>y</sub> = 0 da R<sub>A</sub> como suma de las cargas (una carga repartida q en una longitud L equivale a q·L aplicada en su centro); ΣM<sub>A</sub> = 0 da M<sub>A</sub> como suma de cada carga por su distancia al empotramiento.</li>
<li>Diagrama de <strong>cortantes</strong>: se recorre la viga desde el extremo libre; es constante entre cargas puntuales y lineal bajo cargas repartidas.</li>
<li>Diagrama de <strong>momentos flectores</strong>: nulo en el extremo libre y máximo en el empotramiento (igual a M<sub>A</sub>); lineal donde el cortante es constante y parabólico bajo carga repartida. Se cumple dM/dx = V.</li>
</ol>
<p>El tribunal puntúa el convenio de signos explícito, las secciones de cálculo bien elegidas y que el valor del diagrama en el empotramiento coincida con la reacción calculada.</p>

<h2 id="c5">Cuestión 5. Máquinas térmicas (1 p)</h2>
<p class="enunciado">Motor de 4 cilindros, potencia efectiva de 30 CV a 6200 rpm, diámetro del pistón de 80,5 mm y carrera de 97,6 mm. Calcular a) la cilindrada total y b) el par motor.</p>
<p><strong>a)</strong> Cilindrada unitaria y total:</p>
<p class="f">V<sub>u</sub> = (π D²/4) · L = (π · 8,05²/4) · 9,76 ≈ 496,7 cm³  →  V<sub>T</sub> = 4 · V<sub>u</sub> ≈ <strong>1987 cm³</strong></p>
<p><strong>b)</strong> Potencia en vatios y velocidad angular:</p>
<p class="f">P = 30 CV · 735,5 W/CV ≈ 22 065 W  ·  ω = 6200 · 2π/60 ≈ 649,3 rad/s</p>
<p class="f">M = P / ω ≈ 22 065 / 649,3 ≈ <strong>34 N·m</strong></p>
<p>Error típico: usar las rpm sin pasarlas a rad/s, o mezclar milímetros y centímetros en la cilindrada.</p>

<h2 id="c6">Cuestión 6. Electrónica digital (1 p)</h2>
<p class="enunciado">Dibujar la señal de salida de un biestable a partir del cronograma de sus entradas, con Q = 0 inicialmente.</p>
<p><strong>Método.</strong> Lo primero es identificar el tipo de biestable de la figura y si es <strong>asíncrono</strong> o <strong>síncrono</strong> (y, en ese caso, si dispara por flanco de subida o de bajada). Después se recorre el cronograma instante a instante aplicando su tabla de verdad:</p>
<ul>
<li><strong>RS</strong>: S = 1 pone Q a 1, R = 1 la pone a 0, ambas a 0 mantiene el estado; S = R = 1 es la combinación prohibida (o la que defina el fabricante).</li>
<li><strong>JK</strong>: como el RS, pero con J = K = 1 la salida bascula (Q pasa a Q̅) en cada flanco activo.</li>
<li><strong>D</strong>: en cada flanco activo, Q toma el valor de D.</li>
<li><strong>T</strong>: con T = 1 la salida bascula en cada flanco; con T = 0 se mantiene.</li>
</ul>
<p>Hay que marcar en el dibujo los flancos activos del reloj: es lo que el tribunal mira para ver si se ha entendido el sincronismo.</p>

<h2 id="c7">Cuestión 7. Corriente alterna (1 p)</h2>
<p class="enunciado">Motor monofásico de 5 kW con cos φ = 0,7 conectado a 220 V / 50 Hz. Un condensador en paralelo reduce la corriente de línea un 26 %. Calcular a) la corriente de línea I′ y b) el nuevo factor de potencia y la expresión temporal i′(t).</p>
<p><strong>Corriente inicial:</strong></p>
<p class="f">I = P / (V cos φ) = 5000 / (220 · 0,7) ≈ 32,47 A</p>
<p><strong>a)</strong> Se reduce un 26 %:</p>
<p class="f">I′ = 0,74 · I ≈ <strong>24,03 A</strong></p>
<p><strong>b)</strong> El condensador no consume potencia activa, así que P se mantiene:</p>
<p class="f">cos φ′ = P / (V I′) = 0,7 / 0,74 ≈ <strong>0,946</strong>  →  φ′ ≈ 18,9° ≈ 0,330 rad</p>
<p>Tomando la tensión como referencia, v(t) = 220√2 sen(100πt), y suponiendo compensación parcial (la carga sigue siendo inductiva, corriente en retraso):</p>
<p class="f">i′(t) = 24,03 · √2 · sen(100πt − 0,330) ≈ <strong>34,0 · sen(100πt − 0,330) A</strong></p>
<p>Comprobación útil para el tribunal: la potencia reactiva que aporta el condensador es Q<sub>C</sub> = P (tg φ − tg φ′) ≈ 3,39 kvar, lo que corresponde a C = Q<sub>C</sub> / (V² ω) ≈ 223 µF.</p>

<h2 id="c8">Cuestión 8. Sistemas de control (1 p)</h2>
<p class="enunciado">Determinar H<sub>1</sub>, H<sub>2</sub> y H<sub>3</sub> en función de G<sub>1</sub> y G<sub>2</sub> para que dos sistemas de control sean equivalentes.</p>
<p><strong>Método.</strong> Se obtiene la función de transferencia global de cada diagrama con el álgebra de bloques y se igualan:</p>
<ul>
<li>Bloques en <strong>serie</strong>: se multiplican, G = G<sub>1</sub> · G<sub>2</sub>.</li>
<li>Bloques en <strong>paralelo</strong>: se suman (o restan, según el signo del sumador), G = G<sub>1</sub> ± G<sub>2</sub>.</li>
<li><strong>Realimentación negativa</strong>: G / (1 + G H); positiva: G / (1 − G H).</li>
<li>Al <strong>mover un punto de bifurcación o un sumador</strong> a través de un bloque, hay que compensar con ese bloque o con su inverso.</li>
</ul>
<p>Igualando término a término las dos funciones de transferencia salen las expresiones de cada H. Conviene terminar comprobando un caso sencillo (por ejemplo, G<sub>2</sub> = 1) para detectar errores de signo.</p>

<h2>Qué nos enseña este examen para la próxima convocatoria</h2>
<ul>
<li><strong>Amplitud antes que profundidad.</strong> Ocho bloques distintos en una sola prueba: dejar uno sin preparar cuesta entre 1 y 1,5 puntos.</li>
<li><strong>La justificación puntúa.</strong> El enunciado lo advierte expresamente: planteamiento, unidades y comprobación valen tanto como el resultado.</li>
<li><strong>Los bloques mecánicos pesan.</strong> Materiales y estructuras sumaron 3 puntos, tanto como electrónica, corriente alterna y control juntos.</li>
<li><strong>El formato cambia.</strong> En 2023 la práctica fueron 4 ejercicios de 2,5 puntos en 2 horas; en 2025, 8 cuestiones de peso desigual. Hay que entrenar los dos formatos.</li>
</ul>
""",
    "faq": [
        ("¿Cuántas cuestiones tuvo la prueba práctica de Tecnología de Madrid en 2025?",
         "Ocho cuestiones sobre 10 puntos: dibujo técnico, neumática e hidráulica, materiales y estructuras, de 1,5 puntos cada una, y máquinas térmicas, electrónica digital, corriente alterna y sistemas de control, de 1 punto cada una."),
        ("¿Qué material se podía usar en la prueba práctica de 2025?",
         "Calculadora no programable, bolígrafos de tinta azul o negra y material de dibujo. Además, todas las respuestas y cálculos debían estar justificados."),
        ("¿Dónde está el enunciado oficial del examen?",
         "La Comunidad de Madrid publicó el enunciado de la prueba práctica de la especialidad 019 (Tecnología) en su web, en el apartado de procesos selectivos de Secundaria 2025."),
        ("¿Por qué no están resueltas con números todas las cuestiones?",
         "Las cuestiones 1, 4, 6 y 8 dependen de una figura del examen (la escala dibujada, la viga con sus cargas, el cronograma y los diagramas de bloques). Para no inventar datos, explico el método completo que permite resolverlas."),
    ],
    "relacionadas": ["supuestos-practicos", "programacion-didactica"],
})

PAGINAS.append({
    "slug": "supuestos-practicos",
    "title": "Supuestos prácticos de Tecnología: oposiciones Madrid | Guía",
    "desc": ("Cómo es la prueba práctica de Tecnología en las oposiciones de Madrid: formato de 2023 y 2025, "
             "bloques que entran, errores que penaliza el tribunal y cómo prepararla."),
    "h1": "Supuestos prácticos de Tecnología: <em>cómo es la prueba y cómo prepararla</em>",
    "eyebrow": "Primera prueba · Parte A · 70 %",
    "resumen": ("La prueba práctica es la parte A de la primera prueba de las oposiciones de Tecnología en Madrid y pesa el 70 % "
                "de su nota. Hace falta al menos un 2,5 para que cuente. En 2023 fueron 4 ejercicios de 2,5 puntos en 2 horas; "
                "en 2025, 8 cuestiones de dibujo técnico, neumática e hidráulica, materiales, estructuras, máquinas térmicas, "
                "electrónica digital, corriente alterna y sistemas de control."),
    "cuerpo": """
<p>En la oposición de Tecnología, la práctica es <strong>el gran filtro</strong>. Según CCOO Madrid, en 2025 se ofertaron 165 plazas de Tecnología y 106 quedaron sin cubrir: no faltan candidatos, faltan aprobados. Y la práctica, eliminatoria y con bloques muy distintos, es donde cae la mayoría.</p>

<h2>Qué pesa y qué nota necesitas</h2>
<ul>
<li>La primera prueba tiene dos partes: <strong>A, prueba práctica (70 %)</strong>, y <strong>B, desarrollo de un tema (30 %)</strong>.</li>
<li>Cada parte exige un mínimo de <strong>2,5 puntos</strong> para que cuente, y la primera prueba se supera con un <strong>5</strong> de media ponderada.</li>
<li>Con ese peso, un punto en la práctica vale más del doble que un punto en el tema.</li>
</ul>

<h2>Cómo ha cambiado el formato: 2023 frente a 2025</h2>
<table class="tabla">
<thead><tr><th></th><th>2023</th><th>2025</th></tr></thead>
<tbody>
<tr><td>Ejercicios</td><td>4 ejercicios teórico-prácticos</td><td>8 cuestiones</td></tr>
<tr><td>Puntuación</td><td>2,5 puntos cada uno</td><td>1,5 o 1 punto según la cuestión</td></tr>
<tr><td>Material</td><td>Bolígrafo y calculadora científica no programable</td><td>Calculadora no programable, bolígrafo y material de dibujo</td></tr>
</tbody>
</table>
<p>La lección es clara: <strong>no se puede preparar solo el formato del último examen</strong>. Hay que dominar problemas largos de varios apartados y, a la vez, resolver con rapidez cuestiones cortas de muchos bloques. Puedes ver el examen de 2025 entero en <a href="/oposiciones-tecnologia/examen-practico-2025/">el examen práctico de 2025 resuelto</a>.</p>

<h2>Bloques que hay que dominar</h2>
<p>El temario oficial de Tecnología es amplio y las convocatorias recientes muestran que el tribunal reparte las cuestiones entre muchos bloques. Estos son los que conviene tener a nivel de examen:</p>
<ul>
<li><strong>Dibujo técnico:</strong> escalas, vistas normalizadas, acotación, perspectivas.</li>
<li><strong>Neumática e hidráulica:</strong> Bernoulli, continuidad, fuerza y consumo de cilindros, esquemas y circuitos electroneumáticos.</li>
<li><strong>Materiales:</strong> ensayos (tracción, dureza, resiliencia), diagrama hierro-carbono, tratamientos térmicos, estructuras cristalinas.</li>
<li><strong>Estructuras y resistencia de materiales:</strong> reacciones, diagramas de cortante y flector, celosías, tensiones.</li>
<li><strong>Máquinas térmicas y motores:</strong> cilindrada, par y potencia, rendimiento, ciclos termodinámicos.</li>
<li><strong>Mecanismos:</strong> relaciones de transmisión, trenes de engranajes, poleas.</li>
<li><strong>Electricidad y corriente alterna:</strong> circuitos RLC, potencias, corrección del factor de potencia, trifásica.</li>
<li><strong>Electrónica analógica y digital:</strong> semiconductores, amplificadores, álgebra de Boole, simplificación, biestables y contadores.</li>
<li><strong>Sistemas de control:</strong> álgebra de bloques, funciones de transferencia, estabilidad.</li>
<li><strong>Programación y robótica:</strong> algoritmia, diagramas de flujo, microcontroladores.</li>
</ul>

<h2>Lo que más penaliza el tribunal</h2>
<ul>
<li><strong>Resultados sin justificar.</strong> El enunciado de 2025 lo exige expresamente.</li>
<li><strong>Errores de unidades:</strong> densidades en kg/L, rpm sin pasar a rad/s, milímetros mezclados con metros.</li>
<li><strong>Dejar cuestiones en blanco.</strong> Un planteamiento correcto suele puntuar aunque el resultado no llegue.</li>
<li><strong>Acotar con medidas del dibujo</strong> en lugar de medidas reales.</li>
<li><strong>Mala gestión del tiempo:</strong> atascarse en una cuestión de 1 punto y no llegar a una de 1,5.</li>
</ul>

<h2>Cómo prepararla</h2>
<ol>
<li><strong>Diagnóstico por bloques.</strong> Qué dominas, qué tienes oxidado y qué no has visto nunca. El plan se construye desde ahí.</li>
<li><strong>Teoría mínima, problemas máximos.</strong> Cada bloque con su formulario y una colección de problemas graduados hasta nivel de examen.</li>
<li><strong>Corrección con criterios de tribunal.</strong> No basta con saber si el resultado es correcto: hay que saber cuánto puntuaría.</li>
<li><strong>Simulacros cronometrados</strong> con los dos formatos: pocos problemas largos y muchas cuestiones cortas.</li>
</ol>
""",
    "faq": [
        ("¿Cuánto pesa la prueba práctica en la oposición de Tecnología de Madrid?",
         "La prueba práctica es la parte A de la primera prueba y pesa el 70 % de su nota; el tema escrito (parte B) pesa el 30 %. Cada parte necesita al menos un 2,5 para que cuente, y la primera prueba se supera con un 5."),
        ("¿Cómo fue el formato de la práctica en 2023 y en 2025?",
         "En 2023 fueron 4 ejercicios teórico-prácticos de 2,5 puntos cada uno en 2 horas. En 2025, 8 cuestiones de distintos bloques con un valor de 1,5 o 1 punto cada una."),
        ("¿Qué bloques entran en la prueba práctica de Tecnología?",
         "En 2025 entraron dibujo técnico, neumática e hidráulica, materiales, estructuras, máquinas térmicas, electrónica digital, corriente alterna y sistemas de control. El temario incluye además mecanismos, electrónica analógica y programación y robótica, que pueden aparecer en otras convocatorias."),
        ("¿Necesito ser ingeniero para aprobar la práctica?",
         "No. Muchos opositores vienen de otras titulaciones. Lo importante es trabajar cada bloque desde los fundamentos hasta el nivel de examen y entrenar con corrección y simulacros."),
    ],
    "relacionadas": ["examen-practico-2025", "programacion-didactica"],
})

PAGINAS.append({
    "slug": "programacion-didactica",
    "title": "Programación didáctica de Tecnología: oposiciones Madrid",
    "desc": ("Cómo hacer y defender la programación didáctica de Tecnología para las oposiciones de la Comunidad de "
             "Madrid: normativa LOMLOE, materias, estructura y errores frecuentes."),
    "h1": "Programación didáctica de Tecnología para las <em>oposiciones de Madrid</em>",
    "eyebrow": "Segunda prueba · Aptitud pedagógica",
    "resumen": ("La segunda prueba de la oposición de Tecnología en Madrid consiste en presentar y defender una programación "
                "didáctica (de hasta 80 páginas, incluidos anexos, en la última convocatoria) y exponer ante el tribunal una "
                "unidad didáctica o situación de aprendizaje. Debe ajustarse al currículo LOMLOE de la Comunidad de Madrid: "
                "Decreto 65/2022 para la ESO y Decreto 64/2022 para el Bachillerato."),
    "cuerpo": """
<p>La programación es la parte de la oposición que <strong>puedes llevar hecha de casa</strong>, y por eso el tribunal es exigente con ella: espera un documento coherente con la normativa, realista para un aula de Madrid y defendido con soltura. Aquí tienes lo esencial para hacerla bien.</p>

<h2>Normativa de referencia en Madrid</h2>
<ul>
<li><strong>LOMLOE</strong> (Ley Orgánica 3/2020), que modifica la LOE.</li>
<li><strong>ESO:</strong> Real Decreto 217/2022 (enseñanzas mínimas) y <strong>Decreto 65/2022, de 20 de julio</strong>, de la Comunidad de Madrid, modificado por el Decreto 59/2024.</li>
<li><strong>Bachillerato:</strong> Real Decreto 243/2022 y <strong>Decreto 64/2022, de 20 de julio</strong>, de la Comunidad de Madrid.</li>
<li>La convocatoria indica que se aplica la normativa <strong>vigente al terminar el plazo de solicitudes</strong>: hay que revisarla cuando salga la de 2027.</li>
</ul>

<h2>Qué materia programar</h2>
<p>La programación se refiere a una materia y un curso de la especialidad. Las más habituales en Tecnología son:</p>
<ul>
<li><strong>Tecnología y Digitalización</strong> (1.º a 3.º de ESO), la opción más común y la que el tribunal conoce mejor.</li>
<li><strong>Tecnología</strong> o <strong>Digitalización</strong> en 4.º de ESO.</li>
<li><strong>Tecnología e Ingeniería I y II</strong> en Bachillerato, que permite lucir nivel técnico pero exige más rigor.</li>
</ul>
<p>Elige la que puedas defender con ejemplos reales de aula. Una programación de Bachillerato brillante pierde fuerza si las situaciones de aprendizaje no son creíbles.</p>

<h2>Estructura que espera el tribunal</h2>
<ol>
<li><strong>Contexto</strong> del centro y del grupo, concreto y verosímil (sin exceso de páginas).</li>
<li><strong>Competencias específicas</strong> de la materia y su relación con las competencias clave y el perfil de salida.</li>
<li><strong>Saberes básicos</strong> organizados y temporalizados.</li>
<li><strong>Situaciones de aprendizaje</strong>, el núcleo de una programación LOMLOE: retos con producto final, conectados con criterios de evaluación.</li>
<li><strong>Metodología</strong>: aprendizaje basado en proyectos, método de proyectos tecnológico, trabajo en el aula-taller.</li>
<li><strong>Evaluación</strong>: criterios, instrumentos (rúbricas, listas de cotejo, portfolio) y criterios de calificación.</li>
<li><strong>Atención a las diferencias individuales</strong> y Diseño Universal para el Aprendizaje.</li>
<li><strong>Recursos, seguridad en el taller y actividades complementarias.</strong></li>
</ol>

<h2>Extensión y formato</h2>
<p>En la última convocatoria la programación tenía una <strong>extensión máxima de 80 páginas, incluidos anexos y materiales de apoyo</strong>. Cada convocatoria fija además el formato (tipo de letra, interlineado, márgenes): incumplirlo puede costar puntos o la exclusión del documento, así que hay que comprobarlo en cuanto se publique.</p>

<h2>La defensa ante el tribunal</h2>
<ul>
<li>La exposición de la programación y de la unidad didáctica o situación de aprendizaje se hace <strong>en sesión pública</strong>, en el tiempo que fija la convocatoria.</li>
<li>El tribunal valora que conozcas tu programación sin leerla, que justifiques cada decisión y que la unidad elegida sea <strong>aplicable de verdad</strong> en un aula.</li>
<li>Lo que más diferencia: ejemplos reales del taller, gestión de la diversidad concreta y una evaluación que se entienda en dos minutos.</li>
</ul>

<h2>Errores frecuentes</h2>
<ul>
<li>Copiar una programación ajena: el tribunal lo detecta en la defensa en cuanto pregunta por una decisión.</li>
<li>Normativa desactualizada (referencias a LOMCE o a estándares de aprendizaje).</li>
<li>Situaciones de aprendizaje que son simples listas de actividades, sin reto ni producto.</li>
<li>Criterios de calificación que no suman 100 % o no se relacionan con los criterios de evaluación.</li>
<li>Una temporalización imposible para las horas semanales de la materia.</li>
</ul>
""",
    "faq": [
        ("¿Qué extensión tiene la programación didáctica en las oposiciones de Madrid?",
         "En la última convocatoria, un máximo de 80 páginas incluidos los materiales de apoyo y los anexos. El formato concreto lo fija cada convocatoria."),
        ("¿Qué normativa hay que usar para la programación de Tecnología en Madrid?",
         "La LOMLOE y el currículo de la Comunidad de Madrid: Decreto 65/2022 para la ESO (modificado por el Decreto 59/2024) y Decreto 64/2022 para el Bachillerato, con la normativa vigente al terminar el plazo de solicitudes."),
        ("¿Qué materia es mejor programar para la oposición de Tecnología?",
         "La más habitual es Tecnología y Digitalización de 1.º a 3.º de ESO. Tecnología e Ingeniería de Bachillerato permite mostrar más nivel técnico, pero exige mayor rigor. Lo importante es poder defenderla con ejemplos reales de aula."),
        ("¿Revisas programaciones ya hechas?",
         "Sí. Hago una lectura crítica de la programación con un informe escrito de mejoras y una sesión de simulacro de defensa por videollamada."),
    ],
    "relacionadas": ["supuestos-practicos", "examen-practico-2025"],
})

TITULOS_CORTOS = {
    "examen-practico-2025": "Examen práctico 2025 resuelto",
    "supuestos-practicos": "Supuestos prácticos: cómo es la prueba",
    "programacion-didactica": "Programación didáctica en Madrid",
}

# ───────────────────────── plantilla ─────────────────────────
CSS = """
body{margin:0;background:#EDF0F3;color:#0E1A2B;font-family:'IBM Plex Sans',system-ui,sans-serif}
a{color:#0E1A2B}a:hover{color:#C2410C}
.wrap{max-width:860px;margin:0 auto;padding:0 24px}
header.top{position:sticky;top:0;z-index:10;background:rgba(237,240,243,.94);border-bottom:1px solid #C9D1DB}
header.top .in{max-width:1180px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:12px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none}
.badge{display:flex;align-items:center;justify-content:center;width:40px;height:40px;background:#0E1A2B;color:#fff;font-family:'IBM Plex Mono',monospace;font-size:13px}
.bname{font-family:'Archivo',sans-serif;font-weight:800;font-size:17px}
.bsub{display:block;font-family:'IBM Plex Mono',monospace;font-size:11px;color:#4A5568;letter-spacing:.04em}
.wa{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;background:#25D366;color:#0E1A2B;text-decoration:none;font-weight:700;font-size:15px}
.crumbs{font-family:'IBM Plex Mono',monospace;font-size:12px;color:#4A5568;margin:40px 0 16px}
.crumbs a{color:#4A5568}
.eyebrow{font-family:'IBM Plex Mono',monospace;font-size:13px;letter-spacing:.08em;color:#C2410C;text-transform:uppercase}
h1{font-family:'Archivo',sans-serif;font-weight:800;font-size:46px;line-height:1.05;letter-spacing:-.02em;margin:12px 0 18px}
h1 em{font-style:normal;color:#C2410C}
.meta{font-family:'IBM Plex Mono',monospace;font-size:12px;color:#4A5568;margin-bottom:28px}
.resumen{background:#fff;border-left:4px solid #C2410C;padding:18px 22px;font-size:17px;line-height:1.6;margin:0 0 32px}
article{font-size:17px;line-height:1.7;color:#24303F}
article h2{font-family:'Archivo',sans-serif;font-weight:800;font-size:28px;line-height:1.15;letter-spacing:-.01em;color:#0E1A2B;margin:44px 0 12px;scroll-margin-top:90px}
article ul,article ol{padding-left:22px}article li{margin-bottom:6px}
.enunciado{background:#E2E7ED;padding:14px 18px;font-size:15px;line-height:1.6}
.f{font-family:'IBM Plex Mono',monospace;font-size:15px;background:#fff;padding:2px 6px;display:inline-block}
p.f{display:block;padding:10px 14px;overflow-x:auto}
.tabla{border-collapse:collapse;width:100%;background:#fff;font-size:15px;margin:12px 0}
.tabla th,.tabla td{border:1px solid #C9D1DB;padding:8px 12px;text-align:left}
.tabla th{background:#0E1A2B;color:#fff;font-weight:600}
.cta{background:#0E1A2B;color:#E6EBF1;padding:28px;margin:48px 0}
.cta h2{color:#fff;margin-top:0}.cta p{color:#C9D1DB}
.cta a.wa{margin-top:8px}
.faq details{border-bottom:1px solid #C9D1DB;padding:14px 0}
.faq summary{cursor:pointer;font-weight:600;font-size:17px}
.rel{list-style:none;padding:0}.rel li{border-bottom:1px solid #C9D1DB;padding:10px 0}
footer{background:#0A1320;color:#8A96A6;margin-top:64px;padding:28px 0;font-size:14px}
footer a{color:#C9D1DB}
@media (max-width:720px){h1{font-size:34px}article h2{font-size:24px}.bsub{display:none}}
a:focus-visible,summary:focus-visible{outline:2px solid #C2410C;outline-offset:2px}
"""


def wa_link(texto):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(texto)}"


def pagina(p):
    url = f"{BASE}/{p['slug']}/"
    texto_plano = re.sub(r"<[^>]+>", "", p["h1"])
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "@id": url + "#articulo", "headline": texto_plano, "description": p["desc"],
         "url": url, "mainEntityOfPage": url, "inLanguage": "es-ES", "datePublished": FECHA, "dateModified": FECHA,
         "author": AUTOR, "publisher": {"@id": BASE + "/#enrique"}, "image": IMG,
         "about": ["Oposiciones de Tecnología", "Cuerpo 0590", "Comunidad de Madrid"],
         "isPartOf": {"@id": BASE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Preparación oposiciones Tecnología", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": TITULOS_CORTOS[p["slug"]], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
    ]}
    faq_html = "\n".join(
        f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in p["faq"])
    rel_html = "\n".join(
        f'<li><a href="/oposiciones-tecnologia/{s}/">{esc(TITULOS_CORTOS[s])} →</a></li>' for s in p["relacionadas"])
    wa_txt = f"Hola Enrique, he leído tu página «{TITULOS_CORTOS[p['slug']]}» y quería información sobre la preparación."
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['desc'])}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="author" content="Enrique Delgado Huerta">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Preparación oposiciones Tecnología · Enrique Delgado">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:locale" content="es_ES">
<meta property="og:image" content="{IMG}">
<meta property="article:modified_time" content="{FECHA}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0E1A2B">
<link rel="icon" href="/oposiciones-tecnologia/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&amp;family=IBM+Plex+Sans:wght@400;600&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top"><div class="in">
<a class="brand" href="/oposiciones-tecnologia/"><span class="badge">0590</span><span><span class="bname">Enrique Delgado</span><span class="bsub">PREPARADOR · OPOSICIONES TECNOLOGÍA</span></span></a>
<a class="wa" href="{wa_link(wa_txt)}" target="_blank" rel="noopener">WhatsApp</a>
</div></header>
<main class="wrap">
<nav class="crumbs" aria-label="Migas de pan"><a href="/oposiciones-tecnologia/">Preparación oposiciones Tecnología</a> › {esc(TITULOS_CORTOS[p['slug']])}</nav>
<span class="eyebrow">{esc(p['eyebrow'])}</span>
<h1>{p['h1']}</h1>
<p class="meta">Por Enrique Delgado Huerta, profesor de Tecnología (Cuerpo 0590) · Actualizado el 17/11/2026</p>
<p class="resumen"><strong>En resumen:</strong> {esc(p['resumen'])}</p>
<article>
{p['cuerpo']}
<section class="cta" aria-labelledby="h-cta">
<h2 id="h-cta">Prepara la convocatoria de 2027 con método</h2>
<p>Clases online en directo, grupos de máximo 4 opositores, corrección individual con criterios de tribunal y simulacros. Soy profesor de Tecnología, funcionario de carrera, e ingeniero técnico industrial en electrónica.</p>
<a class="wa" href="{wa_link(wa_txt)}" target="_blank" rel="noopener">Escríbeme por WhatsApp</a>
<p style="margin-top:14px"><a href="/oposiciones-tecnologia/#modalidades" style="color:#fff">Ver modalidades de preparación →</a></p>
</section>
<section class="faq" aria-labelledby="h-faq">
<h2 id="h-faq">Preguntas frecuentes</h2>
{faq_html}
</section>
<section aria-labelledby="h-rel">
<h2 id="h-rel">Sigue leyendo</h2>
<ul class="rel">
{rel_html}
<li><a href="/oposiciones-tecnologia/">Preparación de la oposición de Tecnología en Madrid →</a></li>
</ul>
</section>
</article>
</main>
<footer><div class="wrap">© 2026 Enrique Delgado Huerta · Preparación de oposiciones de Tecnología · Clases online · Comunidad de Madrid · <a href="/">informeperitoinformatico.es</a></div></footer>
</body>
</html>
"""


def sitemap():
    urls = [("", "1.0")] + [(p["slug"] + "/", "0.8") for p in PAGINAS]
    filas = []
    for u, pr in urls:
        img = ""
        if u == "":
            img = f"\n    <image:image><image:loc>{IMG}</image:loc></image:image>"
        filas.append(f"  <url>\n    <loc>{BASE}/{u}</loc>\n    <lastmod>{FECHA}</lastmod>{img}\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(filas) + "\n</urlset>\n")


def main():
    for p in PAGINAS:
        d = os.path.join(ROOT, p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(pagina(p))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap())
    print(f"{len(PAGINAS)} páginas: " + ", ".join("/" + p["slug"] + "/" for p in PAGINAS))


if __name__ == "__main__":
    main()
