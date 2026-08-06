# -*- coding: utf-8 -*-
"""Генератор 100 уникальных лендингов EduPrograms (сетка сайтов).
Контент — из основного сайта edu-programs-shop. Разные: названия, цены, дизайн, шрифты, motion.
"""
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, 'variants')
random.seed(42)

FORM_ENDPOINT = 'https://script.google.com/macros/s/AKfycbyC76Bl2zSpsTZIfDSfzoPECW7kIVwrmPGcEOMT3thmQWa4beTQJ2377Bjl3cJ26TYYAQ/exec'
FALLBACK_EMAIL = 'kvant.aa@mail.ru'
PHONE = '+7 923 216 77 72'
SELLER = 'ООО «КВАНТ+» · ОГРН 1151901001108 · ИНН/КПП 1901123634/190101001'
ADDR = 'Республика Хакасия, г. Абакан · E-mail: %s · Тел: %s' % (FALLBACK_EMAIL, PHONE)

# ---------- 100 уникальных названий ----------
NAMES = []
_n1 = ['ПРОФ', 'Образ', 'Учеб', 'Готовые', 'Программ', 'Комплект', 'Документ', 'Центр', 'Академия', 'Вектор',
       'Стандарт', 'Прайм', 'Мастер', 'Прогресс', 'Лидер', 'Формат', 'Знание', 'Старт', 'Профи', 'Эксперт']
_n2 = ['Программы', 'Комплекты', 'Центр', 'Документы', 'Учебник', 'Академия', 'Стандарт', 'Профиль', 'Бюро',
       'Лаборатория', 'Фабрика', 'Портал', 'Ресурс', 'Система', 'Практика', 'Сервис', 'Консалт', 'Онлайн',
       'Маркет', 'Компания']
used = set()
for a in _n1:
    for b in _n2:
        n = a + b
        if n not in used:
            used.add(n)
            NAMES.append(n)
        if len(NAMES) >= 100:
            break
    if len(NAMES) >= 100:
        break
for n in ['ПрограммСтандарт', 'ОбразЛидер', 'УчебМаркет', 'ПРОФЭксперт', 'КомплектПрайм']:
    if len(NAMES) >= 100:
        break
    if n not in used:
        used.add(n)
        NAMES.append(n)
assert len(NAMES) >= 100, len(NAMES)

# ---------- цены: (комплект, пакет5) круглые ----------
PRICES = [(3900, 15900), (4500, 17900), (4900, 19900), (5500, 21900), (5900, 23500),
          (3500, 13900), (6500, 25900), (6900, 27500), (4200, 16900), (6100, 24500),
          (5300, 21500), (4700, 18900), (3800, 15500), (5600, 22900), (7200, 28900),
          (4400, 17900), (4900, 19500), (6600, 26500), (5800, 22900), (3700, 14900)]

# ---------- палитры ----------
PALETTES = [
    dict(bg='#f8fafc', surface='#ffffff', text='#1a1a2e', muted='#64748b', primary='#2563eb', accent='#7c3aed', hero='#0f172a', dark=True),
    dict(bg='#faf6ef', surface='#ffffff', text='#241a0e', muted='#8a7a66', primary='#b45309', accent='#0f172a', hero='#3b2413', dark=True),
    dict(bg='#f0fdf4', surface='#ffffff', text='#052e16', muted='#5b8a72', primary='#10b981', accent='#047857', hero='#022c22', dark=True),
    dict(bg='#fff1f2', surface='#ffffff', text='#2a0a10', muted='#9f7a82', primary='#e11d48', accent='#7c3aed', hero='#1c1017', dark=True),
    dict(bg='#f0f9ff', surface='#ffffff', text='#0c2536', muted='#6b8799', primary='#0284c7', accent='#38bdf8', hero='#082f49', dark=True),
    dict(bg='#f5f3ff', surface='#ffffff', text='#1e1b4b', muted='#7c7a99', primary='#7c3aed', accent='#c026d3', hero='#1e1b4b', dark=True),
    dict(bg='#ecfeff', surface='#ffffff', text='#042f2e', muted='#64898a', primary='#14b8a6', accent='#0e7490', hero='#042f2e', dark=True),
    dict(bg='#fefce8', surface='#ffffff', text='#3a3410', muted='#93884f', primary='#ca8a04', accent='#dc2626', hero='#3f2d05', dark=True),
    dict(bg='#f8fafc', surface='#ffffff', text='#0f172a', muted='#64748b', primary='#0ea5e9', accent='#f43f5e', hero='#0f172a', dark=True),
    dict(bg='#fafafa', surface='#ffffff', text='#111111', muted='#6b6b6b', primary='#dc2626', accent='#111111', hero='#ffffff', dark=False),
    dict(bg='#eef2ff', surface='#ffffff', text='#1e1b4b', muted='#6d6f92', primary='#4f46e5', accent='#06b6d4', hero='#312e81', dark=True),
    dict(bg='#fdf4ff', surface='#ffffff', text='#2e102e', muted='#96608f', primary='#c026d3', accent='#db2777', hero='#3b0f34', dark=True),
]

