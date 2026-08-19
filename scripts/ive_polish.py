from pathlib import Path
import re

for name in ['index.html', 'jelentkezes.html', 'adatvedelem.html']:
    p = Path(name)
    if not p.exists():
        continue
    s = p.read_text(encoding='utf-8')
    s = s.replace('images/logo-new.svg', 'images/logo.svg')
    s = s.replace('https://becs.taltosdob.hu/images/logo-new.svg', 'https://taltosdob.magyariskola.at/images/logo.png')
    s = re.sub(r'<link rel="icon"[^>]*href="images/logo\.svg"[^>]*>', '<link rel="icon" type="image/png" href="images/logo.png">', s)
    s = s.replace('<link rel="apple-touch-icon" href="images/logo.svg">', '<link rel="apple-touch-icon" href="images/logo.png">')
    p.write_text(s, encoding='utf-8')

p = Path('index.html')
s = p.read_text(encoding='utf-8')
s = re.sub(r'<svg class="nav-tree".*?</svg>', '<img class="nav-brand-logo" src="images/logo.svg" alt="Világfa Sárkányai logó">', s, count=1, flags=re.S)
s = s.replace('https://becs.taltosdob.hu/', 'https://taltosdob.magyariskola.at/')
s = s.replace('https://becs.taltosdob.hu', 'https://taltosdob.magyariskola.at')

