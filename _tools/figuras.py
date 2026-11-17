"""Figuras SVG con la solución de cada cuestión del examen práctico 2025 (Tecnología, Madrid)."""
import math

INK = "#0E1A2B"
ACC = "#C2410C"
GRID = "#C9D1DB"
MUTED = "#4A5568"
FONT = "font-family=\"IBM Plex Sans, Arial, sans-serif\""


def fig(svg, pie):
    return (f'<figure class="sol"><div class="svgwrap">{svg}</div>'
            f'<figcaption>{pie}</figcaption></figure>\n')


def svg_open(w, h, titulo):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="{titulo}" {FONT} font-size="13"><title>{titulo}</title>'
            f'<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            f'<marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{ACC}"/></marker></defs>')


def cota_h(x1, x2, y, txt, ext_from=None):
    s = ""
    if ext_from is not None:
        s += f'<line x1="{x1}" y1="{ext_from}" x2="{x1}" y2="{y+4}" stroke="{MUTED}" stroke-width="0.8"/>'
        s += f'<line x1="{x2}" y1="{ext_from}" x2="{x2}" y2="{y+4}" stroke="{MUTED}" stroke-width="0.8"/>'
    s += (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{MUTED}" stroke-width="0.8" '
          f'marker-start="url(#ar)" marker-end="url(#ar)"/>')
    s += f'<text x="{(x1+x2)/2}" y="{y-5}" text-anchor="middle" fill="{INK}">{txt}</text>'
    return s


def cota_v(x, y1, y2, txt, ext_from=None):
    s = ""
    if ext_from is not None:
        s += f'<line x1="{ext_from}" y1="{y1}" x2="{x-4 if x < ext_from else x+4}" y2="{y1}" stroke="{MUTED}" stroke-width="0.8"/>'
        s += f'<line x1="{ext_from}" y1="{y2}" x2="{x-4 if x < ext_from else x+4}" y2="{y2}" stroke="{MUTED}" stroke-width="0.8"/>'
    s += (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{MUTED}" stroke-width="0.8" '
          f'marker-start="url(#ar)" marker-end="url(#ar)"/>')
    cy = (y1 + y2) / 2
    s += f'<text x="{x-6}" y="{cy}" text-anchor="middle" fill="{INK}" transform="rotate(-90 {x-6} {cy})">{txt}</text>'
    return s


# ───────────── C1: vista a escala 1:5 acotada ─────────────
def c1():
    k = 8  # px por cm real (dibujo ilustrativo)
    ox, oy = 90, 70
    X = lambda cm: ox + cm * k
    Y = lambda cm: oy + cm * k  # y hacia abajo desde el borde superior
    pts = [(0, 0), (30, 0), (30, 10), (45, 10), (45, 30), (0, 30)]
    poly = " ".join(f"{X(a)},{Y(b)}" for a, b in pts)
    s = svg_open(640, 400, "Vista de la cuestión 1 dibujada a escala 1:5 y acotada")
    s += f'<polygon points="{poly}" fill="#fff" stroke="{INK}" stroke-width="2.2"/>'
    cx, cy, r = X(10), Y(20), 5 * k
    s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2.2"/>'
    s += (f'<line x1="{cx-r-8}" y1="{cy}" x2="{cx+r+8}" y2="{cy}" stroke="{ACC}" stroke-width="0.8" stroke-dasharray="10 3 2 3"/>'
          f'<line x1="{cx}" y1="{cy-r-8}" x2="{cx}" y2="{cy+r+8}" stroke="{ACC}" stroke-width="0.8" stroke-dasharray="10 3 2 3"/>')
    # cotas
    s += cota_h(X(0), X(45), Y(30) + 52, "450", ext_from=Y(30) + 4)
    s += cota_h(X(0), X(10), Y(30) + 24, "100", ext_from=Y(30) + 4)
    s += cota_h(X(30), X(45), Y(0) - 22, "150", ext_from=Y(10) - 4)
    s += cota_v(X(0) - 50, Y(0), Y(30), "300", ext_from=X(0) - 4)
    s += cota_v(X(45) + 30, Y(0) + 0.001, Y(10), "100", ext_from=X(30) + 4)
    s += cota_v(X(0) - 22, Y(20), Y(30), "100", ext_from=X(0) - 4)
    # diámetro
    ang = math.radians(40)
    px, py = cx + r * math.cos(ang), cy - r * math.sin(ang)
    s += (f'<line x1="{cx - r*math.cos(ang)}" y1="{cy + r*math.sin(ang)}" x2="{px}" y2="{py}" stroke="{MUTED}" '
          f'stroke-width="0.8" marker-start="url(#ar)" marker-end="url(#ar)"/>'
          f'<line x1="{px}" y1="{py}" x2="{px+46}" y2="{py-30}" stroke="{MUTED}" stroke-width="0.8"/>'
          f'<text x="{px+48}" y="{py-34}" fill="{INK}">⌀100</text>')
    s += (f'<text x="{X(45)+60}" y="{Y(20)}" fill="{ACC}" font-weight="700" font-size="15">E 1:5</text>'
          f'<text x="{X(45)+60}" y="{Y(20)+18}" fill="{MUTED}" font-size="12">Cotas en mm</text>'
          f'<text x="{X(45)+60}" y="{Y(20)+34}" fill="{MUTED}" font-size="12">(medidas reales)</text>')
    s += "</svg>"
    return fig(s, "Cuestión 1. Vista de 45 × 30 cm a escala 1:5 (en el papel, 90 × 60 mm), acotada con las medidas reales en milímetros. Figura ilustrativa, no a tamaño real.")


