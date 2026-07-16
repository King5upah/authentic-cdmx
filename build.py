# -*- coding: utf-8 -*-
"""Generador multi-idioma para Authentic CDMX.
1 plantilla + 1 diccionario por idioma -> genera index.html + en/ + fr/ + intl/.
Ejecutar: python build.py
"""
import os
import re
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://authentic-cdmx.com"
OG_IMG = SITE + "/img/og-image.jpg"
OG_LOCALE = {"zh": "zh_CN", "ja": "ja_JP", "en": "en_US", "fr": "fr_FR", "intl": "en_US"}


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").strip()

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
  .manifesto{background:#180B10;color:#FBEFF3;text-align:center;}
  .manifesto .eyebrow{color:var(--amarillo);}
  .manifesto h2{font-size:clamp(30px,5.5vw,56px);line-height:1.06;margin:0 auto;max-width:22ch;color:#FBEFF3;}
  .manifesto h2 .hit{color:var(--rosa);font-style:italic;}
  .manifesto p{max-width:60ch;margin:26px auto 0;color:rgba(251,239,243,.72);font-size:18px;}
  .shead{display:flex;align-items:end;justify-content:space-between;gap:20px;margin-bottom:42px;}
  .shead h2{font-size:clamp(30px,5vw,48px);margin:0;line-height:1.04;}
  .shead .es-tag{font-family:var(--serif);font-style:italic;color:var(--rosa);font-size:20px;white-space:nowrap;}
  .gallery{columns:3 260px;column-gap:14px;}
  .gallery figure{margin:0 0 14px;break-inside:avoid;border-radius:12px;overflow:hidden;position:relative;}
  .gallery img{width:100%;height:auto;display:block;transition:transform .4s ease;}
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
  .food-intro{max-width:64ch;font-size:19px;color:var(--ink-soft);margin:0 0 8px;}
  .food-intro b{color:var(--ink);}
  .tacos{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:34px 0 10px;}
  @media (max-width:820px){ .tacos{grid-template-columns:1fr 1fr;} }
  @media (max-width:520px){ .tacos{grid-template-columns:1fr;} }
  .taco{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 18px 20px;}
  .taco .when{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.03em;padding:4px 11px;border-radius:100px;margin-bottom:10px;background:color-mix(in srgb,var(--amarillo) 22%,var(--card));color:var(--ink);}
  .taco h4{margin:0;font-family:var(--serif);font-size:22px;}
  .taco .es{color:var(--verde);font-weight:700;font-size:12px;letter-spacing:.03em;}
  .taco p{margin:8px 0 0;font-size:14px;color:var(--ink-soft);line-height:1.55;}
  .food-more{font-family:var(--serif);font-size:24px;margin:44px 0 4px;}
  .food{display:grid;grid-template-columns:1fr 1fr;gap:6px 40px;}
  @media (max-width:640px){ .food{grid-template-columns:1fr;} }
  .dish{display:flex;gap:16px;padding:16px 0;border-bottom:1px solid var(--line);}
  .dish .n{font-family:var(--serif);font-size:30px;color:var(--rosa);font-weight:700;min-width:44px;}
  .dish h4{margin:0;font-size:19px;font-family:var(--serif);}
  .dish .es{color:var(--verde);font-weight:700;font-size:13px;}
  .dish p{margin:6px 0 0;font-size:14px;color:var(--ink-soft);}
  .chili{color:var(--rosa-deep);font-weight:700;}
  .myth-band{background:#180B10;color:#FBEFF3;}
  .myth-band .eyebrow{color:var(--amarillo);}
  .myth-band h2{color:#FBEFF3;}
  .qa{columns:2 340px;column-gap:20px;}
  .qa-card{break-inside:avoid;margin:0 0 20px;border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:18px;background:rgba(255,255,255,.035);display:flex;flex-direction:column;gap:12px;}
  .msg{display:flex;gap:11px;align-items:flex-start;}
  .msg .av{width:36px;height:36px;border-radius:50%;flex:0 0 36px;display:grid;place-items:center;font-weight:800;font-size:15px;overflow:hidden;}
  .msg-in .av{background:#2f6fed;color:#fff;}
  .msg-out .av{background:var(--rosa);color:#fff;}
  .msg .col{display:flex;flex-direction:column;min-width:0;flex:1;}
  .msg .who{font-size:12px;font-weight:700;margin:0 0 4px;color:rgba(251,239,243,.55);}
  .msg .who .ok{color:#4fd1a5;}
  .msg .bubble{border-radius:14px;padding:11px 14px;font-size:15px;line-height:1.5;}
  .msg-in .bubble{background:#2f6fed;color:#fff;border-top-left-radius:4px;}
  .msg-out{flex-direction:row-reverse;}
  .msg-out .col{align-items:flex-end;}
  .msg-out .who{text-align:right;color:rgba(255,255,255,.7);}
  .msg-out .bubble{background:var(--rosa);color:#fff;border-top-right-radius:4px;}
  @media (max-width:520px){ .msg-out{flex-direction:row;} .msg-out .col{align-items:flex-start;} .msg-out .who{text-align:left;} }
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
LANG_ORDER = ["zh", "ja", "en", "fr", "intl"]
LANG_PATH = {"zh": "/", "ja": "/ja/", "en": "/en/", "fr": "/fr/", "intl": "/intl/"}
LANG_LABEL = {"zh": "中文", "ja": "日本語", "en": "EN·US", "fr": "FR", "intl": "EN·Intl"}
HREFLANG = {"zh": "zh", "ja": "ja", "en": "en-US", "fr": "fr", "intl": "en"}


def langbar(cur):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (LANG_PATH[l], ' class="active"' if l == cur else "", LANG_LABEL[l])
        for l in LANG_ORDER)
    return '<div class="langs">%s</div>' % links


def render(lang, C):
    nav = "".join('<a href="#%s">%s</a>' % (k, v) for k, v in C["nav"])
    gallery = "".join(
        '<figure><img src="/img/%s" alt="%s"%s loading="lazy" decoding="async"><figcaption>%s</figcaption></figure>' % (img, cap, wh(img), cap)
        for img, cap in C["gallery"])
    spots = "".join(
        '<div class="card%s"><div class="thumb"><img src="/img/%s" alt="%s"%s loading="lazy" decoding="async"></div><div class="body"><span class="zh-sub">%s</span><h3>%s</h3><p>%s</p></div></div>'
        % ((" soft" if soft else ""), img, h3, wh(img), sub, h3, p)
        for img, sub, h3, p, soft in C["spots"])
    dishes = "".join(
        '<div class="dish"><div class="n">%02d</div><div><h4>%s <span class="es">%s</span></h4><p>%s</p></div></div>'
        % (i + 1, name, es, desc)
        for i, (name, es, desc) in enumerate(C["dishes"]))
    tacos = "".join(
        '<div class="taco"><span class="when">%s</span><h4>%s <span class="es">%s</span></h4><p>%s</p></div>'
        % (when, name, es, desc)
        for name, es, when, desc in C["tacos"])
    myths = "".join(
        '<div class="qa-card">'
        '<div class="msg msg-in"><div class="av">?</div><div class="col">'
        '<p class="who">%s</p><div class="bubble">%s</div></div></div>'
        '<div class="msg msg-out"><div class="av">R</div><div class="col">'
        '<p class="who">%s <span class="ok">&#10003;</span></p><div class="bubble">%s</div></div></div>'
        '</div>' % (C["anon_label"], q, C["me_label"], a)
        for q, a in C["myths"])
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

    canonical = SITE + LANG_PATH[lang]
    alts = "".join(
        '<link rel="alternate" hreflang="%s" href="%s%s">' % (HREFLANG[l], SITE, LANG_PATH[l])
        for l in LANG_ORDER)
    alts += '<link rel="alternate" hreflang="x-default" href="%s/">' % SITE

    # --- structured data: ProfessionalService + FAQPage (desde mitos) ---
    site_schema = {
        "@context": "https://schema.org", "@type": "WebSite",
        "@id": SITE + "/#website", "url": SITE + "/", "name": "Authentic CDMX",
        "inLanguage": C["htmllang"],
        "publisher": {"@id": SITE + "/#business"},
    }
    page_schema = {
        "@context": "https://schema.org", "@type": "WebPage",
        "@id": canonical + "#webpage", "url": canonical, "name": C["title"],
        "description": strip_tags(C["desc"]), "inLanguage": C["htmllang"],
        "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": SITE + "/#business"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": OG_IMG,
                               "width": 1200, "height": 630},
    }
    faq = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "inLanguage": C["htmllang"],
        "mainEntity": [
            {"@type": "Question", "name": strip_tags(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in C["myths"]],
    }
    offers = [
        {"@type": "Offer", "name": pk["name"], "price": pk["price"].replace("$", ""),
         "priceCurrency": "USD", "availability":
             "https://schema.org/SoldOut" if pk.get("sold") else "https://schema.org/InStock",
         "description": " · ".join(strip_tags(f) for f in pk["features"])}
        for pk in C["packs"]]
    biz = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "@id": SITE + "/#business", "name": "Authentic CDMX",
        "image": OG_IMG, "url": canonical, "description": strip_tags(C["desc"]),
        "areaServed": {"@type": "City", "name": "Mexico City"},
        "address": {"@type": "PostalAddress", "addressLocality": "Ciudad de México", "addressRegion": "CDMX", "addressCountry": "MX"},
        "geo": {"@type": "GeoCoordinates", "latitude": 19.4326, "longitude": -99.1332},
        "priceRange": "$$", "email": "authenticcdmx@gmail.com",
        "sameAs": ["https://instagram.com/rod0cv"],
        "knowsLanguage": ["es", "en", "fr", "zh", "ja"],
        "availableLanguage": ["English", "Spanish"],
        "serviceType": "Travel and portrait photography, local guide",
        "provider": {"@type": "Person", "name": "Rodo", "jobTitle": "Photographer & local guide",
                     "sameAs": ["https://instagram.com/rod0cv"]},
        "makesOffer": offers,
    }
    jsonld = "".join('<script type="application/ld+json">%s</script>' % json.dumps(o, ensure_ascii=False)
                     for o in (site_schema, biz, page_schema, faq))

    og_alt = "".join('<meta property="og:locale:alternate" content="%s">' % OG_LOCALE[l]
                     for l in LANG_ORDER if l != lang)
    seo = (
        '<link rel="canonical" href="%(can)s">'
        '<meta name="robots" content="index,follow,max-image-preview:large">'
        '<meta name="theme-color" content="#EC1E79">'
        '<meta name="author" content="Rodo">'
        '<link rel="icon" href="/favicon.ico" sizes="any">'
        '<link rel="icon" type="image/png" href="/favicon.png">'
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png">'
        '<meta property="og:type" content="website">'
        '<meta property="og:site_name" content="Authentic CDMX">'
        '<meta property="og:title" content="%(title)s">'
        '<meta property="og:description" content="%(desc)s">'
        '<meta property="og:url" content="%(can)s">'
        '<meta property="og:image" content="%(og)s">'
        '<meta property="og:image:width" content="1200">'
        '<meta property="og:image:height" content="630">'
        '<meta property="og:image:alt" content="Authentic CDMX — Mexico City photography & guide">'
        '<meta name="twitter:image:alt" content="Authentic CDMX — Mexico City photography & guide">'
        '<meta property="og:locale" content="%(loc)s">%(ogalt)s'
        '<meta name="twitter:card" content="summary_large_image">'
        '<meta name="twitter:title" content="%(title)s">'
        '<meta name="twitter:description" content="%(desc)s">'
        '<meta name="twitter:image" content="%(og)s">'
        '%(jsonld)s'
    ) % dict(can=canonical, title=C["title"], desc=C["desc"], og=OG_IMG,
             loc=OG_LOCALE[lang], ogalt=og_alt, jsonld=jsonld)
    alts = alts + seo

    html = """<!doctype html>
<html lang="%(htmllang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="preload" as="image" href="/img/hero-street.jpg" fetchpriority="high">
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
  <img class="bg" src="/img/hero-street.jpg" alt="%(hero_alt)s" width="853" height="1280" fetchpriority="high" decoding="async">
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
  <p class="food-intro">%(food_intro)s</p>
  <div class="tacos">%(tacos)s</div>
  <h3 class="food-more">%(food_more)s</h3>
  <div class="food">%(dishes)s</div>
  <p class="note">%(food_corn)s</p>
</div></section>
<section id="mitos" class="myth-band"><div class="wrap">
  <p class="eyebrow">%(myth_eyebrow)s</p>
  <div class="shead"><h2 style="color:#FBEFF3">%(myth_h2)s</h2></div>
  <div class="qa">%(myths)s</div>
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
  <p class="note" style="max-width:520px;margin:22px auto 0;text-align:left;">%(con_comm)s</p>
  <p class="lede" style="margin:18px auto 0;">%(con_lede)s</p>
</div></section>
<footer>%(footer)s</footer>
</body>
</html>
""" % dict(
        htmllang=C["htmllang"], title=C["title"], desc=C["desc"], alts=alts, css=CSS,
        hero_alt=C.get("hero_alt", "Authentic Mexico City street photography by Rodo — local CDMX photographer and guide"),
        nav=nav, langbar=langbar(lang), kicker=C["kicker"], h1=C["h1"], sub=C["sub"],
        cta1=C["cta1"], cta2=C["cta2"], man_eyebrow=C["man_eyebrow"], man_h2=C["man_h2"], man_p=C["man_p"],
        port_eyebrow=C["port_eyebrow"], port_h2=C["port_h2"], port_tag=C["port_tag"], gallery=gallery,
        spot_eyebrow=C["spot_eyebrow"], spot_h2=C["spot_h2"], spot_tag=C["spot_tag"], spots=spots, spot_note=C["spot_note"],
        food_eyebrow=C["food_eyebrow"], food_h2=C["food_h2"], food_tag=C["food_tag"], dishes=dishes,
        food_intro=C["food_intro"], tacos=tacos, food_more=C["food_more"], food_corn=C["food_corn"],
        myth_eyebrow=C["myth_eyebrow"], myth_h2=C["myth_h2"], myths=myths,
        pack_eyebrow=C["pack_eyebrow"], pack_h2=C["pack_h2"], pack_tag=C["pack_tag"], packs=packs, pack_note=C["pack_note"],
        plano_eyebrow=C["plano_eyebrow"], plano_h2=C["plano_h2"], plano_tag=C["plano_tag"], plano_lede=C["plano_lede"], planos=planos,
        con_eyebrow=C["con_eyebrow"], con_h2=C["con_h2"], con_wechat=C["con_wechat"], con_lede=C["con_lede"],
        con_comm=C["con_comm"], footer=C["footer"],
    )
    return html


# ----------------- CONTENIDO POR IDIOMA -----------------
GAL = lambda caps: list(zip(
    ["portrait-red.jpg","angel-bw.jpg","skyline-sunset.jpg","doorway.jpg","vocho.jpg","mural-wings.jpg",
     "intersection.jpg","revolucion.jpg","oxxo.jpg","red-car.jpg","mural-dragon.jpg","moto.jpg"], caps))

# dimensiones reales (px) — reservan espacio y matan CLS (Core Web Vitals)
DIMS = {
    "portrait-red.jpg":(1280,853),"angel-bw.jpg":(853,1280),"skyline-sunset.jpg":(960,1280),
    "doorway.jpg":(853,1280),"vocho.jpg":(720,1280),"mural-wings.jpg":(720,1280),
    "intersection.jpg":(1280,720),"revolucion.jpg":(960,1280),"oxxo.jpg":(1280,853),
    "red-car.jpg":(853,1280),"mural-dragon.jpg":(1280,720),"moto.jpg":(1280,853),
    "cielo-abierto.jpg":(720,1280),"reforma-dusk.jpg":(853,1280),"torre-night.jpg":(960,1280),
    "revolucion.jpg":(960,1280),"hero-street.jpg":(853,1280),"portrait-red.jpg":(1280,853),
}
def wh(img):
    d = DIMS.get(img)
    return (' width="%d" height="%d"' % d) if d else ""

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
   ("cielo-abierto.jpg","PLAZA CIELO ABIERTO","天空广场 Cielo Abierto","红色拱廊 + 霓虹灯的现代空间。造型感强、超上镜 —— 拍出来像电影场景。",False),
   ("oxxo.jpg","CALLE · MERCADO","街头 & 市场","小卖部、水果摊、涂鸦墙。真正的城市日常，随手一拍就是故事，比景点真实一百倍。",False),
   ("reforma-dusk.jpg","ROMA · CONDESA","罗马 & 康德萨区","公开的秘密 —— 又潮又安全、最 foreign-friendly，咖啡馆和涂鸦墙确实好看。想拍网红风就来，但别只拍这里。",True),
   ("vocho.jpg","ICONOS · 城市符号","甲壳虫 & 城市符号","老 Vocho、棕榈树、复古招牌。这些细节才是墨西哥城的灵魂，明信片上没有。",False),
   ("skyline-sunset.jpg","ROOFTOP · 天台日落","天台看日落","想要大片天际线？我知道几个能上去的天台，日落 golden hour 一组，绝了。",False)],
 "spot_note":"🗺️ 想去金字塔（Teotihuacán）、霍奇米尔科、Roma/Condesa 打卡？都能安排。但想要别人没有的照片 —— 上面那些冷门点才是重点。",
 "food_eyebrow":"Qué comer · 吃什么","food_h2":"塔可不是一道菜，<br>是一整套文化","food_tag":"Sabores",
 "food_intro":"在墨西哥，<b>塔可 taco 不是「一道菜」，是一种「形式」</b> —— 像寿司一样多样，像面包、像奶酪一样千变万化。而<b>玉米 maíz，在墨西哥就是文化本身</b>。而且不是什么都能随时吃：barbacoa 和 carnitas 是周末早上的仪式，pastor 是夜宵。",
 "tacos":[
   ("Al pastor","牧羊人","🌙 夜宵","立式烤炉的 adobo 腌猪肉 + 菠萝。夜晚之王，配香菜洋葱。"),
   ("Canasta / al vapor","篮子塔可","🌅 早上","自行车叫卖的蒸软塔可，便宜又家常。土豆、豆泥、猪皮。"),
   ("Guisado","炖菜","☀️ 中午","大锅炖：tinga 鸡肉、rajas 辣椒、chicharrón 猪皮。家常午餐。"),
   ("Carnitas","脆皮猪","🌅 周末上午","米却肯式慢炖炸猪肉，各个部位都有。周末早晨的仪式。"),
   ("Barbacoa","蒸羊肉","🌅 周末上午","龙舌兰叶包蒸的羊肉，配 consomé 汤。周末限定，去晚就卖光。"),
   ("Cochinita pibil","尤卡坦","🍊 特色","achiote 红酱慢烤猪肉，尤卡坦名物，配腌紫洋葱。")],
 "food_more":"塔可之外",
 "dishes":[
   ("Mole","莫雷酱","巧克力+辣椒+香料的酱，浇在鸡肉上。味道复杂，普埃布拉名菜。"),
   ("Elote / Esquite","墨西哥烤玉米","玉米抹蛋黄酱、芝士粉、辣椒粉、青柠。街头小吃之王，玉米文化的日常。"),
   ("Tamal","玉米粽","玉米面裹馅，用玉米叶或香蕉叶蒸熟。早餐配 atole 热饮。"),
   ("Barrio Chino","唐人街","<span class=\"chili\">先说清楚：这里的「中餐」是墨西哥化的，别期待家乡味。</span>但拍照氛围很好。"),
   ("正宗中餐","Auténtico","想吃地道川菜/粤菜？我带你去本地华人真正吃的馆子，不踩雷。")],
 "food_corn":"🌽 玉米在墨西哥不只是食物 —— 从塔可、tamal 到 atole，几千年的文明都建立在玉米上。吃一个塔可，就是在吃这座城市的历史。",
 "myth_eyebrow":"Mitos y verdades · 谣言粉碎机","myth_h2":"你私信问我的，<br>我一条条回你",
 "anon_label":"匿名 · 游客","me_label":"Rodo · Authentic CDMX",
 "myths":[
   ("听说墨西哥城很危险，我有点怕…是真的吗？😟","旅游区白天很安全。晚上叫 Uber、别露富，跟任何大城市一样。有我带着，我知道哪条街该走、哪条别走。"),
   ("是不是所有东西都很辣？我吃不了辣 🌶️","不会。辣椒酱都是分开放的，你完全可以不加。会说一句「sin chile」就行。"),
   ("自来水能喝吗？","别直接喝，买瓶装水 agua embotellada。餐厅的冰块一般是净化水，正常吃没问题。"),
   ("需要给小费吗？给多少？","餐厅 10–15%。带点现金和一张 Visa —— 微信 / 支付宝这边商家几乎不收。"),
   ("听说海拔很高，会不会有高原反应？","墨西哥城 2240 米，走快可能会喘，少数人轻微高反。第一天别排太满，多喝水就好。"),
   ("我西语和英语都不太行，能沟通吗？😅","旅游区基础英语能用。有我在，英语 / 西语全程沟通 —— 点菜、打车、砍价都交给我。")],
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
 "con_comm":"🗣 <b>沟通语言：英语 或 西班牙语。</b> 我不说中文，但全程用英语 / 西语沟通没问题，也会用翻译软件帮你点菜、打车、带路。<b>预约时请用英文或西班牙语留言。</b>",
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
   ("cielo-abierto.jpg","PLAZA CIELO ABIERTO","Plaza Cielo Abierto","A modern open-air corridor with red arches and neon. Bold, cinematic, super photogenic — looks like a film set.",False),
   ("oxxo.jpg","CALLE · MERCADO","Streets & markets","Corner stores, fruit stands, graffiti walls. Real daily life — one frame and you've got a story, a hundred times more real than a landmark.",False),
   ("reforma-dusk.jpg","ROMA · CONDESA","Roma & Condesa","The worst-kept secret — trendy, safe, the most foreign-friendly. Cafés and murals really do look good. Come for the IG shot, just don't stop there.",True),
   ("vocho.jpg","ICONOS · city symbols","Vochos & city icons","Old VW Beetles, palm trees, retro signage. The details are the soul of this city — never on a postcard.",False),
   ("skyline-sunset.jpg","ROOFTOP · sunset","Rooftop golden hour","Want the big skyline? I know a few rooftops you can actually get onto. One golden-hour set and it's a wrap.",False)],
 "spot_note":"🗺️ Want Teotihuacán pyramids, Xochimilco, or the Roma/Condesa checklist? All doable. But if you want photos nobody else has, the off-map spots above are the point.",
 "food_eyebrow":"What to eat","food_h2":"A taco isn't a dish,<br>it's a whole culture","food_tag":"Sabores",
 "food_intro":"In Mexico, <b>a taco isn't a dish — it's a format.</b> As varied as sushi, as bread, as cheese. And <b>corn (maíz) is culture itself.</b> Not everything is eaten anytime, either: barbacoa and carnitas are a weekend-morning ritual; al pastor is a late-night thing.",
 "tacos":[
   ("Al pastor","spit-roast pork","🌙 Night","Adobo-marinated pork off a vertical trompo + pineapple. King of the night, with cilantro and onion."),
   ("Canasta / steamed","basket tacos","🌅 Morning","Soft steamed tacos sold off a bicycle — cheap, homey. Potato, beans, chicharrón."),
   ("Guisado","stew tacos","☀️ Midday","Straight from the pot: tinga, rajas, chicharrón. The everyday lunch taco."),
   ("Carnitas","confit pork","🌅 Weekend AM","Michoacán-style slow-cooked pork, every cut. A weekend-morning ritual."),
   ("Barbacoa","steamed lamb","🌅 Weekend AM","Agave-leaf steamed lamb with consomé broth. Weekends only — go early or it's gone."),
   ("Cochinita pibil","Yucatán","🍊 Specialty","Achiote-marinated slow-roast pork from Yucatán, with pickled red onion.")],
 "food_more":"Beyond the taco",
 "dishes":[
   ("Mole","chili-chocolate sauce","Chili + chocolate + spices over chicken. Complex, iconic Puebla dish."),
   ("Elote / Esquite","Mexican street corn","Corn with mayo, cheese, chili powder, lime. King of street snacks — everyday corn culture."),
   ("Tamal","steamed corn parcel","Corn dough with a filling, steamed in a husk or banana leaf. Breakfast, with a warm atole."),
   ("Barrio Chino","Chinatown","<span class=\"chili\">Heads up: the “Chinese” food here is Mexican-ized — don't expect the real thing.</span> Great photo vibe though."),
   ("Real Chinese","Auténtico","Craving proper Sichuan/Cantonese? I'll take you where the local Chinese community actually eats.")],
 "food_corn":"🌽 Corn in Mexico isn't just food — from tacos to tamales to atole, thousands of years of civilization are built on it. Eating a taco is eating the city's history.",
 "myth_eyebrow":"Myths & truths","myth_h2":"The stuff you DM me —<br>answered, one by one",
 "anon_label":"Anonymous · traveler","me_label":"Rodo · Authentic CDMX",
 "myths":[
   ("Everyone says Mexico City is dangerous… is it really that bad? 😟","Tourist areas are fine by day. At night take Uber, don't flash valuables — same as any big city. With me you're covered: I know which streets to take and which to skip."),
   ("Is everything super spicy? I can't handle heat 🌶️","Nope. The salsa is always on the side — just don't add it. Say “sin chile” and you're good."),
   ("Can I drink the tap water?","Don't drink it straight — grab bottled water. Restaurant ice is usually purified, so eating out is fine."),
   ("Do I need to tip? How much?","10–15% at restaurants. Bring some cash + a Visa — WeChat/Alipay aren't really accepted here."),
   ("I heard the altitude is high — will I feel it?","Mexico City sits at 2,240 m (7,350 ft). You might get a little winded walking fast. Take day one easy and drink water."),
   ("My English and Spanish aren't great — can we still communicate? 😅","Basic English works in tourist zones. With me it's fully English/Spanish — ordering, taxis, haggling all handled.")],
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
 "con_comm":"🗣 <b>We communicate in English or Spanish.</b> Message me in either one — on the ground I'll handle ordering food, taxis and directions for you.",
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
   ("cielo-abierto.jpg","PLAZA CIELO ABIERTO","Plaza Cielo Abierto","Un couloir moderne à ciel ouvert, arches rouges et néons. Graphique, cinématographique, très photogénique — on dirait un décor de film.",False),
   ("oxxo.jpg","CALLE · MERCADO","Rues & marchés","Épiceries de coin, étals de fruits, murs de graffitis. La vraie vie quotidienne — une image et vous avez une histoire, cent fois plus vraie qu'un monument.",False),
   ("reforma-dusk.jpg","ROMA · CONDESA","Roma & Condesa","Le secret le moins bien gardé — branché, sûr, le plus accueillant pour les étrangers. Cafés et fresques sont vraiment beaux. Venez pour la photo Insta, mais ne vous arrêtez pas là.",True),
   ("vocho.jpg","ICONOS · symboles","Vochos & symboles de la ville","Vieilles Coccinelles VW, palmiers, enseignes rétro. Les détails sont l'âme de cette ville — jamais sur une carte postale.",False),
   ("skyline-sunset.jpg","ROOFTOP · coucher de soleil","Toits à l'heure dorée","Envie du grand panorama urbain ? Je connais des toits accessibles. Une série à l'heure dorée et c'est plié.",False)],
 "spot_note":"🗺️ Envie des pyramides de Teotihuacán, de Xochimilco ou de la checklist Roma/Condesa ? Tout est possible. Mais pour des photos que personne d'autre n'a, les lieux hors des sentiers ci-dessus sont l'essentiel.",
 "food_eyebrow":"Quoi manger","food_h2":"Le taco n'est pas un plat,<br>c'est toute une culture","food_tag":"Sabores",
 "food_intro":"Au Mexique, <b>le taco n'est pas un plat — c'est un format.</b> Aussi varié que le sushi, que le pain, que les fromages. Et <b>le maïs (maíz), c'est la culture elle-même.</b> On ne mange pas tout à toute heure : la barbacoa et les carnitas sont un rituel du week-end matin ; l'al pastor se mange le soir.",
 "tacos":[
   ("Al pastor","porc à la broche","🌙 Soir","Porc mariné à l'adobo sur trompo vertical + ananas. Le roi de la nuit, coriandre et oignon."),
   ("Canasta / vapeur","tacos panier","🌅 Matin","Tacos vapeur moelleux vendus à vélo — bon marché, familial. Pomme de terre, haricots, chicharrón."),
   ("Guisado","mijoté","☀️ Midi","Tout droit de la marmite : tinga, rajas, chicharrón. Le taco du déjeuner de tous les jours."),
   ("Carnitas","porc confit","🌅 Week-end matin","Porc mijoté à la façon du Michoacán, tous les morceaux. Un rituel du week-end."),
   ("Barbacoa","agneau vapeur","🌅 Week-end matin","Agneau cuit vapeur en feuilles d'agave, avec consomé. Le week-end seulement — arrivez tôt."),
   ("Cochinita pibil","Yucatán","🍊 Spécialité","Porc mariné à l'achiote rôti lentement, du Yucatán, avec oignon rouge mariné.")],
 "food_more":"Au-delà du taco",
 "dishes":[
   ("Mole","sauce piment-chocolat","Piment + chocolat + épices sur du poulet. Complexe, plat emblématique de Puebla."),
   ("Elote / Esquite","maïs de rue","Maïs avec mayo, fromage, piment en poudre, citron vert. Le roi du snack — la culture du maïs au quotidien."),
   ("Tamal","pâte de maïs vapeur","Pâte de maïs farcie, cuite vapeur dans une feuille. Petit-déjeuner, avec un atole chaud."),
   ("Barrio Chino","quartier chinois","<span class=\"chili\">Attention : la cuisine « chinoise » ici est mexicanisée — n'attendez pas l'authentique.</span> Mais l'ambiance photo est top."),
   ("Vrai chinois","Auténtico","Envie de vrai sichuanais/cantonais ? Je vous emmène là où la communauté chinoise locale mange vraiment.")],
 "food_corn":"🌽 Au Mexique, le maïs n'est pas qu'un aliment — du taco au tamal en passant par l'atole, des milliers d'années de civilisation reposent dessus. Manger un taco, c'est manger l'histoire de la ville.",
 "myth_eyebrow":"Mythes & vérités","myth_h2":"Ce que vous me demandez en DM —<br>je réponds, une par une",
 "anon_label":"Anonyme · voyageur","me_label":"Rodo · Authentic CDMX",
 "myths":[
   ("Tout le monde dit que Mexico est dangereux… c'est vraiment le cas ? 😟","Les zones touristiques sont sûres de jour. Le soir, Uber, pas d'objets de valeur en vue — comme dans toute grande ville. Avec moi vous êtes couvert : je sais quelles rues prendre et lesquelles éviter."),
   ("Est-ce que tout est très épicé ? Je ne supporte pas 🌶️","Non. La sauce est toujours à part — il suffit de ne pas en mettre. Dites « sin chile » et c'est réglé."),
   ("Est-ce que je peux boire l'eau du robinet ?","Ne la buvez pas telle quelle — prenez de l'eau en bouteille. Les glaçons au restaurant sont en général purifiés, donc manger dehors ne pose pas de souci."),
   ("Faut-il laisser un pourboire ? Combien ?","10–15 % au restaurant. Prévoyez du liquide + une carte Visa — WeChat/Alipay ne sont quasiment pas acceptés ici."),
   ("On m'a dit que l'altitude est élevée — vais-je la ressentir ?","Mexico est à 2 240 m. Vous serez peut-être un peu essoufflé en marchant vite. Allez-y doucement le premier jour et buvez de l'eau."),
   ("Mon anglais et mon espagnol sont limités — on pourra communiquer ? 😅","L'anglais de base passe dans les zones touristiques. Avec moi, tout se fait en anglais/espagnol — commandes, taxis, négociation, je gère.")],
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
 "con_comm":"🗣 <b>Communication en anglais ou en espagnol.</b> Écrivez-moi dans l'une de ces langues — sur place, je m'occupe des commandes, des taxis et de l'itinéraire pour vous.",
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
   ("Everyone says Mexico City is dangerous… is it really that bad? 😟","Tourist areas are fine by day. At night take Uber, don't flash valuables — same as any big city. With me you're covered: I know which streets to take and which to skip."),
   ("Is everything super spicy? I can't handle heat 🌶️","Nope. The salsa is always on the side — just don't add it. Say “sin chile” and you're good."),
   ("Can I drink the tap water?","Don't drink it straight — grab bottled water. Restaurant ice is usually purified, so eating out is fine."),
   ("Do I need to tip? How much?","10–15% at restaurants. Bring some cash + a Visa/Mastercard — mobile wallets aren't really accepted here."),
   ("I heard the altitude is high — will I feel it?","Mexico City sits at 2,240 m (7,350 ft). You might get a little winded walking fast. Take day one easy and drink water."),
   ("My English isn't perfect — can we still communicate? 😅","Basic English works in tourist zones. With me it's fully English/Spanish — ordering, taxis, haggling all handled.")],
})

# ---------- JA ----------
LANGS["ja"] = dict(LANGS["en"])
LANGS["ja"].update({
 "htmllang":"ja","title":"Authentic CDMX · 本当のメキシコシティ撮影ツアー",
 "desc":"地元フォトグラファーが「本当の」メキシコシティを撮影 — 絵はがきではない、街のリアルな姿を。週末の撮影 + ガイド。",
 "nav":[("trabajo","作品"),("lugares","案内"),("comida","食事"),("mitos","誤解"),("foto","予約"),("planos","構図"),("contacto","連絡")],
 "kicker":"メキシコシティ · 本当の姿","h1":"本当の<br><span class=\"es\">メキシコシティ</span>",
 "sub":"地元フォトグラファーが、街のありのままの姿を撮影します — 絵はがきではなく。週末の撮影 + ガイド。英語・スペイン語で対応。",
 "cta1":"プランを見る →","cta2":"作品を見る",
 "man_eyebrow":"Manifiesto · 私の流儀",
 "man_h2":"Roma と Condesa も良い — でもそこは<span class=\"hit\">誰もが知る秘密</span>。私は誰も撮らない場所にも案内します。",
 "man_p":"Roma と Condesa はおしゃれで安全、外国人にもやさしい — 行きたいなら行きましょう、価値はあります。でもあのカフェは何百回も撮られています。私はむしろ、夜の大通り、古い中華街、街のネオンや市場に案内したい — 本物の光、本物の物語、誰も持っていない写真。両方？もちろん大歓迎。",
 "port_eyebrow":"Portafolio · 作品","port_h2":"この街を、<br>私のレンズで","port_tag":"All shot in CDMX",
 "gallery":GAL(["ポートレート · 街角","Ángel de la Independencia","Reforma · 夕暮れ","コロニアルな門","Vocho · VWビートル","Mural · 翼の壁画","夜 · 交差点","Monumento a la Revolución","街角の日常","Neón · ネオン","Mural · 龍","Movimiento · 躍動"]),
 "spot_eyebrow":"案内する場所","spot_h2":"リアルで、絵になる、<br>観光地図にない場所","spot_tag":"Lugares con alma",
 "spots":[
   ("torre-night.jpg","CENTRO 夜","夜の歴史地区","昼は混雑、夜は魔法。Torre Latino、人のいない大通り、暖かい街灯。一番いい写真が撮れる時間帯です。",False),
   ("cielo-abierto.jpg","PLAZA CIELO ABIERTO","Plaza Cielo Abierto","赤いアーチとネオンのモダンな開放型の通路。グラフィックで映画のような雰囲気、とても映える — まるでセットのよう。",False),
   ("oxxo.jpg","CALLE · MERCADO","街と市場","コンビニ、果物屋、グラフィティの壁。本物の日常 — 一枚で物語になる、観光名所より百倍リアル。",False),
   ("reforma-dusk.jpg","ROMA · CONDESA","Roma & Condesa","誰もが知る秘密 — おしゃれで安全、外国人に一番やさしい。カフェも壁画も確かに映える。SNS映えを撮りに来るならどうぞ、でもそこだけで終わらないで。",True),
   ("vocho.jpg","ICONOS · 街の象徴","Vocho と街の象徴","古いVWビートル、ヤシの木、レトロな看板。細部こそこの街の魂 — 絵はがきには写らない。",False),
   ("skyline-sunset.jpg","ROOFTOP · 夕日","屋上のゴールデンアワー","大きなスカイラインが欲しい？登れる屋上をいくつか知っています。夕日の一連で完璧に。",False)],
 "spot_note":"🗺️ テオティワカン遺跡、ソチミルコ、Roma/Condesa の定番も手配できます。でも誰も持っていない写真が欲しいなら、上の穴場こそが本命です。",
 "food_eyebrow":"何を食べる","food_h2":"タコスは一皿の料理ではない、<br>ひとつの文化","food_tag":"Sabores",
 "food_intro":"メキシコでは、<b>タコスは「料理」ではなく「形式」です。</b>寿司のように、パンのように、チーズのように多彩。そして<b>トウモロコシ（maíz）はまさに文化そのもの。</b>何でもいつでも食べられるわけではありません：バルバコアやカルニータスは週末の朝の儀式、アル・パストールは夜の食べ物です。",
 "tacos":[
   ("Al pastor","串焼き豚","🌙 夜","縦型ローストのアドボ漬け豚 + パイナップル。夜の王様、パクチーと玉ねぎで。"),
   ("Canasta / 蒸し","バスケット","🌅 朝","自転車で売られる蒸しタコス — 安くて家庭的。じゃがいも、豆、チチャロン。"),
   ("Guisado","煮込み","☀️ 昼","鍋からそのまま：ティンガ、ラハス、チチャロン。日常のランチタコス。"),
   ("Carnitas","豚のコンフィ","🌅 週末の朝","ミチョアカン風の煮込み豚、あらゆる部位。週末の朝の儀式。"),
   ("Barbacoa","蒸し羊","🌅 週末の朝","アガベの葉で蒸した羊肉、コンソメ添え。週末限定 — 早く行かないと売り切れ。"),
   ("Cochinita pibil","ユカタン","🍊 名物","アチョーテ漬けの豚の低温ロースト、ユカタン名物、赤玉ねぎのピクルスと。")],
 "food_more":"タコスの先へ",
 "dishes":[
   ("Mole","唐辛子チョコソース","唐辛子 + チョコ + スパイスのソースを鶏肉に。複雑な味、プエブラの名物。"),
   ("Elote / Esquite","メキシコ流焼きトウモロコシ","トウモロコシにマヨ、チーズ、唐辛子粉、ライム。屋台スナックの王様 — 日常のトウモロコシ文化。"),
   ("Tamal","トウモロコシ生地の蒸し","具入りのトウモロコシ生地を皮で包んで蒸す。朝食に温かいアトーレと。"),
   ("Barrio Chino","中華街","<span class=\"chili\">先に言うと、ここの「中華」はメキシコ風 — 本場の味は期待しないで。</span>でも写真の雰囲気は最高。"),
   ("本場の中華","Auténtico","本格的な四川/広東料理が食べたい？地元の華人が実際に通う店へ案内します。")],
 "food_corn":"🌽 メキシコでトウモロコシは単なる食べ物ではありません — タコス、タマル、アトーレまで、数千年の文明がその上に築かれています。タコスを食べることは、この街の歴史を食べること。",
 "myth_eyebrow":"Mitos y verdades · 誤解と真実","myth_h2":"DMで届く質問に、<br>ひとつずつ答えます",
 "anon_label":"匿名 · 旅行者","me_label":"Rodo · Authentic CDMX",
 "myths":[
   ("メキシコシティは危険ってよく聞くけど…本当に危ない？😟","観光エリアは昼間は安全です。夜はUber、貴重品は見せない — どの大都市とも同じ。私が一緒なら安心、どの道を通りどの道を避けるか分かっています。"),
   ("何でも辛いんですか？辛いのが苦手で 🌶️","大丈夫。サルサは必ず別添えなので、入れなければOK。「sin chile」と言えば辛さ抜きです。"),
   ("水道水は飲めますか？","そのままは飲まないで、ボトル入りの水を。レストランの氷はたいてい浄水なので、外食は問題ありません。"),
   ("チップは必要？いくら？","レストランで10〜15%。現金とVisaカードを用意して — WeChat/Alipayはこちらではほぼ使えません。"),
   ("標高が高いと聞きました — 影響ありますか？","メキシコシティは標高2,240m。早歩きで少し息切れするかも。初日は無理せず、水分をしっかり。"),
   ("英語もスペイン語も得意じゃないけど、やり取りできますか？😅","観光地では基本英語が通じます。私がいれば英語・スペイン語で全部対応 — 注文、タクシー、交渉、お任せください。")],
 "pack_eyebrow":"撮影プラン · Paquetes","pack_h2":"週末の撮影<br>ガイド + フォトグラファーを一度に","pack_tag":"Fotógrafo local",
 "packs":[
   {"cls":"","badge":None,"badge_cls":"","name":"City Walk","price":"$120","unit":"/2時間","ref":"USD","features":["1か所","編集済み写真25枚","ガイド + 撮影","3日以内に納品"],"btn":"予約する","sold":False},
   {"cls":"feat","badge":"残りわずか","badge_cls":"low","name":"Half Day","price":"$220","unit":"/4時間","ref":"USD","features":["2〜3か所、穴場含む","編集済み写真60枚","ガイド + 撮影 + ルート設計","タクシー・注文サポート","2日以内に納品"],"btn":"今すぐ予約 →","sold":False},
   {"cls":"sold","badge":"満席 SOLD OUT","badge_cls":"sold","name":"Full Day","price":"$320","unit":"/1日","ref":"USD","features":["終日撮影（遺跡オプション）","編集済み写真100枚","移動の手配","日の出 / 屋上スポット"],"btn":"満席","sold":True}],
 "pack_note":"💵 価格は仮です — 実際の料金に差し替えてください。支払い方法を明記（現金 / 送金 / カード）。",
 "plano_eyebrow":"構図のタイプ","plano_h2":"予約前に、<br>どんな写真が欲しいか教えて","plano_tag":"構図を選ぶ",
 "plano_lede":"連絡の際に「1番 / 2番がいい」と一言でOK。決まっていなくても大丈夫 — 現場で私が決めます。大事なのは楽しむこと。",
 "planos":[
   ("wide","全身 + 背景","Plano general · Wide","人物は小さく、景色は大きく。ランドマーク、街、スカイライン向け — あなたと街が一枚に。"),
   ("american","膝上","Plano americano","太もも中ほどから上。定番のエディトリアル感 — 服装も少し背景も見える。"),
   ("portrait","クローズアップ","Retrato · Portrait","顔と肩、背景はぼかし。感情を前面に — プロフィール写真や表紙に最適。"),
   ("fun","スナップ","Libre · Just have fun","飛んで、歩いて、笑って。自然な瞬間こそ一番いい写真になることが多い。")],
 "con_eyebrow":"Contacto · 連絡","con_h2":"メッセージをどうぞ —<br>メキシコシティ撮影を計画しましょう","con_wechat":"WeChat",
 "con_comm":"🗣 <b>やり取りは英語またはスペイン語です。</b> 日本語は話せませんが、現地では英語・スペイン語で対応し、翻訳アプリも使います。<b>ご予約は英語かスペイン語でメッセージください。</b>",
 "con_lede":"日程、行きたい場所、人数を教えてください — オーダーメイドのルートと見積もりを作ります。週末は枠が限られるので、1週間前の予約がおすすめです。",
 "footer":"Authentic CDMX · メキシコシティの地元撮影 &amp; ガイド · Ciudad de México<br>© 2026 · All photos by Rodo",
})

if __name__ == "__main__":
    targets = {l: (ROOT if l == "zh" else os.path.join(ROOT, l)) for l in LANG_ORDER}
    for lang, path in targets.items():
        os.makedirs(path, exist_ok=True)
        html = render(lang, LANGS[lang])
        with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", lang, "->", os.path.join(path, "index.html"), len(html), "bytes")

    # sitemap.xml (hreflang vive en <head>, no se duplica; imágenes → Google Images)
    import datetime
    today = datetime.date.today().isoformat()
    from xml.sax.saxutils import escape as _esc
    # bloque de imágenes (galería + hero) colgado del home — image SEO para fotógrafo
    img_block = "".join(
        '    <image:image><image:loc>%s/img/%s</image:loc><image:title>%s</image:title></image:image>\n'
        % (SITE, img, _esc(strip_tags(cap))) for img, cap in LANGS["en"]["gallery"])
    img_block = ('    <image:image><image:loc>%s/img/hero-street.jpg</image:loc>'
                 '<image:title>Authentic Mexico City street photography</image:title></image:image>\n' % SITE) + img_block
    urls = ""
    for l in LANG_ORDER:
        extra = img_block if l == "zh" else ""
        urls += ('  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority>\n%s  </url>\n'
                 % (SITE, LANG_PATH[l], today, "1.0" if l == "zh" else "0.8", extra))
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
               'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    # robots.txt — permite explícitamente crawlers de IA (GEO)
    ai_bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web",
               "anthropic-ai", "PerplexityBot", "Google-Extended", "Applebot-Extended",
               "Bingbot", "Amazonbot", "CCBot"]
    robots = "User-agent: *\nAllow: /\n\n"
    for b in ai_bots:
        robots += "User-agent: %s\nAllow: /\n\n" % b
    robots += "Sitemap: %s/sitemap.xml\n" % SITE
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    # llms.txt — resumen para LLMs (Claude, ChatGPT, Perplexity)
    llms = """# Authentic CDMX

> Local photographer and guide in Mexico City (Ciudad de México). Weekend photo sessions that capture the real city — street, night avenues, old Chinatown, markets, murals — not just the postcard spots. Guide + photographer in one. Communication in English or Spanish.

## What it is
- Service: travel & portrait photography plus local guiding in Mexico City.
- Photographer: Rodo. Instagram: https://instagram.com/rod0cv
- Contact: authenticcdmx@gmail.com · WeChat (QR on site).
- Languages of the website: Chinese, Japanese, English, French. Communication with clients happens in English or Spanish.

## Packages (USD, indicative)
- City Walk — $120 / 2 hours, 1 location, 25 edited photos.
- Half Day — $220 / 4 hours, 2-3 locations, 60 edited photos (low availability).
- Full Day — $320 / full day, 100 edited photos, pyramids optional (currently sold out).

## Shot types offered
- Wide / full body with background (plano general)
- Knees-up / american shot (plano americano)
- Close portrait (retrato)
- Candid / just have fun

## Good to know (Mexico City for tourists)
- Tourist areas are safe by day; use Uber at night. Safer with a local guide.
- Not everything is spicy — salsa is served on the side.
- Don't drink tap water; use bottled water.
- Tipping 10-15% at restaurants.
- Altitude 2,240 m (7,350 ft) — pace day one.

## Pages
- Chinese (default): %(s)s/
- Japanese: %(s)s/ja/
- English (US): %(s)s/en/
- French: %(s)s/fr/
- International English: %(s)s/intl/
""" % {"s": SITE}
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms)
    print("wrote sitemap.xml + robots.txt + llms.txt")
