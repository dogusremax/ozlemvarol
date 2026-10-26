#!/bin/sh
# dogusportal danisman.html'i alip ozlemvarol.com icin index.html uretir:
# assets/data yollari dogusportal.com'a cevrilir, varsayilan danisman ozlem_varol olur.
curl -fsSL https://dogusportal.com/danisman.html \
 | sed -e "s#\([(\"'\`]\)\(assets\|data\)/#\1https://dogusportal.com/\2/#g" \
       -e "s#q.get('id')||''#q.get('id')||'ozlem_varol'#" \
       -e 's#<meta name="robots" content="noindex">#<link rel="canonical" href="https://ozlemvarol.com/">#' \
       -e 's#<title>Danışman · RE/MAX Doğuş</title>#<title>Özlem Varol · RE/MAX Doğuş Gayrimenkul Danışmanı</title>#' \
       -e 's#content="RE/MAX Doğuş gayrimenkul danışmanı"#content="Özlem Varol, RE/MAX Doğuş gayrimenkul danışmanı. Fikirtepe ve Kadıköy’de satılık ve kiralık konut."#' > index.tmp
# Etap teslim takvimi karti (teslim-takvimi.html, teslim-sync.py ile uretilir): Yeni Fikirtepe kartinin altina eklenir
awk 'FNR==NR{d=d $0 "\n";next} {print} /id="yfAc"/{printf "%s", d}' teslim-kart.html index.tmp > index.html && rm index.tmp
python3 teslim-sync.py