# ───────────── C2: tubería ─────────────
def c2():
    s = svg_open(600, 230, "Esquema de la instalación hidráulica de la cuestión 2 con sus resultados")
    s += f'<rect x="40" y="70" width="230" height="60" fill="#E2E7ED" stroke="{INK}" stroke-width="2"/>'
    s += f'<path d="M270,70 L330,94 L330,106 L270,130 Z" fill="#E2E7ED" stroke="{INK}" stroke-width="2"/>'
    s += f'<rect x="330" y="94" width="230" height="12" fill="#E2E7ED" stroke="{INK}" stroke-width="2"/>'
    for x, lab, p in ((150, "d₁ = 10 mm", "p₁ = 3·10⁶ Pa"), (440, "d₂ = 2 mm", "p₂ = 5·10⁵ Pa")):
        top = 70 if x < 300 else 94
        s += (f'<line x1="{x}" y1="{top}" x2="{x}" y2="30" stroke="{INK}" stroke-width="1.5"/>'
              f'<circle cx="{x}" cy="22" r="12" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
              f'<line x1="{x}" y1="22" x2="{x+7}" y2="15" stroke="{ACC}" stroke-width="1.5"/>'
              f'<text x="{x+20}" y="20" fill="{INK}">{p}</text>')
    s += (f'<line x1="80" y1="100" x2="230" y2="100" stroke="{ACC}" stroke-width="2" marker-end="url(#arA)"/>'
          f'<text x="155" y="150" text-anchor="middle" fill="{INK}">d₁ = 10 mm · v₁ ≈ 2,98 m/s</text>'
          f'<line x1="360" y1="100" x2="540" y2="100" stroke="{ACC}" stroke-width="2" marker-end="url(#arA)"/>'
          f'<text x="445" y="130" text-anchor="middle" fill="{INK}">d₂ = 2 mm · v₂ ≈ 74,6 m/s</text>')
    s += (f'<rect x="150" y="172" width="300" height="40" fill="{INK}"/>'
          f'<text x="300" y="198" text-anchor="middle" fill="#fff" font-weight="700" font-size="15">Q ≈ 2,34·10⁻⁴ m³/s ≈ 14,1 L/min</text>')
    s += "</svg>"
    return fig(s, "Cuestión 2. Al pasar de 10 a 2 mm la velocidad se multiplica por 25 y la presión cae: Bernoulli horizontal más continuidad dan el caudal.")