# ---------- шрифты (head, body) ----------
FONTS = [
    ('Unbounded', 'Manrope'),
    ('Russo One', 'Rubik'),
    ('Playfair Display', 'Nunito Sans'),
    ('Oswald', 'Open Sans'),
    ('Merriweather', 'Lato'),
    ('Montserrat', 'Montserrat'),
    ('Exo 2', 'Comfortaa'),
    ('Comfortaa', 'PT Sans'),
    ('PT Serif', 'PT Sans'),
    ('Righteous', 'Jost'),
]

# ---------- hero-макеты и motion ----------
HERO_LAYOUTS = ['centered', 'split', 'bigtype', 'bento', 'compact']
MOTIONS = ['reveal', 'counters', 'marquee', 'blobs', 'gradtext', 'tilt', 'pulse', 'reveal_cards']


def fmt_price(n):
    return '{:,}'.format(n).replace(',', ' ')


def build_page(idx, name, palette, font, hero_layout, motion, price):
    price1, price5 = price
    head, body = font
    p = palette
    dark_hero = p['dark']
    p1s = fmt_price(price1)
    p5s = fmt_price(price5)
    old5 = fmt_price(5 * price1)
    if 5 * price1 > price5:
        saving_line = 'вместо %s ₽ (экономия %s ₽)' % (old5, fmt_price(5 * price1 - price5))
    else:
        saving_line = 'выгодно при покупке пакетом'

    use_marquee = 'marquee' in motion
    use_blobs = 'blobs' in motion
    use_counters = 'counters' in motion
    use_tilt = 'tilt' in motion
    use_pulse = 'pulse' in motion
    use_grad = 'gradtext' in motion
    reveal_mode = 'reveal' in motion or 'reveal_cards' in motion

    # ---------- motion css ----------
    mcss = []
    def mc(tpl):
        return tpl.replace('__PRIMARY__', p['primary']).replace('__ACCENT__', p['accent'])
    if use_marquee:
        mcss.append(mc("""
.marquee{display:block;overflow:hidden;white-space:nowrap;background:linear-gradient(90deg,__PRIMARY__,__ACCENT__);color:#fff;padding:14px 0;font-weight:600}
.marquee span{display:inline-block;padding-right:4px;animation:scrollX 30s linear infinite}
@keyframes scrollX{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
"""))
    if use_blobs:
        mcss.append(mc("""
.hero{position:relative;overflow:hidden}
.hero .blob{position:absolute;border-radius:50%;filter:blur(90px);opacity:.5;pointer-events:none;z-index:0}
.hero .blob.b1{width:560px;height:560px;background:radial-gradient(circle,__ACCENT__,transparent 70%);top:-180px;right:-140px;animation:blob1 18s ease-in-out infinite}
.hero .blob.b2{width:520px;height:520px;background:radial-gradient(circle,__PRIMARY__,transparent 70%);bottom:-200px;left:-140px;animation:blob2 24s ease-in-out infinite}
@keyframes blob1{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(-70px,50px) scale(1.18)}}
@keyframes blob2{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(60px,-50px) scale(1.12)}}
"""))
    if use_counters:
        mcss.append('.num{font-variant-numeric:tabular-nums}')
    if use_grad:
        mcss.append(mc("""
.hero h1 em{background:linear-gradient(90deg,__PRIMARY__,__ACCENT__,__PRIMARY__);background-size:200% 200%;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:gradShift 6s ease-in-out infinite;font-style:normal}
@keyframes gradShift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
"""))
    if use_tilt:
        mcss.append('.tilt{transition:transform .25s ease;will-change:transform}')
    if use_pulse:
        mcss.append("""
.cta{animation:pulseG 3.2s ease-in-out infinite}
@keyframes pulseG{0%,100%{box-shadow:0 10px 30px rgba(0,0,0,.2)}50%{box-shadow:0 10px 45px rgba(0,0,0,.35)}}
""")
    if reveal_mode:
        mcss.append("""
.js .rv{opacity:0;transform:translateY(26px);transition:opacity .6s ease,transform .6s ease}
.js .rv.in{opacity:1;transform:none}
.js .crd:nth-child(2){transition-delay:.08s}.js .crd:nth-child(3){transition-delay:.16s}.js .crd:nth-child(4){transition-delay:.24s}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}.js .rv{opacity:1;transform:none}}
""")

    # ---------- layout css ----------
    if hero_layout == 'split':
        lcss = """
.hero{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:130px 40px 80px}
.hero .hwrap{position:relative;z-index:2}
.hero h1{font-size:clamp(34px,4.6vw,54px);line-height:1.1}
.hero .side{position:relative;z-index:2;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-radius:24px;padding:28px;backdrop-filter:blur(8px)}
.hero .side h3{margin-bottom:14px;font-size:20px}
.hero .side ul{list-style:none}
.hero .side li{padding:9px 0 9px 26px;position:relative;opacity:.95}
.hero .side li:before{content:"\\2713";position:absolute;left:0;color:%s;font-weight:700}
.hero-points{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:34px}
.point{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:14px;padding:16px}
.point b{display:block;font-size:18px;margin-bottom:3px}
.point span{font-size:13px;opacity:.85}
""" % p['accent']
    elif hero_layout == 'bigtype':
        lcss = """
.hero{display:flex;flex-direction:column;align-items:flex-start;justify-content:center;min-height:88vh;padding:130px 40px 80px}
.hero .hwrap{position:relative;z-index:2;max-width:1000px}
.hero .badge{letter-spacing:.14em;text-transform:uppercase;font-size:13px}
.hero h1{font-size:clamp(44px,8vw,96px);line-height:.98;font-weight:800}
.hero h1 em{display:block}
.hero p{font-size:clamp(17px,2.2vw,24px);max-width:640px;margin-top:18px}
.hero-points{display:flex;gap:34px;flex-wrap:wrap;margin-top:44px}
.point b{display:block;font-size:30px}
.point span{font-size:14px;opacity:.8}
"""
    elif hero_layout == 'bento':
        lcss = """
.hero{padding:130px 40px 80px;display:grid;grid-template-columns:1.4fr 1fr;gap:26px;align-items:center}
.hero .hwrap{position:relative;z-index:2}
.hero h1{font-size:clamp(34px,4.4vw,52px);line-height:1.08}
.hero-points{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.point{background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.18);border-radius:18px;padding:20px}
.point:first-child{grid-column:1/-1;background:linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.05))}
.point b{display:block;font-size:22px;margin-bottom:4px}
.point span{font-size:13px;opacity:.85}
"""
    elif hero_layout == 'compact':
        lcss = """
.hero{padding:120px 40px 60px;max-width:1000px}
.hero .hwrap{position:relative;z-index:2}
.hero h1{font-size:clamp(32px,4vw,46px);line-height:1.12}
.hero-points{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:14px;margin-top:30px}
.point{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:12px;padding:14px 18px}
.point b{display:block;font-size:17px}
.point span{font-size:13px;opacity:.85}
"""
    else:  # centered
        lcss = """
.hero{display:flex;flex-direction:column;align-items:center;text-align:center;padding:130px 20px 80px}
.hero .hwrap{max-width:900px}
.hero h1{font-size:clamp(38px,5.4vw,62px);line-height:1.08}
.hero-points{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px;max-width:900px;margin-top:40px;width:100%}
.point{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:16px;padding:18px 22px}
.point b{display:block;font-size:20px;margin-bottom:4px}
.point span{font-size:14px;opacity:.85}
"""

    # ---------- base css ----------
    css = """
:root{--bg:%s;--surface:%s;--text:%s;--muted:%s;--primary:%s;--accent:%s}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'%s',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden}
h1,h2,h3,h4{font-family:'%s',sans-serif;line-height:1.15}
a{text-decoration:none;color:inherit}
.nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;justify-content:space-between;align-items:center;padding:16px 40px;background:rgba(255,255,255,.9);backdrop-filter:blur(10px);box-shadow:0 2px 18px rgba(0,0,0,.07)}
.nav .logo{font-family:'%s',sans-serif;font-weight:800;font-size:21px;color:var(--primary)}
.nav .links{display:flex;gap:26px;align-items:center}
.nav .links a{color:#475569;font-weight:500}
.nav .links a:hover{color:var(--primary)}
.nav .cta{background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff!important;padding:9px 20px;border-radius:50px;font-weight:600}
.hero{background:%s;color:%s}
.hero h1{margin-bottom:22px}
.badge{display:inline-block;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.2);padding:8px 20px;border-radius:50px;font-size:13px;margin-bottom:22px}
.hero p{opacity:.94}
.hero-cta{display:flex;gap:16px;flex-wrap:wrap;margin-top:26px}
.btn{padding:15px 30px;border-radius:50px;font-weight:600;display:inline-block;font-size:16px;border:none;cursor:pointer}
.btn.primary{background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff}
.btn.ghost{background:rgba(255,255,255,.14);color:inherit;border:1px solid rgba(255,255,255,.3)}
section{padding:76px 40px;max-width:1200px;margin:0 auto}
.sec-title{font-size:36px;text-align:center;margin-bottom:14px}
.sec-sub{font-size:17px;color:var(--muted);text-align:center;margin-bottom:44px}
.catalog{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:26px}
.card{background:var(--surface);border:1px solid #e2e8f0;border-radius:20px;padding:26px;display:flex;flex-direction:column;box-shadow:0 4px 18px rgba(0,0,0,.05)}
.card .code{align-self:flex-start;background:#eef2ff;color:#4f46e5;font-size:12px;font-weight:600;padding:5px 12px;border-radius:50px;margin-bottom:12px}
.card h3{font-size:22px;margin-bottom:10px}
.card .status{align-self:flex-start;font-size:12px;padding:4px 12px;border-radius:50px;margin-bottom:14px;background:#dcfce7;color:#15803d}
.card ul{list-style:none;margin-bottom:16px;font-size:15px;color:#475569}
.card ul li{padding:5px 0 5px 24px;position:relative}
.card ul li:before{content:"\\2713";position:absolute;left:0;color:#16a34a;font-weight:700}
.card .row{margin-top:auto;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #e2e8f0;padding-top:16px}
.card .price{font-size:26px;font-weight:800;color:var(--primary)}
.card .pick{background:var(--primary);color:#fff;border:none;padding:10px 18px;border-radius:50px;font-weight:600;cursor:pointer}
.bundle{background:linear-gradient(135deg,var(--primary),var(--accent));border-radius:28px;color:#fff;padding:48px;display:flex;gap:36px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.bundle h3{font-size:30px;margin-bottom:10px}
.bundle ul{list-style:none;margin-top:8px}
.bundle li{padding:4px 0;opacity:.93}
.bprice{font-size:44px;font-weight:800}
.bprice small{font-size:16px;opacity:.85;display:block;font-weight:400}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:24px}
.step{background:var(--surface);border:1px solid #e2e8f0;border-radius:18px;padding:26px;position:relative}
.step .n{position:absolute;top:-18px;left:22px;width:42px;height:42px;border-radius:50%%;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;font-weight:800;font-size:19px;display:flex;align-items:center;justify-content:center}
.step h4{margin:12px 0 8px}
.step p{font-size:15px;color:#475569}
.form-wrap{background:var(--surface);border-radius:26px;box-shadow:0 10px 40px rgba(0,0,0,.08);padding:44px;max-width:740px;margin:0 auto}
.form-wrap h3{font-size:28px;text-align:center;margin-bottom:8px}
.form-wrap .sub{color:var(--muted);text-align:center;margin-bottom:26px}
.tb{background:#f8fafc;border:1px solid #e2e8f0;border-radius:14px;padding:18px;margin-bottom:16px}
.tb h4{margin-bottom:4px}
.tb h4 span{font-size:13px;color:var(--muted);font-weight:500}
label{font-size:14px;font-weight:600;color:#334155;display:block;margin:10px 0 6px}
input,textarea{width:100%%;padding:12px 14px;border:1.5px solid #e2e8f0;border-radius:10px;font-size:15px;font-family:inherit}
input:focus,textarea:focus{outline:none;border-color:var(--primary)}
.rrow{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.btn-sub{width:100%%;text-align:center;margin-top:8px}
.hint{font-size:13px;color:var(--muted);margin-top:12px}
.faq{max-width:820px;margin:0 auto}
.faq-item{background:var(--surface);border:1px solid #e2e8f0;border-radius:14px;margin-bottom:12px;overflow:hidden}
.faq-item summary{padding:18px 22px;font-weight:600;cursor:pointer;list-style:none}
.faq-item p{padding:0 22px 18px;color:#475569}
footer{background:%s;color:#94a3b8;padding:46px 40px;text-align:center}
footer b{color:#fff}
.msg{display:none;text-align:center;padding:14px;border-radius:12px;margin-top:14px;font-weight:600}
.msg.ok{background:#dcfce7;color:#15803d}
.msg.err{background:#fee2e2;color:#b91c1c}
@media(max-width:768px){.nav{padding:12px 18px}.nav .links{display:none}section{padding:56px 18px}.rrow{grid-template-columns:1fr}.hero{padding:110px 18px 60px}}
""" % (p['bg'], p['surface'], p['text'], p['muted'], p['primary'], p['accent'],
       body, head, head, p['hero'], ('#fff' if dark_hero else '#0f172a'), p['hero'])
    css += ''.join(mcss) + lcss

    # ---------- контент ----------
    badge = 'Для учебных центров · соответствует Приказу № 534 и Приказу № 266'
    if use_grad:
        h1_inner = 'Готовые комплекты <em>образовательных программ</em> для учебных центров'
    else:
        h1_inner = 'Готовые комплекты образовательных программ для учебных центров'
    hero_p = ('Полный пакет материалов и документов по профессии: Программа ПО, Методическое пособие, '
              'Методичка «вопросы-ответы», Контрольно-оценочные материалы, плакаты и Тесты. '
              'Всё создаётся конкретно под вашу организацию. Автовыдача файлов после оплаты.')

    num_cls = ' class="num"' if use_counters else ''
    points = ''.join(
        '<div class="point"><b%s>%s</b><span>%s</span></div>' % (num_cls, a, b)
        for a, b in [('5 000+ профессий', 'по Перечню Приказа № 534'),
                     ('ПО · ДПО · ДО · Курсы', 'все виды обучения'),
                     (p1s + ' ₽', 'комплект, от ' + p5s + ' ₽ пакет из 5'),
                     ('Автовыдача', 'файлы после оплаты на e-mail')])

    side_html = ''
    if hero_layout in ('split', 'bento'):
        side_html = """<div class="side">
  <h3>Что входит в комплект</h3>
  <ul>
    <li>Программа профессионального обучения</li>
    <li>Методическое пособие</li>
    <li>Методичка «вопросы-ответы»</li>
    <li>Контрольно-оценочные материалы</li>
    <li>Плакаты и тест для экзамена</li>
  </ul>
</div>"""

    marquee_html = ''
    if use_marquee:
        profs = ['Стропальщик', 'Машинист крана', 'Водитель погрузчика', 'Машинист экскаватора',
                 'Машинист бульдозера', 'Весовщик', 'Машинист автогрейдера', 'Машинист катка',
                 'Аппаратчик-гидрометаллург']
        band = ' · '.join(profs) + ' · '
        marquee_html = '<div class="marquee"><span>%s%s</span></div>' % (band * 2, band * 2)

    hero = '<div class="hero">%s<div class="hwrap"><div class="badge">%s</div><h1>%s</h1><p>%s</p>' \
           '<div class="hero-cta"><a href="#form" class="btn primary cta">Заказать комплект</a>' \
           '<a href="#catalog" class="btn ghost">Смотреть каталог</a></div><div class="hero-points">%s</div></div>%s</div>' % (
               ('<div class="blob b1"></div><div class="blob b2"></div>' if use_blobs else ''),
               badge, h1_inner, hero_p, points, side_html)

    cards = []
    for code, title, status, docs, typ in [
            ('Профессиональное обучение', 'ПО', '5 100+ профессий по Приказу № 534',
             ['Подготовка / переподготовка / повышение квалификации рабочих', 'Программа ПО, методическое пособие, КОМ, тесты', 'Любая профессия из Перечня № 534'], 'ПО'),
            ('Дополнительное профессиональное образование', 'ДПО', 'Под заказ',
             ['Профессиональная переподготовка', 'Повышение квалификации специалистов', 'По актуальным требованиям (Приказ № 266)'], 'ДПО'),
            ('Дополнительное образование', 'ДО', 'Под заказ',
             ['Дополнительные общеразвивающие программы', 'Дополнительные предпрофессиональные программы', 'Для детей и взрослых'], 'ДО'),
            ('Курсы', 'Курсы', 'Под заказ',
             ['Краткосрочные обучающие курсы', 'Семинары, тренинги, стажировки', 'Технический минимум и другие направления'], 'Курсы')]:
        li = ''.join('<li>%s</li>' % d for d in docs)
        cards.append('<div class="card crd%s"><span class="code">%s</span><h3>%s</h3>'
                     '<span class="status">%s</span><ul>%s</ul><div class="row">'
                     '<div class="price">от %s ₽</div><button class="pick" data-t="%s">Выбрать</button>'
                     '</div></div>' % (' tilt' if use_tilt else '', code, title, status, li, p1s, typ))
    cards_html = ''.join(cards)

    steps_html = ''.join(
        '<div class="step"><div class="n">%d</div><h4>%s</h4><p>%s</p></div>' % (i + 1, a, b)
        for i, (a, b) in enumerate([('Заявка', 'Выбираете виды обучения, нужные направления и заполняете форму: название организации, ИНН, e-mail.'),
                                    ('Оплата', 'Счёт для юрлица или оплата картой онлайн. Автоматическое подтверждение на e-mail.'),
                                    ('Автовыдача', 'После оплаты получаете ссылку на скачивание комплекта файлов (Яндекс.Диск).'),
                                    ('Адаптация', 'Комплект выдаётся с титульными данными под вашу организацию. Готов к лицензированию.')]))

    faq_html = ''.join('<details class="faq-item"><summary>%s</summary><p>%s</p></details>' % (q, a)
                       for q, a in [('Что входит в комплект?', 'Программа профессионального обучения (ПО) нужной длительности, методическое пособие, методичка в формате «вопросы-ответы», контрольно-оценочные материалы, плакаты и тест для экзамена.'),
                                    ('Программы соответствуют требованиям?', 'Да. Программы построены по Перечню профессий рабочих (Приказ Минпросвещения № 534), с учётом норм Закона «Об образовании» (273-ФЗ) и правил организации профобучения. Для ДПО — актуальная редакция Порядка (Приказ Минобрнауки № 266).'),
                                    ('Как получить файлы?', 'После оплаты на ваш e-mail автоматически приходит письмо со ссылкой на скачивание комплекта. Ссылка доступна 7 дней.'),
                                    ('Можно ли по безналу для юрлица?', 'Да. Выставляем счёт на ООО «КВАНТ+». После поступления оплаты высылаем файлы и закрывающие документы.'),
                                    ('Нужной профессии нет в каталоге?', 'Сделаем комплект под заказ по любой профессии из Приказа № 534 за 1–2 дня. Укажите её в комментарии к заявке.')])

    sec = {
        'catalog': '<section id="catalog" class="rv"><h2 class="sec-title">Что мы готовим</h2>'
                   '<p class="sec-sub">Готовые комплекты документов под все виды обучения: ПО, ДПО, ДО и курсы.</p>'
                   '<div class="catalog">%s</div></section>' % cards_html,
        'form': ('<section id="form" class="rv"><div class="form-wrap"><h3>Заявка на комплекты программ</h3>'
                 '<p class="sub">Выберите виды обучения и укажите нужные направления — пришлём счёт и комплекты на e-mail. '
                 'Вопросы по телефону %s.</p><form id="orderForm">'
                 '<div class="tb"><h4>ПО <span>Профессиональное обучение</span></h4>'
                 '<label>Название (профессия, должность, направление)</label>'
                 '<input type="text" data-blk="ПО" placeholder="Например: Стропальщик, 80 часов">'
                 '<div class="hint">Выбор из Перечня Приказа № 534 (5 100+ профессий) — просто укажите профессию.</div></div>'
                 '<div class="tb"><h4>ДПО <span>Дополнительное проф. образование</span></h4>'
                 '<label>Название</label><input type="text" data-blk="ДПО" placeholder="Повышение квалификации специалиста по охране труда"></div>'
                 '<div class="tb"><h4>ДО <span>Дополнительное образование</span></h4>'
                 '<label>Название</label><input type="text" data-blk="ДО" placeholder="Дополнительная общеразвивающая программа"></div>'
                 '<div class="tb"><h4>Курсы</h4><label>Название</label>'
                 '<input type="text" data-blk="Курсы" placeholder="Технический минимум, семинар, тренинг"></div>'
                 '<div class="rrow"><div><label>Организация *</label><input type="text" id="org" required placeholder="ООО «Учебный центр»"></div>'
                 '<div><label>E-mail *</label><input type="email" id="email" required placeholder="mail@centr.ru"></div></div>'
                 '<div class="rrow"><div><label>ИНН</label><input type="text" id="inn" placeholder="1234567890"></div>'
                 '<div><label>Контактное лицо</label><input type="text" id="contact" placeholder="ФИО"></div></div>'
                 '<label>Комментарий</label><textarea id="comment" rows="3" placeholder="Дополнительные пожелания, объём часов, документы для лицензирования"></textarea>'
                 '<button type="submit" class="btn primary btn-sub">Отправить заявку</button>'
                 '<div class="msg" id="msg"></div><p class="hint">Отправляя форму, вы соглашаетесь с обработкой персональных данных.</p>'
                 '</form></div></section>') % PHONE,
        'pricing': '<section id="pricing" class="rv"><div class="bundle"><div><h3>Пакет «Старт учебного центра» — 5 комплектов</h3>'
                   '<p>Любые 5 комплектов программ (ПО, ДПО, ДО или курсы) — самый ходовой набор для лицензирования и запуска обучения.</p>'
                   '<ul><li>5 комплектов на выбор</li><li>Все виды обучения: ПО, ДПО, ДО, курсы</li><li>Под вашу организацию</li></ul></div>'
                   '<div style="text-align:right"><div class="bprice">%s ₽ <small>%s</small></div>'
                   '<a href="#form" class="btn primary cta" style="margin-top:18px">Заказать пакет</a></div></div></section>' % (p5s, saving_line),
        'how': '<section id="how" class="rv"><h2 class="sec-title">Как это работает</h2>'
               '<p class="sec-sub">Всё по письменной заявке — пришлём счёт и комплекты на e-mail, ответим на вопросы по телефону</p>'
               '<div class="steps">%s</div></section>' % steps_html,
        'faq': '<section id="faq" class="rv"><h2 class="sec-title">Частые вопросы</h2><div class="faq">%s</div></section>' % faq_html,
    }
    order = ['catalog', 'form', 'pricing', 'how', 'faq']
    if idx % 3 == 1:
        order = ['form', 'catalog', 'how', 'pricing', 'faq']
    elif idx % 3 == 2:
        order = ['how', 'catalog', 'form', 'faq', 'pricing']
    body_sections = ''.join(sec[k] for k in order)

    # ---------- js ----------
    js = "document.documentElement.classList.add('js');\n"
    if reveal_mode:
        js += ("(function(){if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){"
               "es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}});},"
               "{threshold:.15});document.querySelectorAll('.rv').forEach(function(el){io.observe(el);});}else{"
               "document.querySelectorAll('.rv').forEach(function(el){el.classList.add('in');});}})();\n")
    if use_counters:
        js += ("(function(){var els=document.querySelectorAll('.num');if(!els.length)return;"
               "function fmt(n){return n.toLocaleString('ru-RU');}"
               "function run(el){var t=el.textContent,m=t.match(/^(\\d[\\d\\s]*\\d|\\d)([\\s\\u20bd+\\-\\u2013\\u2014].*)?$/);"
               "if(!m)return;var target=parseInt(m[1].replace(/\\s/g,''),10),suf=m[2]||'',d=1100,t0=performance.now();"
               "function st(tm){var p=Math.min((tm-t0)/d,1),e=1-Math.pow(1-p,3);el.textContent=fmt(Math.round(target*e))+suf;"
               "if(p<1)requestAnimationFrame(st);}requestAnimationFrame(st);"
               "setTimeout(function(){el.textContent=fmt(target)+suf;},d+120);}"
               "if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){"
               "es.forEach(function(en){if(en.isIntersecting){run(en.target);io.unobserve(en.target);}});},{threshold:.4});"
               "els.forEach(function(c){io.observe(c);});}else{els.forEach(run);}})();\n")
    if use_tilt:
        js += ("(function(){var cards=document.querySelectorAll('.tilt');cards.forEach(function(c){"
               "c.addEventListener('mousemove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,"
               "y=(e.clientY-r.top)/r.height-.5;c.style.transform='perspective(700px) rotateY('+(x*7)+'deg) rotateX('+(-y*7)+'deg)';});"
               "c.addEventListener('mouseleave',function(){c.style.transform='';});});})();\n")
    js += ("(function(){var nav=document.querySelector('.nav'),s=false;function f(){var n=window.scrollY>60;"
           "if(n!==s){s=n;nav.classList.toggle('scrolled',n);}}window.addEventListener('scroll',f,{passive:true});f();})();\n"
           "document.getElementById('orderForm').addEventListener('submit',function(e){e.preventDefault();"
           "var org=document.getElementById('org').value.trim(),email=document.getElementById('email').value.trim(),"
           "msg=document.getElementById('msg');"
           "if(!org||!email){msg.className='msg err';msg.textContent='Заполните обязательные поля: организация и e-mail.';"
           "msg.style.display='block';return;}"
           "var blocks=[];document.querySelectorAll('input[data-blk]').forEach(function(i){var v=i.value.trim();"
           "if(v)blocks.push(i.getAttribute('data-blk')+': '+v);});"
           "var comment='Сайт: %s'+(document.getElementById('comment').value.trim()?"
           "('\\n'+document.getElementById('comment').value.trim()):'');"
           "var vals={org:org,email:email,inn:document.getElementById('inn').value.trim(),"
           "contact:document.getElementById('contact').value.trim(),phone:'',comment:comment,"
           "po:blocks.filter(function(b){return b.indexOf('ПО:')===0;}).join('; '),"
           "dpo:blocks.filter(function(b){return b.indexOf('ДПО:')===0;}).join('; '),"
           "'do':blocks.filter(function(b){return b.indexOf('ДО:')===0;}).join('; '),"
           "courses:blocks.filter(function(b){return b.indexOf('Курсы:')===0;}).join('; ')};"
           "var f=document.createElement('form');f.method='POST';f.action='%s';f.style.display='none';"
           "Object.keys(vals).forEach(function(k){var i=document.createElement('input');i.type='hidden';"
           "i.name=k;i.value=vals[k];f.appendChild(i);});document.body.appendChild(f);f.submit();"
           "msg.className='msg ok';msg.textContent='Заявка отправлена! Пришлём счёт и ссылку на оплату на указанный e-mail.';"
           "msg.style.display='block';e.target.reset();return false;});\n") % (name, FORM_ENDPOINT)

    html = ('<!DOCTYPE html>\n<html lang="ru"><head>\n<meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>%s — готовые образовательные программы для учебных центров</title>\n'
            '<meta name="description" content="Готовые комплекты образовательных программ по Приказу № 534: '
            'программа ПО, методичка, тесты, КОМ. От %s ₽. Автовыдача после оплаты.">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link href="https://fonts.googleapis.com/css2?family=%s:wght@400;600;700;800&family=%s:wght@400;500;600;700&display=swap" rel="stylesheet">\n'
            '<style>%s</style>\n</head><body>\n'
            '<div class="nav"><div class="logo">%s</div><div class="links">'
            '<a href="#catalog">Каталог</a><a href="#how">Как это работает</a>'
            '<a href="#pricing">Цены</a><a href="#faq">FAQ</a>'
            '<a class="cta" href="#form">Оставить заявку</a></div></div>\n'
            '%s%s\n%s\n'
            '<footer><b>%s</b> — готовые комплекты образовательных программ для учебных центров<br><br>'
            'Продавец: %s<br>%s<br><br>© 2026 %s. Все права защищены.</footer>\n'
            '<script>%s</script>\n</body></html>' % (
                name, p1s, head.replace(' ', '+'), body.replace(' ', '+'), css,
                name, marquee_html, hero, body_sections, name, SELLER, ADDR, name, js))
    return html


def main():
    if os.path.exists(OUT_DIR):
        import shutil
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR)
    for i in range(100):
        pal = PALETTES[(i * 7) % len(PALETTES)]
        font = FONTS[(i * 5) % len(FONTS)]
        layout = HERO_LAYOUTS[(i * 3) % len(HERO_LAYOUTS)]
        mot = MOTIONS[(i * 11) % len(MOTIONS)]
        price = PRICES[(i * 13) % len(PRICES)]
        name = NAMES[i]
        folder = os.path.join(OUT_DIR, 'site-%03d' % (i + 1))
        os.makedirs(folder)
        html = build_page(i, name, pal, font, layout, mot, price)
        with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print('%03d %-24s layout=%-9s font=%-18s motion=%-13s price=%s/%s' % (
            i + 1, name, layout, font[0], mot, price[0], price[1]))


if __name__ == '__main__':
    main()