polish_css = r'''
/* ========== 2026-08 authentic precision polish ========== */
:root{--night:#1D2A1E;--night-soft:#26372A;--gold:#C8A65B;--gold-bright:#E5C980;--parchment:#F3EFE5;--parchment-dim:#D9D2C2;--ink:#22251F;--surface:#FAF8F2;--hairline:rgba(41,47,38,.12)}
body{background:var(--surface);letter-spacing:-.012em}
.wrap{width:min(1180px,88vw)}
.nav{background:rgba(25,37,27,.82)!important;border-bottom:1px solid rgba(255,255,255,.08)!important;backdrop-filter:saturate(140%) blur(22px)!important;-webkit-backdrop-filter:saturate(140%) blur(22px)!important}
.nav-brand-logo{width:48px;height:48px;object-fit:contain;flex:0 0 auto;filter:none!important}
.nav-title-main{letter-spacing:-.02em;font-weight:600}.nav-title-sub{opacity:.66;letter-spacing:.01em}
.hero{min-height:92vh;background:radial-gradient(ellipse 95% 70% at 50% 4%,#344B37 0%,#223324 47%,#142016 100%)!important}
.hero-content{padding-top:clamp(7rem,12vw,10rem)!important;padding-bottom:clamp(6rem,10vw,9rem)!important}
.hero-logo{width:clamp(116px,14vw,172px)!important;height:auto!important;object-fit:contain!important;filter:drop-shadow(0 16px 38px rgba(0,0,0,.18))!important;margin-bottom:2rem!important}
.hero h1{max-width:12ch;font-size:clamp(3.4rem,7.2vw,6.7rem)!important;line-height:.94!important;letter-spacing:-.045em!important}
.hero-sub{max-width:52ch!important;font-size:clamp(1.05rem,1.5vw,1.22rem)!important;line-height:1.72!important}
.btn{border-radius:999px!important;min-height:48px;padding:.9rem 1.55rem!important;font-weight:600!important;letter-spacing:-.01em;box-shadow:none!important}.btn-gold:hover{transform:translateY(-1px)}
.feature{padding:clamp(5.5rem,9vw,9.5rem) 0!important}.feature-grid{gap:clamp(3rem,7vw,7rem)!important;align-items:center!important}
.feature h2,.learn-head h2,.year-head h2,.location-section h2,.info-section h2{letter-spacing:-.035em!important;line-height:1.02!important}.feature p,.learn-head p,.year-head p,.location-section p,.info-section p{line-height:1.78!important}
.feature-img,.instructor-img{overflow:hidden!important;border-radius:28px!important;background:#EEE9DE!important;box-shadow:0 24px 70px rgba(25,34,26,.09)!important}
.feature-img img,.instructor-img img{width:100%!important;height:auto!important;max-height:none!important;object-fit:contain!important;object-position:center!important;display:block!important}
.full-bleed{height:auto!important;min-height:0!important;background:#172019!important;overflow:hidden!important}.full-bleed img{position:relative!important;inset:auto!important;width:100%!important;height:auto!important;max-height:none!important;object-fit:contain!important;object-position:center!important;display:block!important}.full-bleed .overlay{background:linear-gradient(180deg,transparent 52%,rgba(12,17,13,.72) 100%)!important}.bleed-duo{display:grid!important;gap:1px!important;background:rgba(255,255,255,.06)!important}
.learn-section,.location-section{padding:clamp(5.5rem,9vw,9rem) 0!important}.learn-row{padding:1.45rem 0!important;border-bottom:1px solid var(--hairline)!important}
.year-section{padding:clamp(6rem,10vw,10rem) 0!important;background:linear-gradient(180deg,#1C2B1E,#142016)!important}.months-rail{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:18px!important;overflow:visible!important}.month-card{min-width:0!important;border-radius:22px!important;border:1px solid rgba(229,201,128,.16)!important;background:rgba(255,255,255,.055)!important;box-shadow:none!important;padding:1.65rem!important}.month-name{letter-spacing:.01em!important}.month-theme{line-height:1.15!important}
.location-card,.info-block,.price-card{border-radius:24px!important;box-shadow:none!important}.location-card,.info-block{border:1px solid var(--hairline)!important;background:rgba(255,255,255,.78)!important}.price-card{background:#172219!important}
.mission-section{padding:clamp(6rem,11vw,11rem) 0!important}.mission-section blockquote{letter-spacing:-.035em!important;line-height:1.08!important}.closing-section{padding:clamp(7rem,12vw,11rem) 0 4.5rem!important}.reveal,.reveal-img{transition-duration:.85s!important}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}.reveal,.reveal-img,.stagger-child{opacity:1!important;transform:none!important}}
@media(max-width:980px){.months-rail{grid-template-columns:repeat(2,minmax(0,1fr))!important}.feature-grid{gap:2.8rem!important}}
@media(max-width:680px){.wrap{width:min(92vw,680px)}.nav-brand-logo{width:42px;height:42px}.nav-title-sub{display:none!important}.hero{min-height:auto!important}.hero-content{padding-top:8.6rem!important;padding-bottom:5.8rem!important}.hero h1{font-size:clamp(3.1rem,15vw,4.55rem)!important}.feature{padding:4.6rem 0!important}.feature-grid{gap:2.2rem!important}.feature-img,.instructor-img{border-radius:20px!important}.months-rail{grid-template-columns:1fr!important;gap:13px!important}.month-card{padding:1.35rem!important;border-radius:18px!important}.full-bleed .caption{padding-bottom:1.25rem!important}}
'''
if '2026-08 authentic precision polish' not in s:
    s = s.replace('</style>', polish_css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')

p = Path('jelentkezes.html')
s = p.read_text(encoding='utf-8')
s = s.replace('https://becs.taltosdob.hu/', 'https://taltosdob.magyariskola.at/')
s = s.replace('https://becs.taltosdob.hu', 'https://taltosdob.magyariskola.at')
signup_css = r'''
/* 2026-08 precision polish */
body{background:#F4F0E7!important;letter-spacing:-.012em}.form-hero{background:radial-gradient(ellipse 105% 80% at 50% -12%,#38503B 0%,#233426 55%,#142016 100%)!important;padding-top:4.5rem!important}.form-hero img.logo{width:clamp(112px,15vw,154px)!important;height:auto!important;object-fit:contain!important;filter:drop-shadow(0 14px 34px rgba(0,0,0,.18))!important}.form-hero h1{letter-spacing:-.035em!important}.card{border:1px solid rgba(42,42,30,.08)!important;box-shadow:0 24px 70px rgba(36,51,35,.08)!important}.program-summary,.highlight-box{border-radius:20px!important;background:#F7F1E4!important}.field input,.field select,.field textarea{background:#FFFEFB!important;border-color:#D8D0C0!important}.btn-submit{min-height:52px!important;box-shadow:none!important}
'''
if '2026-08 precision polish' not in s:
    s = s.replace('</style>', signup_css + '\n</style>', 1)
p.write_text(s, encoding='utf-8')

p = Path('adatvedelem.html')
if p.exists():
    s = p.read_text(encoding='utf-8')
    s = s.replace('https://becs.taltosdob.hu/', 'https://taltosdob.magyariskola.at/')
    s = s.replace('https://becs.taltosdob.hu', 'https://taltosdob.magyariskola.at')
    s = s.replace('images/logo-new.svg', 'images/logo.svg')
    p.write_text(s, encoding='utf-8')