# ───────────── C3: curva de tracción ─────────────
def c3():
    s = svg_open(600, 340, "Curva tensión-deformación del ensayo de tracción de un acero con 0,5 % de carbono")
    ox, oy = 70, 290
    s += (f'<line x1="{ox}" y1="{oy}" x2="560" y2="{oy}" stroke="{INK}" stroke-width="1.5" marker-end="url(#ar)"/>'
          f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="25" stroke="{INK}" stroke-width="1.5" marker-end="url(#ar)"/>'
          f'<text x="555" y="{oy+20}" fill="{INK}" text-anchor="end">ε = ΔL / L₀</text>'
          f'<text x="{ox-10}" y="30" fill="{INK}" text-anchor="end">σ = F / S₀</text>')
    d = (f"M{ox},{oy} L120,150 "            # elástica
         f"L126,140 L132,150 L170,152 L174,146 "  # fluencia (superior/inferior)
         f"C230,100 300,72 360,70 "         # endurecimiento hasta máximo
         f"C410,70 450,95 490,150")         # estricción y rotura
    s += f'<path d="{d}" fill="none" stroke="{ACC}" stroke-width="3"/>'
    s += f'<circle cx="490" cy="150" r="4" fill="{INK}"/>'
    lab = [(120, 150, "σP ≈ σE", -10, 4, "end"), (150, 152, "Fluencia", 0, 22, "middle"),
           (360, 70, "σR = Fmáx / S₀ (resistencia a la tracción)", 0, -14, "middle"), (490, 150, "Rotura", 8, 4, "start")]
    for x, y, t, dx, dy, a in lab:
        s += f'<text x="{x+dx}" y="{y+dy}" fill="{INK}" text-anchor="{a}" font-size="12">{t}</text>'
    s += (f'<text x="104" y="250" fill="{MUTED}" font-size="12">σ = E·ε (Hooke)</text>'
          f'<line x1="{ox}" y1="{oy+28}" x2="160" y2="{oy+28}" stroke="{MUTED}" stroke-width="0.8" marker-start="url(#ar)" marker-end="url(#ar)"/>'
          f'<text x="115" y="{oy+44}" fill="{MUTED}" font-size="12" text-anchor="middle">Zona elástica</text>'
          f'<line x1="160" y1="{oy+28}" x2="360" y2="{oy+28}" stroke="{MUTED}" stroke-width="0.8" marker-start="url(#ar)" marker-end="url(#ar)"/>'
          f'<text x="260" y="{oy+44}" fill="{MUTED}" font-size="12" text-anchor="middle">Zona plástica (endurecimiento)</text>'
          f'<line x1="360" y1="{oy+28}" x2="490" y2="{oy+28}" stroke="{MUTED}" stroke-width="0.8" marker-start="url(#ar)" marker-end="url(#ar)"/>'
          f'<text x="425" y="{oy+44}" fill="{MUTED}" font-size="12" text-anchor="middle">Estricción</text>')
    s += "</svg>"
    return fig(s, "Cuestión 3. Curva σ–ε de un acero hipoeutectoide (0,5 % C): zona elástica (Hooke), fluencia, endurecimiento hasta σR y estricción hasta la rotura. Gráfica cualitativa, a mano alzada como pide el enunciado.")


