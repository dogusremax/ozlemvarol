#!/usr/bin/env python3
# yenifikirtepeburada.com/teslim-takvimi.html'i alip ozlemvarol.com/teslim-takvimi.html uretir:
# ust menu Ozlem Varol basligiyla degisir, WhatsApp numaralari Ozlem Hanim'in olur,
# veri ve gorseller yenifikirtepeburada.com'dan okunur. Calistir: python3 teslim-sync.py
import re, urllib.request

YF = 'https://yenifikirtepeburada.com/'
WA_OFIS, WA_OZLEM = 'wa.me/902163151515', 'wa.me/905336248598'

s = urllib.request.urlopen(YF + 'teslim-takvimi.html').read().decode('utf-8')

def degis(eski, yeni, adet=1):
    global s
    if s.count(eski) < adet:
        raise SystemExit('Kaynakta bulunamadi: ' + eski[:60])
    s = s.replace(eski, yeni)

# Baslik ve adresler
degis('<title>Teslim Takvimi | Yeni Fikirtepe Blok ve Daire Teslim Tarihleri</title>',
      '<title>Teslim Takvimi · Yeni Fikirtepe | Özlem Varol, RE/MAX Doğuş</title>')
s = s.replace(YF + 'teslim-takvimi.html', 'https://ozlemvarol.com/teslim-takvimi.html')
degis('<meta property="og:site_name" content="Yeni Fikirtepe">', '<meta property="og:site_name" content="Özlem Varol">')

# Fikirtepe sitesinin analitik, dil ve telif betikleri alinmaz
s = re.sub(r'<!-- Google tag \(gtag.js\) -->\s*<script src="cerez.js"[^>]*></script>\s*<script>.*?</script>\s*<script src="dil.js"></script>',
           '', s, count=1, flags=re.S)
s = s.replace('<script src="telif.js" defer></script>', '')

# Ust menu yerine Ozlem Varol basligi
s, n = re.subn(r'<div class="navbar">.*?</nav>\s*</div>', '''<header class="ov-ust"><a href="/" class="ov-marka"><img src="https://dogusportal.com/assets/dogus-logo.webp" width="83" height="30" alt="RE/MAX Doğuş" onerror="this.onerror=null;this.src='https://dogusportal.com/assets/dogus-logo.png'"><i></i><span>Özlem Varol</span></a><a href="/" class="ov-don">Ana sayfa</a></header>''', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Ust menu bulunamadi')
degis('</style>', '''  .ov-ust{position:relative;z-index:2;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px max(20px,calc((100% - 960px)/2 + 24px));background:#050A30}
  .ov-marka{display:flex;align-items:center;gap:14px;text-decoration:none;color:#fff;font-weight:700;font-size:1.05rem}
  .ov-marka img{height:30px;width:auto;display:block}
  .ov-marka i{width:1px;height:26px;background:rgba(255,255,255,.35)}
  .ov-don{color:#fff;text-decoration:none;font-size:.9rem;font-weight:500;opacity:.85;border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:6px 14px}
  .ov-don:hover{opacity:1}
</style>''')
degis('<a href="index.html" class="back">← Ana sayfa</a>', '<a href="/" class="back">← Özlem Varol</a>')
s = re.sub(r'<script>\s*// mobilde bir linke .*?</script>', '', s, count=1, flags=re.S)

# Fikirtepe sitesindeki sayfa ve veri yollari
for yol in ['favicon.png', 'balloon.png', 'kiralik-deger.html', 'vaziyet-plani.html', 'kat-planlari.html', 'etaplar.html']:
    s = s.replace('"' + yol, '"' + YF + yol)
degis("src='assets/vaziyet/", "src='" + YF + "assets/vaziyet/")
degis("fetch('teslim-takvimi.json", "fetch('" + YF + "teslim-takvimi.json")
s = re.sub(r'(href="https://yenifikirtepeburada\.com/[^"]+")(?! target)', r'\1 target="_blank" rel="noopener"', s)

# WhatsApp: ofis yerine Ozlem Hanim
s = s.replace(WA_OFIS, WA_OZLEM).replace('tel:+902163151515', 'tel:+905336248598')

open('teslim-takvimi.html', 'w', encoding='utf-8').write(s)
print('teslim-takvimi.html yazildi')
