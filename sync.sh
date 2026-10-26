#!/bin/sh
# dogusportal danisman.html'i alip ozlemvarol.com icin index.html uretir:
# Veri: teslim-duyuru.html yenifikirtepeburada.com/teslim-takvimi.json'u okur.
# assets/data yollari dogusportal.com'a cevrilir, varsayilan danisman ozlem_varol olur.
curl -fsSL https://dogusportal.com/danisman.html \
 | sed -e "s#\([(\"'\`]\)\(assets\|data\)/#\1https://dogusportal.com/\2/#g" \
       -e "s#q.get('id')||''#q.get('id')||'ozlem_varol'#" \
       -e 's#<meta name="robots" content="noindex">#<link rel="canonical" href="https://ozlemvarol.com/">#' \
       -e 's#<title>Danışman · RE/MAX Doğuş</title>#<title>Özlem Varol · RE/MAX Doğuş Gayrimenkul Danışmanı</title>#' \
       -e 's#content="RE/MAX Doğuş gayrimenkul danışmanı"#content="Özlem Varol, RE/MAX Doğuş gayrimenkul danışmanı. Fikirtepe ve Kadıköy’de satılık ve kiralık konut."#' > index.tmp
# 13. Etap teslim duyurusu (geri sayimli, yenifikirtepeburada.com'dan uyarlandi): </body> oncesine eklenir
awk 'FNR==NR{d=d $0 "\n";next} /<\/body>/{printf "%s", d} {print}' teslim-duyuru.html index.tmp > index.html && rm index.tmp