# ───────────── C4: viga y diagramas ─────────────
def c4():
    s = svg_open(600, 520, "Viga en voladizo con carga repartida y diagramas de cortante y momento flector")
    x0, x1 = 90, 510  # 6 m
    L = x1 - x0
    # viga
    s += f'<rect x="{x0}" y="90" width="{L}" height="14" fill="#E2E7ED" stroke="{INK}" stroke-width="2"/>'
    s += f'<line x1="{x0}" y1="60" x2="{x0}" y2="134" stroke="{INK}" stroke-width="3"/>'
    for i in range(8):
        y = 62 + i * 9
        s += f'<line x1="{x0}" y1="{y}" x2="{x0-10}" y2="{y+9}" stroke="{INK}" stroke-width="1"/>'
    s += f'<line x1="{x0}" y1="48" x2="{x1}" y2="48" stroke="{INK}" stroke-width="1.2"/>'
    for i in range(13):
        x = x0 + i * L / 12
        s += f'<line x1="{x}" y1="48" x2="{x}" y2="86" stroke="{INK}" stroke-width="1.2" marker-end="url(#ar)"/>'
    s += f'<text x="{(x0+x1)/2}" y="38" text-anchor="middle" fill="{INK}">q = 52 kN/m</text>'
    s += cota_h(x0, x1, 128, "6 m")
    s += (f'<line x1="{x0-30}" y1="140" x2="{x0-30}" y2="100" stroke="{ACC}" stroke-width="2.2" marker-end="url(#arA)"/>'
          f'<text x="{x0-34}" y="158" text-anchor="middle" fill="{ACC}" font-weight="700">RA = 312 kN</text>'
          f'<path d="M{x0-48},84 A26,26 0 1,1 {x0-20},74" fill="none" stroke="{ACC}" stroke-width="2" marker-end="url(#arA)"/>'
          f'<text x="{x0-36}" y="28" text-anchor="middle" fill="{ACC}" font-weight="700">MA = 936 kN·m</text>')
    # cortante
    yb, hV = 270, 80
    s += f'<text x="20" y="{yb-hV/2}" fill="{INK}" font-weight="700">V</text>'
    s += f'<line x1="{x0}" y1="{yb}" x2="{x1+20}" y2="{yb}" stroke="{INK}" stroke-width="1"/>'
    s += f'<polygon points="{x0},{yb} {x0},{yb-hV} {x1},{yb}" fill="#F6D9C9" stroke="{ACC}" stroke-width="2"/>'
    s += (f'<text x="{x0+6}" y="{yb-hV-6}" fill="{INK}">312 kN</text>'
          f'<text x="{x1+4}" y="{yb-6}" fill="{INK}">0</text>'
          f'<text x="{(x0+x1)/2+30}" y="{yb-hV/2+10}" fill="{MUTED}" font-size="12">V(x) = 312 − 52x</text>')
    # flector
    ym, hM = 330, 140
    s += f'<text x="20" y="{ym+hM/2}" fill="{INK}" font-weight="700">M</text>'
    s += f'<line x1="{x0}" y1="{ym}" x2="{x1+20}" y2="{ym}" stroke="{INK}" stroke-width="1"/>'
    pts = []
    for i in range(61):
        xm = 6 * i / 60
        M = -936 + 312 * xm - 26 * xm * xm
        pts.append(f"{x0 + L*xm/6:.1f},{ym - M/936*hM:.1f}")
    s += f'<polygon points="{x0},{ym} {" ".join(pts)}" fill="#F6D9C9" stroke="{ACC}" stroke-width="2"/>'
    s += (f'<text x="{x0+6}" y="{ym+hM+18}" fill="{INK}">−936 kN·m</text>'
          f'<text x="{x1+4}" y="{ym-6}" fill="{INK}">0</text>'
          f'<text x="{(x0+x1)/2+10}" y="{ym+hM/2+20}" fill="{MUTED}" font-size="12">M(x) = −936 + 312x − 26x²</text>')
    s += "</svg>"
    return fig(s, "Cuestión 4. Voladizo de 6 m con 52 kN/m: reacción de 312 kN y momento de empotramiento de 936 kN·m. Cortante lineal y flector parabólico (negativo), ambos nulos en el extremo libre.")


