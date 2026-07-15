# -*- coding: utf-8 -*-
"""Generador multi-idioma para Authentic CDMX.
1 plantilla + 1 diccionario por idioma -> genera index.html + en/ + fr/ + intl/.
Ejecutar: python build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

CSS = r"""
  :root {
    --rosa:#EC1E79; --rosa-deep:#B00D5A; --verde:#0E9C9C; --amarillo:#F4A62A;
    --ground:#FBF5F2; --card:#FFFFFF; --ink:#1B1013; --ink-soft:#5B4B50; --line:#EBD9D3;
    --shadow:22px 22px 0 rgba(236,30,121,.10);
    --serif:"Cormorant Garamond","Songti SC","Noto Serif CJK SC",Georgia,"Times New Roman",serif;
    --sans:"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",-apple-system,"Segoe UI",system-ui,sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    :root { --ground:#140609; --card:#1F1017; --ink:#FBEFF3; --ink-soft:#C7A7B3; --line:#38202A;
      --shadow:22px 22px 0 rgba(236,30,121,.22); --rosa:#FF4C97; --rosa-deep:#FF7FB4; }
  }
  :root[data-theme="dark"]{ --ground:#140609;--card:#1F1017;--ink:#FBEFF3;--ink-soft:#C7A7B3;--line:#38202A;--shadow:22px 22px 0 rgba(236,30,121,.22);--rosa:#FF4C97;--rosa-deep:#FF7FB4; }
  :root[data-theme="light"]{ --ground:#FBF5F2;--card:#FFFFFF;--ink:#1B1013;--ink-soft:#5B4B50;--line:#EBD9D3;--shadow:22px 22px 0 rgba(236,30,121,.10);--rosa:#EC1E79;--rosa-deep:#B00D5A; }
  *{box-sizing:border-box;} html{scroll-behavior:smooth;}
  @media (prefers-reduced-motion: reduce){ html{scroll-behavior:auto;} }
  body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);line-height:1.7;-webkit-font-smoothing:antialiased;}
  img{max-width:100%;display:block;}
  .wrap{max-width:1120px;margin:0 auto;padding:0 24px;}
  section{padding:92px 0;}
  .eyebrow{font-size:13px;letter-spacing:.28em;text-transform:uppercase;color:var(--rosa);font-weight:700;margin:0 0 14px;}
  h1,h2,h3{font-family:var(--serif);text-wrap:balance;font-weight:600;}
  .lede{max-width:62ch;color:var(--ink-soft);font-size:18px;}
  .bar{position:sticky;top:0;z-index:30;display:flex;align-items:center;justify-content:space-between;padding:14px 24px;background:color-mix(in srgb,var(--ground) 82%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);gap:16px;flex-wrap:wrap;}
  .brand{font-family:var(--serif);font-size:21px;font-weight:700;}
  .brand b{color:var(--rosa);}
  .nav{display:flex;gap:22px;font-size:14px;}
  .nav a{color:var(--ink-soft);text-decoration:none;}
  .nav a:hover{color:var(--rosa);}
  @media (max-width:900px){ .nav{display:none;} }
  .langs{display:flex;gap:10px;font-size:13px;font-weight:700;align-items:center;}
  .langs a{color:var(--ink-soft);text-decoration:none;padding:3px 6px;border-radius:6px;}
  .langs a.active{color:#fff;background:var(--rosa);}
  .langs a:hover{color:var(--rosa);}
  .langs a.active:hover{color:#fff;}
  .hero{position:relative;min-height:92vh;display:flex;align-items:flex-end;overflow:hidden;}
  .hero img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 40%;}
  .hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,3,6,.28) 0%,rgba(10,3,6,.15) 40%,rgba(10,3,6,.86) 100%);}
  .hero .inner{position:relative;z-index:2;padding:0 24px 72px;max-width:1120px;margin:0 auto;width:100%;}
  .hero .kicker{display:inline-block;background:var(--rosa);color:#fff;padding:6px 14px;border-radius:100px;font-size:12px;font-weight:800;letter-spacing:.16em;margin-bottom:20px;}
  .hero h1{font-size:clamp(46px,9vw,104px);line-height:.98;margin:0;color:#fff;}
  .hero h1 .es{font-style:italic;color:#FF7FB4;}
  .hero p.sub{font-size:20px;max-width:44ch;color:rgba(255,255,255,.86);margin:22px 0 32px;}
  .hero-cta{display:flex;gap:14px;flex-wrap:wrap;}
  .btn{display:inline-flex;align-items:center;gap:8px;cursor:pointer;padding:15px 28px;border-radius:100px;font-size:16px;font-weight:700;text-decoration:none;border:2px solid #fff;transition:transform .12s ease;}
  .btn:hover{transform:translateY(-2px);}
  .btn-primary{background:var(--rosa);border-color:var(--rosa);color:#fff;}
  .btn-ghost{background:transparent;color:#fff;}
  .btn:focus-visible{outline:3px solid var(--amarillo);outline-offset:3px;}
  .manifesto{background:var(--ink);color:var(--ground);text-align:center;}
  .manifesto .eyebrow{color:var(--amarillo);}
  .manifesto h2{font-size:clamp(30px,5.5vw,56px);line-height:1.06;margin:0 auto;max-width:22ch;color:var(--ground);}
  .manifesto h2 .hit{color:var(--rosa);font-style:italic;}
  .manifesto p{max-width:60ch;margin:26px auto 0;color:rgba(251,239,243,.72);font-size:18px;}
  .shead{display:flex;align-items:end;justify-content:space-between;gap:20px;margin-bottom:42px;}
  .shead h2{font-size:clamp(30px,5vw,48px);margin:0;line-height:1.04;}
  .shead .es-tag{font-family:var(--serif);font-style:italic;color:var(--rosa);font-size:20px;white-space:nowrap;}
  .gallery{columns:3 260px;column-gap:14px;}
  .gallery figure{margin:0 0 14px;break-inside:avoid;border-radius:12px;overflow:hidden;position:relative;}
  .gallery img{width:100%;transition:transform .4s ease;}
  .gallery figure:hover img{transform:scale(1.04);}
  .gallery figcaption{position:absolute;left:10px;bottom:8px;color:#fff;font-size:12px;font-weight:600;text-shadow:0 1px 8px rgba(0,0,0,.7);opacity:0;transition:opacity .25s;}
  .gallery figure:hover figcaption{opacity:1;}
  .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;}
  @media (max-width:820px){ .grid{grid-template-columns:1fr 1fr;} }
  @media (max-width:540px){ .grid{grid-template-columns:1fr;} }
  .card{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;}
  .card .thumb{aspect-ratio:4/5;overflow:hidden;}
  .card .thumb img{width:100%;height:100%;object-fit:cover;}
  .card .body{padding:18px 20px 22px;}
  .card h3{margin:0 0 4px;font-size:23px;}
  .card .zh-sub{color:var(--rosa);font-size:12px;font-weight:700;letter-spacing:.06em;}
  .card p{margin:10px 0 0;color:var(--ink-soft);font-size:15px;}
  .card.soft{border-color:var(--verde);}
  .card.soft .zh-sub{color:var(--verde);}
  .food{display:grid;grid-template-columns:1fr 1fr;gap:6px 40px;}
  @media (max-width:640px){ .food{grid-template-columns:1fr;} }
  .dish{display:flex;gap:16px;padding:16px 0;border-bottom:1px solid var(--line);}
  .dish .n{font-family:var(--serif);font-size:30px;color:var(--rosa);font-weight:700;min-width:44px;}
  .dish h4{margin:0;font-size:19px;font-family:var(--serif);}
  .dish .es{color:var(--verde);font-weight:700;font-size:13px;}
  .dish p{margin:6px 0 0;font-size:14px;color:var(--ink-soft);}
  .chili{color:var(--rosa-deep);font-weight:700;}
  .myth-band{background:var(--ink);color:var(--ground);}
  .myth-band .eyebrow{color:var(--amarillo);}
  .myth-band h2{color:var(--ground);}
  .myths{display:grid;grid-template-columns:1fr 1fr;gap:18px;}
  @media (max-width:720px){ .myths{grid-template-columns:1fr;} }
  .myth{border:1px solid rgba(255,255,255,.14);border-radius:16px;padding:24px;background:rgba(255,255,255,.03);}
  .myth .tag{font-size:12px;letter-spacing:.18em;text-transform:uppercase;font-weight:800;}
  .myth .tag.f{color:#ff6b6b;} .myth .tag.t{color:#4fd1a5;}
  .myth h4{margin:8px 0 6px;font-family:var(--serif);font-size:22px;color:var(--ground);}
  .myth p{margin:0;color:rgba(251,239,243,.75);font-size:15px;}
  .planos-band{background:color-mix(in srgb,var(--verde) 7%,var(--ground));}
  .planos{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;}
  @media (max-width:860px){ .planos{grid-template-columns:1fr 1fr;} }
  @media (max-width:460px){ .planos{grid-template-columns:1fr;} }
  .plano{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;text-align:center;}
  .plano .frame{background:color-mix(in srgb,var(--ink) 5%,var(--card));border-radius:12px;padding:10px;margin-bottom:14px;}
  .plano svg{width:100%;height:auto;display:block;}
  .plano .num{font-family:var(--serif);font-size:14px;font-weight:700;color:var(--rosa);letter-spacing:.1em;}
  .plano h4{margin:6px 0 2px;font-family:var(--serif);font-size:21px;}
  .plano .es{color:var(--verde);font-weight:700;font-size:12px;letter-spacing:.04em;display:block;margin-bottom:8px;}
  .plano p{margin:0;font-size:13px;color:var(--ink-soft);line-height:1.55;}
  .sil{fill:var(--rosa);} .scene{fill:color-mix(in srgb,var(--ink) 16%,transparent);}
  .bracket{fill:none;stroke:var(--ink);stroke-width:2.4;opacity:.5;}
  .confetti{fill:var(--amarillo);} .confetti.v{fill:var(--verde);}
  .packs{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
  @media (max-width:820px){ .packs{grid-template-columns:1fr;max-width:460px;margin:0 auto;} }
  .pack{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:30px 26px;display:flex;flex-direction:column;position:relative;}
  .pack.feat{border:2px solid var(--rosa);box-shadow:var(--shadow);}
  .pack.sold{opacity:.62;}
  .pack-badge{position:absolute;top:-13px;left:26px;font-size:12px;font-weight:800;padding:5px 14px;border-radius:100px;letter-spacing:.05em;}
  .pack-badge.low{background:var(--amarillo);color:#1B1013;}
  .pack-badge.sold{background:var(--ink-soft);color:#fff;}
  .pack h3{margin:0;font-size:26px;}
  .pack .price{font-family:var(--serif);font-size:44px;font-weight:700;margin:10px 0 2px;}
  .pack .price small{font-size:16px;color:var(--ink-soft);font-weight:400;}
  .pack .price .usd{font-size:15px;color:var(--verde);display:block;}
  .pack ul{list-style:none;padding:0;margin:18px 0 24px;display:grid;gap:10px;}
  .pack li{padding-left:26px;position:relative;font-size:15px;color:var(--ink-soft);}
  .pack li::before{content:"\2733";position:absolute;left:0;color:var(--rosa);}
  .pack .btn{justify-content:center;margin-top:auto;border-color:var(--ink);color:var(--ink);}
  .pack.feat .btn{background:var(--rosa);border-color:var(--rosa);color:#fff;}
  .pack .btn.disabled{background:transparent;border-color:var(--line);color:var(--ink-soft);cursor:not-allowed;pointer-events:none;}
  .contact{text-align:center;}
  .qr{width:244px;margin:26px auto 18px;border-radius:18px;background:#fff;border:2px solid var(--rosa);padding:12px;overflow:hidden;}
  .qr img{width:100%;border-radius:10px;}
  .handles{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:8px;}
  .chip{border:1px solid var(--line);border-radius:100px;padding:9px 18px;font-size:14px;font-weight:600;background:var(--card);text-decoration:none;color:var(--ink);}
  a.chip:hover{border-color:var(--rosa);}
  .chip b{color:var(--rosa);}
  footer{border-top:1px solid var(--line);padding:34px 0 60px;color:var(--ink-soft);font-size:13px;text-align:center;}
  .note{font-size:13px;color:var(--ink-soft);background:color-mix(in srgb,var(--amarillo) 14%,var(--ground));border-left:3px solid var(--amarillo);padding:12px 16px;border-radius:8px;margin-top:22px;}
"""

# 4 diagramas SVG (markup fijo, texto va aparte)
SVG = {
"wide": """<svg viewBox="0 0 160 200" role="img" aria-label="wide shot">
<rect class="scene" x="18" y="112" width="22" height="60" rx="2"/><rect class="scene" x="118" y="96" width="24" height="76" rx="2"/><rect class="scene" x="0" y="170" width="160" height="6"/>
<circle class="sil" cx="80" cy="72" r="8"/><rect class="sil" x="74" y="80" width="12" height="38" rx="5"/><rect class="sil" x="68" y="84" width="4" height="30" rx="2"/><rect class="sil" x="88" y="84" width="4" height="30" rx="2"/><rect class="sil" x="75" y="116" width="4" height="52" rx="2"/><rect class="sil" x="81" y="116" width="4" height="52" rx="2"/>
<path class="bracket" d="M6,22 L6,6 L22,6"/><path class="bracket" d="M138,6 L154,6 L154,22"/><path class="bracket" d="M6,178 L6,194 L22,194"/><path class="bracket" d="M138,194 L154,194 L154,178"/></svg>""",
"american": """<svg viewBox="0 0 160 200" role="img" aria-label="american shot">
<circle class="sil" cx="80" cy="50" r="16"/><rect class="sil" x="60" y="66" width="40" height="60" rx="14"/><rect class="sil" x="48" y="70" width="11" height="52" rx="5"/><rect class="sil" x="101" y="70" width="11" height="52" rx="5"/><rect class="sil" x="63" y="120" width="14" height="80" rx="6"/><rect class="sil" x="83" y="120" width="14" height="80" rx="6"/>
<path class="bracket" d="M6,22 L6,6 L22,6"/><path class="bracket" d="M138,6 L154,6 L154,22"/><path class="bracket" d="M6,178 L6,194 L22,194"/><path class="bracket" d="M138,194 L154,194 L154,178"/></svg>""",
"portrait": """<svg viewBox="0 0 160 200" role="img" aria-label="portrait">
<rect class="sil" x="26" y="150" width="108" height="60" rx="34"/><circle class="sil" cx="80" cy="82" r="40"/>
<path class="bracket" d="M6,22 L6,6 L22,6"/><path class="bracket" d="M138,6 L154,6 L154,22"/><path class="bracket" d="M6,178 L6,194 L22,194"/><path class="bracket" d="M138,194 L154,194 L154,178"/></svg>""",
"fun": """<svg viewBox="0 0 160 200" role="img" aria-label="candid">
<circle class="confetti" cx="26" cy="34" r="4"/><circle class="confetti v" cx="140" cy="46" r="4"/><circle class="confetti" cx="132" cy="150" r="4"/><circle class="confetti v" cx="30" cy="140" r="4"/>
<g transform="rotate(-9 80 100)"><circle class="sil" cx="80" cy="60" r="14"/><rect class="sil" x="67" y="74" width="26" height="46" rx="11"/><rect class="sil" x="46" y="48" width="9" height="34" rx="4" transform="rotate(-38 50 65)"/><rect class="sil" x="105" y="48" width="9" height="34" rx="4" transform="rotate(38 110 65)"/><rect class="sil" x="66" y="116" width="10" height="46" rx="5" transform="rotate(14 71 139)"/><rect class="sil" x="84" y="116" width="10" height="46" rx="5" transform="rotate(-14 89 139)"/></g>
<path class="bracket" d="M6,22 L6,6 L22,6"/><path class="bracket" d="M138,6 L154,6 L154,22"/><path class="bracket" d="M6,178 L6,194 L22,194"/><path class="bracket" d="M138,194 L154,194 L154,178"/></svg>""",
}

# idiomas y rutas
LANG_ORDER = ["zh", "en", "fr", "intl"]
LANG_PATH = {"zh": "/", "en": "/en/", "fr": "/fr/", "intl": "/intl/"}
LANG_LABEL = {"zh": "中文", "en": "EN·US", "fr": "FR", "intl": "EN·Intl"}
HREFLANG = {"zh": "zh", "en": "en-US", "fr": "fr", "intl": "en"}


def langbar(cur):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (LANG_PATH[l], ' class="active"' if l == cur else "", LANG_LABEL[l])
        for l in LANG_ORDER)
    return '<div class="langs">%s</div>' % links


def render(lang, C):
    nav = "".join('<a href="#%s">%s</a>' % (k, v) for k, v in C["nav"])
    gallery = "".join(
        '<figure><img src="/img/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>' % (img, cap, cap)
        for img, cap in C["gallery"])
    spots = "".join(
        '<div class="card%s"><div class="thumb"><img src="/img/%s" alt="%s" loading="lazy"></div><div class="body"><span class="zh-sub">%s</span><h3>%s</h3><p>%s</p></div></div>'
        % ((" soft" if soft else ""), img, h3, sub, h3, p)
        for img, sub, h3, p, soft in C["spots"])
    dishes = "".join(
        '<div class="dish"><div class="n">%02d</div><div><h4>%s <span class="es">%s</span></h4><p>%s</p></div></div>'
        % (i + 1, name, es, desc)
        for i, (name, es, desc) in enumerate(C["dishes"]))
    myths = "".join(
        '<div class="myth"><span class="tag %s">%s</span><h4>%s</h4><p>%s</p></div>'
        % (("f" if kind == "myth" else "t"), tag, h4, p)
        for kind, tag, h4, p in C["myths"])
    planos = "".join(
        '<div class="plano"><div class="frame">%s</div><span class="num">%02d</span><h4>%s</h4><span class="es">%s</span><p>%s</p></div>'
        % (SVG[key], i + 1, h4, es, p)
        for i, (key, h4, es, p) in enumerate(C["planos"]))
    packs = ""
    for pk in C["packs"]:
        cls = " " + pk["cls"] if pk["cls"] else ""
        badge = '<span class="pack-badge %s">%s</span>' % (pk["badge_cls"], pk["badge"]) if pk.get("badge") else ""
        feats = "".join("<li>%s</li>" % f for f in pk["features"])
        if pk.get("sold"):
            btn = '<span class="btn disabled" aria-disabled="true">%s</span>' % pk["btn"]
        else:
            btn = '<a href="#contacto" class="btn">%s</a>' % pk["btn"]
        packs += '<div class="pack%s">%s<h3>%s</h3><div class="price">%s<small>%s</small><span class="usd">%s</span></div><ul>%s</ul>%s</div>' % (
            cls, badge, pk["name"], pk["price"], pk["unit"], pk["ref"], feats, btn)

    alts = "".join(
        '<link rel="alternate" hreflang="%s" href="https://authentic-cdmx.com%s">' % (HREFLANG[l], LANG_PATH[l])
        for l in LANG_ORDER)
    alts += '<link rel="alternate" hreflang="x-default" href="https://authentic-cdmx.com/">'

    html = """<!doctype html>
<html lang="%(htmllang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
%(alts)s
<style>%(css)s</style>
</head>
<body>
<div class="bar">
  <div class="brand">Authentic <b>CDMX</b></div>
  <nav class="nav">%(nav)s</nav>
  %(langbar)s
</div>
<header class="hero">
  <img class="bg" src="/img/hero-street.jpg" alt="Ciudad de México">
  <div class="inner">
    <span class="kicker">%(kicker)s</span>
    <h1>%(h1)s</h1>
    <p class="sub">%(sub)s</p>
    <div class="hero-cta">
      <a href="#foto" class="btn btn-primary">%(cta1)s</a>
      <a href="#trabajo" class="btn btn-ghost">%(cta2)s</a>
    </div>
  </div>
</header>
<section class="manifesto"><div class="wrap">
  <p class="eyebrow">%(man_eyebrow)s</p>
  <h2>%(man_h2)s</h2>
  <p>%(man_p)s</p>
</div></section>
<section id="trabajo"><div class="wrap">
  <p class="eyebrow">%(port_eyebrow)s</p>
  <div class="shead"><h2>%(port_h2)s</h2><span class="es-tag">%(port_tag)s</span></div>
  <div class="gallery">%(gallery)s</div>
</div></section>
<section id="lugares" style="background:color-mix(in srgb,var(--rosa) 5%%,var(--ground));"><div class="wrap">
  <p class="eyebrow">%(spot_eyebrow)s</p>
  <div class="shead"><h2>%(spot_h2)s</h2><span class="es-tag">%(spot_tag)s</span></div>
  <div class="grid">%(spots)s</div>
  <p class="note">%(spot_note)s</p>
</div></section>
<section id="comida"><div class="wrap">
  <p class="eyebrow">%(food_eyebrow)s</p>
  <div class="shead"><h2>%(food_h2)s</h2><span class="es-tag">%(food_tag)s</span></div>
  <div class="food">%(dishes)s</div>
</div></section>
<section id="mitos" class="myth-band"><div class="wrap">
  <p class="eyebrow">%(myth_eyebrow)s</p>
  <div class="shead"><h2 style="color:var(--ground)">%(myth_h2)s</h2></div>
  <div class="myths">%(myths)s</div>
</div></section>
<section id="foto"><div class="wrap">
  <p class="eyebrow">%(pack_eyebrow)s</p>
  <div class="shead"><h2>%(pack_h2)s</h2><span class="es-tag">%(pack_tag)s</span></div>
  <div class="packs">%(packs)s</div>
  <p class="note">%(pack_note)s</p>
</div></section>
<section id="planos" class="planos-band"><div class="wrap">
  <p class="eyebrow">%(plano_eyebrow)s</p>
  <div class="shead"><h2>%(plano_h2)s</h2><span class="es-tag">%(plano_tag)s</span></div>
  <p class="lede" style="margin:-24px 0 34px;">%(plano_lede)s</p>
  <div class="planos">%(planos)s</div>
</div></section>
<section id="contacto" class="contact"><div class="wrap">
  <p class="eyebrow">%(con_eyebrow)s</p>
  <div class="shead" style="justify-content:center;"><h2>%(con_h2)s</h2></div>
  <div class="qr"><img src="/img/wechat-qr.jpg" alt="WeChat QR"></div>
  <div class="handles">
    <span class="chip">%(con_wechat)s <b>QR &#8593;</b></span>
    <a class="chip" href="https://instagram.com/rod0cv" target="_blank" rel="noopener">Instagram <b>@rod0cv</b></a>
    <a class="chip" href="mailto:authenticcdmx@gmail.com">Email <b>authenticcdmx@gmail.com</b></a>
  </div>
  <p class="lede" style="margin:24px auto 0;">%(con_lede)s</p>
</div></section>
<footer>%(footer)s</footer>
</body>
</html>
""" % dict(
        htmllang=C["htmllang"], title=C["title"], desc=C["desc"], alts=alts, css=CSS,
        nav=nav, langbar=langbar(lang), kicker=C["kicker"], h1=C["h1"], sub=C["sub"],
        cta1=C["cta1"], cta2=C["cta2"], man_eyebrow=C["man_eyebrow"], man_h2=C["man_h2"], man_p=C["man_p"],
        port_eyebrow=C["port_eyebrow"], port_h2=C["port_h2"], port_tag=C["port_tag"], gallery=gallery,
        spot_eyebrow=C["spot_eyebrow"], spot_h2=C["spot_h2"], spot_tag=C["spot_tag"], spots=spots, spot_note=C["spot_note"],
        food_eyebrow=C["food_eyebrow"], food_h2=C["food_h2"], food_tag=C["food_tag"], dishes=dishes,
        myth_eyebrow=C["myth_eyebrow"], myth_h2=C["myth_h2"], myths=myths,
        pack_eyebrow=C["pack_eyebrow"], pack_h2=C["pack_h2"], pack_tag=C["pack_tag"], packs=packs, pack_note=C["pack_note"],
        plano_eyebrow=C["plano_eyebrow"], plano_h2=C["plano_h2"], plano_tag=C["plano_tag"], plano_lede=C["plano_lede"], planos=planos,
        con_eyebrow=C["con_eyebrow"], con_h2=C["con_h2"], con_wechat=C["con_wechat"], con_lede=C["con_lede"],
        footer=C["footer"],
    )
    return html


# ----------------- CONTENIDO POR IDIOMA -----------------
GAL = lambda caps: list(zip(
    ["portrait-red.jpg","angel-bw.jpg","skyline-sunset.jpg","doorway.jpg","vocho.jpg","mural-wings.jpg",
     "intersection.jpg","revolucion.jpg","oxxo.jpg","red-car.jpg","mural-dragon.jpg","moto.jpg"], caps))

LANGS = {}

LANGS["zh"] = {
 "htmllang":"zh","title":"Authentic CDMX · 真实的墨西哥城旅拍",
 "desc":"本地摄影师带你拍真实的墨西哥城 — 不是明信片，是这座城市真正的样子。周末约拍 + 向导。",
 "nav":[("trabajo","作品"),("lugares","带你去哪"),("comida","吃什么"),("mitos","谣言粉碎"),("foto","约拍"),("planos","景别"),("contacto","联系")],
 "kicker":"CIUDAD DE MÉXICO · 真实版","h1":"真实的<br><span class=\"es\">墨西哥城</span>",
 "sub":"本地摄影师带你拍这座城市真正的样子 —— 不是明信片。周末约拍 + 向导，英语 / 西语沟通。",
 "cta1":"约拍套餐 →","cta2":"看作品",
 "man_eyebrow":"Manifiesto · 我的原则",
 "man_h2":"Roma、Condesa 值得去 —— 但那是<span class=\"hit\">全世界都知道的秘密</span>。我还带你去别人拍不到的地方。",
 "man_p":"Roma、Condesa 又潮又安全、对外国人超友好，想去我们就去，值得。但那些咖啡馆谁都拍过一百遍了。我更想带你去夜里的中央大道、老唐人街、街头霓虹和市场 —— 有故事、有光、别人朋友圈里没有的照片。两种都要？完美。",
 "port_eyebrow":"Portafolio · 我的作品","port_h2":"这座城市，<br>我镜头里的样子","port_tag":"Todo shot in CDMX",
 "gallery":GAL(["Retrato · 街头人像","Ángel de la Independencia","Reforma · 日落","殖民老门廊","Vocho · 甲壳虫","Mural · 翅膀壁画","夜 · 城市路口","Monumento a la Revolución","街角日常","Neón · 霓虹","Mural · 龙","Movimiento · 动态"]),
 "spot_eyebrow":"Dónde te llevo · 带你去哪","spot_h2":"真实、上镜、<br>游客不知道的地方","spot_tag":"Lugares con alma",
 "spots":[
   ("torre-night.jpg","CENTRO DE NOCHE","夜晚的历史中心","白天游客多，夜里才有魔力。Torre Latino、空荡的大道、暖黄路灯。出片率最高的时段。",False),
   ("barrio-chino.jpg","BARRIO CHINO","老唐人街 Dolores 街","红灯笼、烟火气的窄巷。对你来说亲切又有反差 —— 墨西哥味的中国街，拍出来很有意思。",False),
   ("oxxo.jpg","CALLE · MERCADO","街头 & 市场","小卖部、水果摊、涂鸦墙。真正的城市日常，随手一拍就是故事，比景点真实一百倍。",False),
   ("reforma-dusk.jpg","ROMA · CONDESA","罗马 & 康德萨区","公开的秘密 —— 又潮又安全、最 foreign-friendly，咖啡馆和涂鸦墙确实好看。想拍网红风就来，但别只拍这里。",True),
   ("vocho.jpg","ICONOS · 城市符号","甲壳虫 & 城市符号","老 Vocho、棕榈树、复古招牌。这些细节才是墨西哥城的灵魂，明信片上没有。",False),
   ("skyline-sunset.jpg","ROOFTOP · 天台日落","天台看日落","想要大片天际线？我知道几个能上去的天台，日落 golden hour 一组，绝了。",False)],
 "spot_note":"🗺️ 想去金字塔（Teotihuacán）、霍奇米尔科、Roma/Condesa 打卡？都能安排。但想要别人没有的照片 —— 上面那些冷门点才是重点。",
 "food_eyebrow":"Qué comer · 吃什么","food_h2":"墨西哥必吃 &<br>中餐去哪里","food_tag":"Sabores",
 "dishes":[
   ("Tacos al pastor","牧羊人塔可","竖烤猪肉 + 菠萝，玉米饼卷着吃。<span class=\"chili\">微辣，可说「sin picante」不辣。</span>"),
   ("Birria","红烧羊肉汤 taco","慢炖羊/牛肉，蘸汤吃。中国胃很容易接受，我带你去本地人排队的摊。"),
   ("Mole","莫雷酱","巧克力+辣椒+香料的酱，浇在鸡肉上。味道复杂，普埃布拉名菜。"),
   ("Elote / Esquite","墨西哥烤玉米","玉米抹蛋黄酱、芝士粉、辣椒粉、青柠。街头小吃之王。"),
   ("Barrio Chino","唐人街","<span class=\"chili\">先说清楚：这里的「中餐」是墨西哥化的，别期待家乡味。</span>但拍照氛围很好。"),
   ("正宗中餐","Auténtico","想吃地道川菜/粤菜？我带你去本地华人真正吃的馆子，不踩雷。")],
 "myth_eyebrow":"Mitos y verdades · 谣言粉碎机","myth_h2":"来之前你担心的，<br>其实是这样",
 "myths":[
   ("myth","谣言 MITO","「墨西哥城超级危险」","真相：旅游区白天很安全。晚上用 Uber、别露富，跟任何大城市一样。有本地人带更放心 —— 我知道哪条街该走、哪条不该。"),
   ("myth","谣言 MITO","「所有东西都超辣」","真相：辣椒酱是分开放的，你可以完全不加。会说「sin chile」就行。"),
   ("truth","真相 VERDAD","自来水不要直接喝","喝瓶装水 agua embotellada。餐厅冰块通常是净化水，正常吃没问题。"),
   ("truth","真相 VERDAD","要给小费 propina","餐厅 10–15%。Uber、Google 翻译好用；但微信/支付宝几乎不收，备好现金和一张 Visa。"),
   ("truth","真相 VERDAD","海拔 2240 米","墨西哥城在高原，走快会喘、少数人轻微高反。第一天别排太满，多喝水。"),
   ("myth","谣言 MITO","「语言完全不通」","真相：旅游区能用基础英语。有我在，英语 / 西语全程沟通，点菜、打车、砍价都不用你操心。")],
 "pack_eyebrow":"约拍套餐 · Paquetes","pack_h2":"周末约拍<br>向导 + 摄影 一次搞定","pack_tag":"Fotógrafo local",
 "packs":[
   {"cls":"","badge":None,"badge_cls":"","name":"City Walk","price":"$120","unit":"/2小时","ref":"≈ 700 元","features":["一个地点","精修 25 张","向导 + 拍摄","3 天内交付"],"btn":"预约","sold":False},
   {"cls":"feat","badge":"名额紧张 · Low availability","badge_cls":"low","name":"Half Day","price":"$220","unit":"/4小时","ref":"≈ 1300 元","features":["2–3 个地点，含隐藏机位","精修 60 张","向导 + 摄影 + 路线规划","协助打车、点餐","2 天内交付"],"btn":"立即预约 →","sold":False},
   {"cls":"sold","badge":"已订满 · SOLD OUT","badge_cls":"sold","name":"Full Day","price":"$320","unit":"/整天","ref":"≈ 1900 元","features":["全天旅拍（含金字塔可选）","精修 100 张","用车协调","日出 / 天台机位"],"btn":"已订满 Sold out","sold":True}],
 "pack_note":"💵 价格为示意，请换成你真实报价。付款方式建议写清楚（现金 / 转账 / 刷卡）。",
 "plano_eyebrow":"Tipo de plano · 你想要什么景别","plano_h2":"预约前告诉我<br>你想要哪种照片","plano_tag":"Elige tu encuadre",
 "plano_lede":"加微信时，说一句「我想要 1 号 / 2 号…」就行。不确定也没关系 —— 到现场我帮你决定，重点是玩得开心。",
 "planos":[
   ("wide","全身 + 背景","Plano general · Wide","人小、景大。适合地标、街道、天际线 —— 你和这座城市一起入镜。"),
   ("american","七分身","Plano americano","大腿以上入镜。经典时尚感，既看得到你的穿搭，也带一点环境。"),
   ("portrait","人像特写","Retrato · Portrait","头肩为主，背景虚化。突出表情和情绪，最适合当头像、当封面。"),
   ("fun","随意抓拍","Libre · Just have fun","跳起来、走起来、笑出来。抓拍最自然的瞬间，往往是最好看的照片。")],
 "con_eyebrow":"Contacto · 联系我","con_h2":"加微信，聊聊你的<br>墨西哥城行程","con_wechat":"微信 WeChat",
 "con_lede":"告诉我你的日期、想去的地方、几个人 —— 我给你定制路线和报价。周末档期有限，建议提前一周约。",
 "footer":"Authentic CDMX · 墨西哥城本地摄影 &amp; 向导 · Ciudad de México<br>© 2026 · Todas las fotos por Rodo",
}

# ---------- EN (US) ----------
LANGS["en"] = {
 "htmllang":"en","title":"Authentic CDMX · Real Mexico City Photo Sessions",
 "desc":"A local photographer takes you to shoot the real Mexico City — not the postcard. Weekend photo sessions + guide.",
 "nav":[("trabajo","Work"),("lugares","Where"),("comida","Eat"),("mitos","Myths"),("foto","Book"),("planos","Framing"),("contacto","Contact")],
 "kicker":"MEXICO CITY · THE REAL ONE","h1":"The real<br><span class=\"es\">Mexico City</span>",
 "sub":"A local photographer takes you to shoot the city as it actually is — not the postcard. Weekend sessions + guide. We speak English & Spanish.",
 "cta1":"See packages →","cta2":"View work",
 "man_eyebrow":"Manifesto · How I work",
 "man_h2":"Roma & Condesa are worth it — but they're the <span class=\"hit\">worst-kept secret</span> in town. I'll also take you where nobody else shoots.",
 "man_p":"Roma & Condesa are cool, safe and super foreign-friendly — if you want them, we'll go, they're worth it. But those cafés have been shot a thousand times. I'd rather take you to the avenues at night, the old Chinatown, street neon and markets — real light, real stories, photos nobody else has. Want both? Perfect.",
 "port_eyebrow":"Portfolio · My work","port_h2":"This city,<br>through my lens","port_tag":"All shot in CDMX",
 "gallery":GAL(["Portrait · street","Ángel de la Independencia","Reforma · sunset","Colonial doorway","Vocho · VW Beetle","Mural · wings","Night · intersection","Monumento a la Revolución","Corner store life","Neón · neon","Mural · dragon","Movimiento · motion"]),
 "spot_eyebrow":"Where I take you","spot_h2":"Real, photogenic,<br>off the tourist map","spot_tag":"Lugares con alma",
 "spots":[
   ("torre-night.jpg","CENTRO AT NIGHT","Downtown after dark","Crowded by day, magic at night. Torre Latino, empty avenues, warm street light. The highest hit-rate window there is.",False),
   ("barrio-chino.jpg","BARRIO CHINO","Old Chinatown · Dolores St.","Red lanterns, a narrow buzzing alley. Small but full of character — a great contrast backdrop.",False),
   ("oxxo.jpg","CALLE · MERCADO","Streets & markets","Corner stores, fruit stands, graffiti walls. Real daily life — one frame and you've got a story, a hundred times more real than a landmark.",False),
   ("reforma-dusk.jpg","ROMA · CONDESA","Roma & Condesa","The worst-kept secret — trendy, safe, the most foreign-friendly. Cafés and murals really do look good. Come for the IG shot, just don't stop there.",True),
   ("vocho.jpg","ICONOS · city symbols","Vochos & city icons","Old VW Beetles, palm trees, retro signage. The details are the soul of this city — never on a postcard.",False),
   ("skyline-sunset.jpg","ROOFTOP · sunset","Rooftop golden hour","Want the big skyline? I know a few rooftops you can actually get onto. One golden-hour set and it's a wrap.",False)],
 "spot_note":"🗺️ Want Teotihuacán pyramids, Xochimilco, or the Roma/Condesa checklist? All doable. But if you want photos nobody else has, the off-map spots above are the point.",
 "food_eyebrow":"What to eat","food_h2":"Must-eat Mexican &<br>where to find real Chinese","food_tag":"Sabores",
 "dishes":[
   ("Tacos al pastor","spit-roast pork","Marinated pork + pineapple in a corn tortilla. <span class=\"chili\">Mild — say “sin picante” for no heat.</span>"),
   ("Birria","stewed meat + broth","Slow-cooked goat/beef taco you dip in broth. Easy on any palate — I'll take you to the stall locals line up for."),
   ("Mole","chili-chocolate sauce","Chili + chocolate + spices over chicken. Complex, iconic Puebla dish."),
   ("Elote / Esquite","Mexican street corn","Corn with mayo, cheese, chili powder, lime. King of street snacks."),
   ("Barrio Chino","Chinatown","<span class=\"chili\">Heads up: the “Chinese” food here is Mexican-ized — don't expect the real thing.</span> Great photo vibe though."),
   ("Real Chinese","Auténtico","Craving proper Sichuan/Cantonese? I'll take you where the local Chinese community actually eats.")],
 "myth_eyebrow":"Myths & truths","myth_h2":"What you're worried about<br>before coming — the truth",
 "myths":[
   ("myth","MYTH","“Mexico City is super dangerous”","Truth: tourist areas are fine by day. At night use Uber, don't flash valuables — same as any big city. Safer with a local — I know which streets to take and which to skip."),
   ("myth","MYTH","“Everything is spicy”","Truth: the salsa is on the side. You control it. Just say “no spicy / sin chile.”"),
   ("truth","TRUE","Don't drink the tap water","Stick to bottled water. Restaurant ice is usually purified — you'll be fine eating out."),
   ("truth","TRUE","Tipping is expected","10–15% at restaurants. Uber and Google Translate work great. Bring some cash + a Visa card."),
   ("truth","TRUE","Altitude: 7,350 ft (2,240 m)","The city sits high. You may get slightly winded walking fast. Don't over-pack day one, drink water."),
   ("myth","MYTH","“Nobody speaks my language”","Truth: basic English works in tourist zones. With me it's fully English/Spanish — ordering, taxis, haggling all handled.")],
 "pack_eyebrow":"Packages · Paquetes","pack_h2":"Weekend sessions<br>guide + photographer in one","pack_tag":"Fotógrafo local",
 "packs":[
   {"cls":"","badge":None,"badge_cls":"","name":"City Walk","price":"$120","unit":"/2 hrs","ref":"USD","features":["One location","25 edited photos","Guide + shoot","Delivered in 3 days"],"btn":"Book","sold":False},
   {"cls":"feat","badge":"Low availability","badge_cls":"low","name":"Half Day","price":"$220","unit":"/4 hrs","ref":"USD","features":["2–3 locations, hidden spots","60 edited photos","Guide + shoot + route planning","Help with taxis & ordering","Delivered in 2 days"],"btn":"Book now →","sold":False},
   {"cls":"sold","badge":"SOLD OUT","badge_cls":"sold","name":"Full Day","price":"$320","unit":"/full day","ref":"USD","features":["Full-day shoot (pyramids optional)","100 edited photos","Transport coordination","Sunrise / rooftop spots"],"btn":"Sold out","sold":True}],
 "pack_note":"💵 Prices shown are placeholders — swap in your real rates. State payment methods clearly (cash / transfer / card).",
 "plano_eyebrow":"Type of shot","plano_h2":"Before we book,<br>tell me the look you want","plano_tag":"Pick your framing",
 "plano_lede":"When you message me, just say “I want #1 / #2…”. Not sure? No stress — I'll call it on location. The point is to have fun.",
 "planos":[
   ("wide","Full body + scene","Plano general · Wide","Small figure, big scene. For landmarks, streets, skylines — you and the city in one frame."),
   ("american","Knees-up","Plano americano","Framed from mid-thigh up. Classic editorial look — shows your outfit plus a bit of the place."),
   ("portrait","Close portrait","Retrato · Portrait","Head and shoulders, background blurred. Emotion-forward — perfect for a profile pic or cover."),
   ("fun","Candid","Libre · Just have fun","Jump, walk, laugh. Candid moments are usually the best-looking shots.")],
 "con_eyebrow":"Contact","con_h2":"Message me — let's plan<br>your Mexico City shoot","con_wechat":"WeChat",
 "con_lede":"Tell me your dates, where you want to go, and how many people — I'll build a custom route and quote. Weekend slots are limited, book about a week ahead.",
 "footer":"Authentic CDMX · Local photography &amp; guide · Ciudad de México<br>© 2026 · All photos by Rodo",
}

# ---------- FR ----------
LANGS["fr"] = dict(LANGS["en"])  # base EN, override textos
LANGS["fr"].update({
 "htmllang":"fr","title":"Authentic CDMX · Séances photo dans le vrai Mexico",
 "desc":"Un photographe local vous emmène photographier le vrai Mexico — pas la carte postale. Séances le week-end + guide.",
 "nav":[("trabajo","Photos"),("lugares","Où"),("comida","Manger"),("mitos","Mythes"),("foto","Réserver"),("planos","Cadrage"),("contacto","Contact")],
 "kicker":"MEXICO · LE VRAI","h1":"Le vrai<br><span class=\"es\">Mexico</span>",
 "sub":"Un photographe local vous emmène photographier la ville telle qu'elle est vraiment — pas la carte postale. Séances le week-end + guide. On parle anglais & espagnol.",
 "cta1":"Voir les formules →","cta2":"Voir les photos",
 "man_eyebrow":"Manifeste · Ma façon de travailler",
 "man_h2":"Roma et Condesa valent le détour — mais c'est <span class=\"hit\">le secret le moins bien gardé</span> de la ville. Je vous emmène aussi là où personne ne photographie.",
 "man_p":"Roma et Condesa sont branchés, sûrs et très accueillants pour les étrangers — si vous voulez, on y va, ça vaut le coup. Mais ces cafés ont été photographiés mille fois. Je préfère vous emmener sur les avenues la nuit, dans le vieux quartier chinois, dans les néons de rue et les marchés — vraie lumière, vraies histoires, des photos que personne d'autre n'a. Les deux ? Parfait.",
 "port_eyebrow":"Portfolio · Mon travail","port_h2":"Cette ville,<br>à travers mon objectif","port_tag":"Tout pris à CDMX",
 "gallery":GAL(["Portrait · rue","Ángel de la Independencia","Reforma · coucher de soleil","Porche colonial","Vocho · Coccinelle VW","Mural · ailes","Nuit · carrefour","Monumento a la Revolución","Vie de quartier","Neón · néon","Mural · dragon","Movimiento · mouvement"]),
 "spot_eyebrow":"Où je vous emmène","spot_h2":"Vrai, photogénique,<br>hors des sentiers touristiques","spot_tag":"Lugares con alma",
 "spots":[
   ("torre-night.jpg","CENTRO LA NUIT","Le centre après la tombée de la nuit","Bondé le jour, magique la nuit. Torre Latino, avenues désertes, lumière chaude. Le meilleur créneau pour de belles photos.",False),
   ("barrio-chino.jpg","BARRIO CHINO","Vieux quartier chinois · rue Dolores","Lanternes rouges, ruelle étroite et animée. Petit mais plein de caractère — un superbe décor de contraste.",False),
   ("oxxo.jpg","CALLE · MERCADO","Rues & marchés","Épiceries de coin, étals de fruits, murs de graffitis. La vraie vie quotidienne — une image et vous avez une histoire, cent fois plus vraie qu'un monument.",False),
   ("reforma-dusk.jpg","ROMA · CONDESA","Roma & Condesa","Le secret le moins bien gardé — branché, sûr, le plus accueillant pour les étrangers. Cafés et fresques sont vraiment beaux. Venez pour la photo Insta, mais ne vous arrêtez pas là.",True),
   ("vocho.jpg","ICONOS · symboles","Vochos & symboles de la ville","Vieilles Coccinelles VW, palmiers, enseignes rétro. Les détails sont l'âme de cette ville — jamais sur une carte postale.",False),
   ("skyline-sunset.jpg","ROOFTOP · coucher de soleil","Toits à l'heure dorée","Envie du grand panorama urbain ? Je connais des toits accessibles. Une série à l'heure dorée et c'est plié.",False)],
 "spot_note":"🗺️ Envie des pyramides de Teotihuacán, de Xochimilco ou de la checklist Roma/Condesa ? Tout est possible. Mais pour des photos que personne d'autre n'a, les lieux hors des sentiers ci-dessus sont l'essentiel.",
 "food_eyebrow":"Quoi manger","food_h2":"Mexicain incontournable &<br>où trouver du vrai chinois","food_tag":"Sabores",
 "dishes":[
   ("Tacos al pastor","porc rôti à la broche","Porc mariné + ananas dans une tortilla de maïs. <span class=\"chili\">Doux — dites « sin picante » pour zéro piquant.</span>"),
   ("Birria","viande mijotée + bouillon","Taco de chèvre/bœuf mijoté qu'on trempe dans le bouillon. Facile pour tous — je vous emmène au stand où les locaux font la queue."),
   ("Mole","sauce piment-chocolat","Piment + chocolat + épices sur du poulet. Complexe, plat emblématique de Puebla."),
   ("Elote / Esquite","maïs de rue mexicain","Maïs avec mayo, fromage, piment en poudre, citron vert. Le roi du snack de rue."),
   ("Barrio Chino","quartier chinois","<span class=\"chili\">Attention : la cuisine « chinoise » ici est mexicanisée — n'attendez pas l'authentique.</span> Mais l'ambiance photo est top."),
   ("Vrai chinois","Auténtico","Envie de vrai sichuanais/cantonais ? Je vous emmène là où la communauté chinoise locale mange vraiment.")],
 "myth_eyebrow":"Mythes & vérités","myth_h2":"Ce qui vous inquiète<br>avant de venir — la vérité",
 "myths":[
   ("myth","MYTHE","« Mexico est ultra dangereux »","Vérité : les zones touristiques sont sûres de jour. Le soir, Uber, ne pas exhiber d'objets de valeur — comme dans toute grande ville. Plus tranquille avec un local — je sais quelles rues prendre et lesquelles éviter."),
   ("myth","MYTHE","« Tout est piquant »","Vérité : la sauce est à part. Vous dosez. Dites simplement « no spicy / sin chile »."),
   ("truth","VRAI","Ne buvez pas l'eau du robinet","De l'eau en bouteille. Les glaçons au restaurant sont en général purifiés — pas de souci pour manger dehors."),
   ("truth","VRAI","Le pourboire est attendu","10–15 % au restaurant. Uber et Google Traduction marchent très bien. Prévoyez du liquide + une carte Visa."),
   ("truth","VRAI","Altitude : 2 240 m","La ville est en altitude. Vous serez peut-être vite essoufflé. Ne surchargez pas le premier jour, buvez de l'eau."),
   ("myth","MYTHE","« Personne ne parle ma langue »","Vérité : l'anglais de base passe dans les zones touristiques. Avec moi, tout se fait en anglais/espagnol — commandes, taxis, négociation, je gère.")],
 "pack_eyebrow":"Formules · Paquetes","pack_h2":"Séances le week-end<br>guide + photographe en un","pack_tag":"Fotógrafo local",
 "packs":[
   {"cls":"","badge":None,"badge_cls":"","name":"City Walk","price":"$120","unit":"/2 h","ref":"USD","features":["Un lieu","25 photos retouchées","Guide + prise de vue","Livraison en 3 jours"],"btn":"Réserver","sold":False},
   {"cls":"feat","badge":"Peu de dispo","badge_cls":"low","name":"Half Day","price":"$220","unit":"/4 h","ref":"USD","features":["2–3 lieux, spots cachés","60 photos retouchées","Guide + prise de vue + itinéraire","Aide taxis & commandes","Livraison en 2 jours"],"btn":"Réserver →","sold":False},
   {"cls":"sold","badge":"COMPLET","badge_cls":"sold","name":"Full Day","price":"$320","unit":"/journée","ref":"USD","features":["Séance journée (pyramides en option)","100 photos retouchées","Coordination transport","Spots lever du soleil / toits"],"btn":"Complet","sold":True}],
 "pack_note":"💵 Prix indicatifs — mettez vos vrais tarifs. Indiquez clairement les moyens de paiement (espèces / virement / carte).",
 "plano_eyebrow":"Type de plan","plano_h2":"Avant de réserver,<br>dites-moi le rendu voulu","plano_tag":"Choisissez votre cadrage",
 "plano_lede":"Quand vous m'écrivez, dites juste « je veux le n°1 / n°2… ». Pas sûr ? Aucun souci — je décide sur place. L'important, c'est de s'amuser.",
 "planos":[
   ("wide","Plein pied + décor","Plano general · Wide","Silhouette petite, décor grand. Pour monuments, rues, panoramas — vous et la ville dans un même cadre."),
   ("american","Plan américain","Plano americano","Cadré à mi-cuisse. Look éditorial classique — on voit votre tenue et un peu du lieu."),
   ("portrait","Portrait serré","Retrato · Portrait","Tête et épaules, arrière-plan flou. Centré sur l'émotion — parfait pour une photo de profil ou une couverture."),
   ("fun","Sur le vif","Libre · Just have fun","Sautez, marchez, riez. Les instants pris sur le vif sont souvent les plus réussis.")],
 "con_eyebrow":"Contact","con_h2":"Écrivez-moi — planifions<br>votre séance à Mexico","con_wechat":"WeChat",
 "con_lede":"Dites-moi vos dates, où vous voulez aller et combien vous êtes — je construis un itinéraire et un devis sur mesure. Les créneaux du week-end sont limités, réservez environ une semaine à l'avance.",
 "footer":"Authentic CDMX · Photographie &amp; guide local · Ciudad de México<br>© 2026 · Toutes les photos par Rodo",
})

# ---------- INTL (English, neutral/global) ----------
LANGS["intl"] = dict(LANGS["en"])
LANGS["intl"].update({
 "htmllang":"en","title":"Authentic CDMX · Real Mexico City Photo Sessions",
 "kicker":"MEXICO CITY · THE REAL ONE",
 "sub":"A local photographer takes you to shoot the city as it actually is — not the postcard. Weekend sessions + guide. English & Spanish, travellers welcome from anywhere.",
 "myths":[
   ("myth","MYTH","“Mexico City is super dangerous”","Truth: tourist areas are fine by day. At night use Uber, don't flash valuables — same as any big city. Safer with a local — I know which streets to take and which to skip."),
   ("myth","MYTH","“Everything is spicy”","Truth: the salsa is on the side. You control it. Just say “no spicy / sin chile.”"),
   ("truth","TRUE","Don't drink the tap water","Stick to bottled water. Restaurant ice is usually purified — you'll be fine eating out."),
   ("truth","TRUE","Tipping is expected","10–15% at restaurants. Uber and Google Translate work great. Bring some cash + a Visa/Mastercard."),
   ("truth","TRUE","Altitude: 2,240 m (7,350 ft)","The city sits high. You may get slightly winded walking fast. Don't over-pack day one, drink water."),
   ("myth","MYTH","“Nobody speaks my language”","Truth: basic English works in tourist zones. With me it's fully English/Spanish — ordering, taxis, haggling all handled.")],
})

if __name__ == "__main__":
    targets = {"zh": ROOT, "en": os.path.join(ROOT, "en"), "fr": os.path.join(ROOT, "fr"), "intl": os.path.join(ROOT, "intl")}
    for lang, path in targets.items():
        os.makedirs(path, exist_ok=True)
        html = render(lang, LANGS[lang])
        with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", lang, "->", os.path.join(path, "index.html"), len(html), "bytes")