# ───────────── C5: cilindro ─────────────
def c5():
    s = svg_open(600, 250, "Esquema del cilindro y resultados de la cuestión 5")
    s += (f'<rect x="80" y="40" width="120" height="170" fill="none" stroke="{INK}" stroke-width="2.5"/>'
          f'<rect x="84" y="120" width="112" height="40" fill="#E2E7ED" stroke="{INK}" stroke-width="1.5"/>'
          f'<line x1="140" y1="160" x2="140" y2="232" stroke="{INK}" stroke-width="3"/>'
          f'<rect x="84" y="56" width="112" height="64" fill="#F6D9C9" opacity="0.7"/>')
    s += cota_h(80, 200, 28, "D = 80,5 mm")
    s += cota_v(230, 56, 120, "L = 97,6 mm")
    s += (f'<text x="140" y="94" text-anchor="middle" fill="{ACC}" font-size="12">Vu ≈ 496,7 cm³</text>'
          f'<rect x="290" y="50" width="280" height="64" fill="{INK}"/>'
          f'<text x="430" y="78" text-anchor="middle" fill="#fff" font-weight="700" font-size="15">VT = 4 · Vu ≈ 1987 cm³</text>'
          f'<text x="430" y="100" text-anchor="middle" fill="#C9D1DB" font-size="12">4 cilindros</text>'
          f'<rect x="290" y="130" width="280" height="64" fill="{INK}"/>'
          f'<text x="430" y="158" text-anchor="middle" fill="#fff" font-weight="700" font-size="15">M = P / ω ≈ 34 N·m</text>'
          f'<text x="430" y="180" text-anchor="middle" fill="#C9D1DB" font-size="12">22 065 W / 649,3 rad/s</text>')
    s += "</svg>"
    return fig(s, "Cuestión 5. Cilindrada unitaria (sección del pistón por carrera), total para 4 cilindros y par motor con la potencia en W y la velocidad en rad/s.")


# ───────────── C6: cronograma ─────────────
CLK = "?????????00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|00000000000|11111111111|0000000"
JS = "?????????00000000000000000|11111111111111111111111111111|00000000000000000|11111|00000000000000000000000|11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111|00000|11111111111111111|00000000000000000000000|11111|00000000000000000|11111111111111111|00000000000|1111111111111111111111111"
KS = "?????????00000000000000000000000000000|11111111111111111111111111111111111111111|00000000000000000000000000000000000000000|11111111111111111111111111111111111111111111111111111111111100000000000000000000000|11111111111111111111111111111111111111111|00000000000000000000000000000|1111111111111111111111111111111111111111111111111"


def _niveles(sv, n):
    out, last = [], 0
    for i in range(n):
        c = sv[i] if i < len(sv) else "?"
        if c in "01":
            last = int(c)
            out.append(last)
        elif c == "|":
            nxt = next((int(x) for x in sv[i+1:] if x in "01"), last)
            out.append(nxt)
        else:
            out.append(None)
    return out


def c6():
    n = len(CLK)
    start, end = 9, n
    clk = _niveles(CLK, n)
    j = _niveles(JS, n)
    k = _niveles(KS, n)
    edges = [i for i in range(1, n - 1) if CLK[i] == "|" and CLK[i-1] == "0"]
    q, Q = 0, []
    for e in edges:
        jj, kk = j[e-1], k[e-1]
        if jj == 1 and kk == 0:
            q = 1
        elif jj == 0 and kk == 1:
            q = 0
        elif jj == 1 and kk == 1:
            q = 1 - q
        Q.append((e, q))
    s_lv = []
    cur = 0
    for i in range(n):
        for e, v in Q:
            if i == e:
                cur = v
        s_lv.append(cur)
    W, x0 = 620, 60
    sx = (W - x0 - 10) / (end - start)
    X = lambda i: x0 + (i - start) * sx
    rows = [("CLK", clk, INK), ("J", j, INK), ("K", k, INK), ("S = Q", s_lv, ACC)]
    H = 40 + 52 * len(rows) + 20
    s = svg_open(W, H, "Cronograma de la cuestión 6 con la salida del biestable JK")
    for e in edges:
        s += f'<line x1="{X(e)}" y1="24" x2="{X(e)}" y2="{H-14}" stroke="{GRID}" stroke-width="1" stroke-dasharray="3 3"/>'
    for idx, (e, v) in enumerate(Q, 1):
        s += f'<text x="{X(e)}" y="16" text-anchor="middle" fill="{MUTED}" font-size="10">{idx}</text>'
    for r, (name, lv, col) in enumerate(rows):
        base = 40 + 52 * r + 30
        hi = base - 24
        s += f'<text x="{x0-10}" y="{base-8}" text-anchor="end" fill="{col}" font-weight="700">{name}</text>'
        d, prev = "", None
        for i in range(start, end):
            v = lv[i]
            if v is None:
                continue
            y = hi if v else base
            if prev is None:
                d += f"M{X(i):.1f},{y}"
            elif v != prev:
                d += f" L{X(i):.1f},{base if prev == 0 else hi} L{X(i):.1f},{y}"
            prev = v
        d += f" L{X(end-1):.1f},{hi if prev else base}"
        s += f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{2.6 if col == ACC else 1.8}"/>'
    s += "</svg>"
    return fig(s, "Cuestión 6. JK por flanco de subida, Q = 0 al inicio. Las líneas discontinuas marcan los 13 flancos ascendentes; S solo cambia en ellos: 0 · 1 · 0 · 0 · 1 · 0 · 1 · 1 · 0 · 0 · 0 · 1 · 0.")


# ───────────── C7: diagrama fasorial ─────────────
def c7():
    s = svg_open(600, 340, "Diagrama fasorial de la corrección del factor de potencia de la cuestión 7")
    ox, oy, k = 70, 60, 6.5  # px por amperio
    phi = math.acos(0.7)
    phi2 = math.acos(0.7 / 0.74)
    I, I2 = 5000 / (220 * 0.7), 0.74 * 5000 / (220 * 0.7)
    ix, iy = ox + I * math.cos(phi) * k, oy + I * math.sin(phi) * k
    jx, jy = ox + I2 * math.cos(phi2) * k, oy + I2 * math.sin(phi2) * k
    s += (f'<line x1="{ox}" y1="{oy}" x2="560" y2="{oy}" stroke="{INK}" stroke-width="2.4" marker-end="url(#ar)"/>'
          f'<text x="556" y="{oy-8}" text-anchor="end" fill="{INK}" font-weight="700">V = 220 V (referencia)</text>'
          f'<line x1="{ox}" y1="{oy}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="{MUTED}" stroke-width="2.2" marker-end="url(#ar)"/>'
          f'<text x="{ix+12:.1f}" y="{iy+6:.1f}" fill="{MUTED}">I = 32,47 A (φ = 45,6°)</text>'
          f'<line x1="{ox}" y1="{oy}" x2="{jx:.1f}" y2="{jy:.1f}" stroke="{ACC}" stroke-width="3" marker-end="url(#arA)"/>'
          f'<text x="{jx+12:.1f}" y="{jy+4:.1f}" fill="{ACC}" font-weight="700">I′ = 24,03 A (φ′ = 18,9°)</text>'
          f'<line x1="{ix:.1f}" y1="{iy:.1f}" x2="{jx:.1f}" y2="{jy+3:.1f}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#ar)"/>'
          f'<text x="{ix+10:.1f}" y="{(iy+jy)/2+10:.1f}" fill="{INK}">IC ≈ 15,4 A (adelantada 90°)</text>'
          f'<line x1="{ix:.1f}" y1="{oy}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="{GRID}" stroke-width="1" stroke-dasharray="2 3"/>'
          f'<text x="{ix+8:.1f}" y="{oy+16}" fill="{MUTED}" font-size="12">I·cos φ = I′·cos φ′ ≈ 22,7 A (P constante)</text>')
    s += (f'<rect x="60" y="290" width="480" height="38" fill="{INK}"/>'
          f'<text x="300" y="315" text-anchor="middle" fill="#fff" font-weight="700">cos φ′ = 0,7 / 0,74 ≈ 0,946 · i′(t) ≈ 34,0 · sen(100πt − 0,330) A</text>')
    s += "</svg>"
    return fig(s, "Cuestión 7. El condensador aporta una corriente adelantada 90° que anula parte de la componente reactiva; la componente activa (22,7 A) no cambia. C ≈ 223 µF.")


# ───────────── C8: diagramas de bloques ─────────────
def _bloque(x, y, txt, w=90):
    return (f'<rect x="{x}" y="{y-20}" width="{w}" height="40" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            f'<text x="{x+w/2}" y="{y+5}" text-anchor="middle" fill="{INK}" font-weight="700" font-size="15">{txt}</text>')


def _sum(x, y):
    r = 14
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="2"/>'
            f'<line x1="{x-10}" y1="{y-10}" x2="{x+10}" y2="{y+10}" stroke="{INK}" stroke-width="1.5"/>'
            f'<line x1="{x-10}" y1="{y+10}" x2="{x+10}" y2="{y-10}" stroke="{INK}" stroke-width="1.5"/>'
            f'<text x="{x-24}" y="{y-6}" fill="{INK}" font-size="12">+</text>'
            f'<text x="{x+4}" y="{y+30}" fill="{INK}" font-size="14">−</text>')


def c8():
    s = svg_open(620, 330, "Sistema equivalente con realimentación unitaria de la cuestión 8")
    y = 60
    s += f'<text x="10" y="22" fill="{MUTED}" font-weight="700">Figura a (dada)</text>'
    s += (f'<line x1="20" y1="{y}" x2="96" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/><text x="24" y="{y-8}">X</text>'
          + _sum(110, y) +
          f'<line x1="124" y1="{y}" x2="200" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/><text x="150" y="{y-8}">Y</text>'
          + _bloque(200, y, "G1") +
          f'<line x1="290" y1="{y}" x2="380" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/><text x="364" y="{y-8}">Z</text>'
          f'<polyline points="330,{y} 330,{y+60} 290,{y+60}" fill="none" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/>'
          + _bloque(200, y + 60, "G2") +
          f'<polyline points="200,{y+60} 110,{y+60} 110,{y+16}" fill="none" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/>'
          f'<text x="410" y="{y+12}" fill="{INK}" font-size="14">Z/X = G1 / (1 + G1·G2)</text>')
    y = 230
    s += f'<text x="10" y="{y-58}" fill="{ACC}" font-weight="700">Figura b equivalente (solución)</text>'
    s += (f'<line x1="20" y1="{y}" x2="50" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/><text x="22" y="{y-8}">X</text>'
          + _bloque(50, y, "1/G2", 80) +
          f'<line x1="130" y1="{y}" x2="166" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/>'
          + _sum(180, y) +
          f'<line x1="194" y1="{y}" x2="240" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/><text x="210" y="{y-8}">Y</text>'
          + _bloque(240, y, "G1", 80) +
          f'<line x1="320" y1="{y}" x2="350" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/>'
          + _bloque(350, y, "G2", 80) +
          f'<line x1="430" y1="{y}" x2="500" y2="{y}" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/><text x="486" y="{y-8}">Z</text>'
          f'<polyline points="465,{y} 465,{y+52} 180,{y+52} 180,{y+16}" fill="none" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)"/>'
          f'<text x="70" y="{y+82}" fill="{ACC}" font-weight="700" font-size="14">H1 = 1/G2 · H2 = G1 · H3 = G2  →  Z/X = (1/G2)·G1G2/(1 + G1G2) = G1/(1 + G1G2) ✓</text>')
    s += "</svg>"
    return fig(s, "Cuestión 8. Paso de realimentación no unitaria a unitaria: se saca 1/G2 delante del lazo y G2 pasa a la cadena directa. Las dos figuras tienen la misma función de transferencia Z/X.")


FIGURAS = {"c1": c1, "c2": c2, "c3": c3, "c4": c4, "c5": c5, "c6": c6, "c7": c7, "c8": c8}

CSS_FIG = """
figure.sol{margin:22px 0 28px;background:#fff;border:1px solid #C9D1DB;padding:14px}
figure.sol .svgwrap{overflow-x:auto}
figure.sol svg{display:block;width:100%;min-width:520px;height:auto}
figure.sol figcaption{font-size:14px;line-height:1.5;color:#4A5568;margin-top:8px}
"""
