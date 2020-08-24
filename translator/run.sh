#/bin/bash

. ~/Desktop/Project/venv/bin/activate
# Rank https://medium.com/@ChannelMeter/youtubes-top-countries-47b0d26dded
# USA< india, UK, Brazil, Thailand, Russia, South Korea, Spain, Japan, Canda, Turkey, Mexico, Vietnam, Germany, France, Argetina, Indonesia, Philippines, Colobia, Italy, Netherlands, Ukraine, Saudi Arabia, Romania
# Vietnam, Egypt, Chile,

# 네덜란드어, 일본어, 영어, 한국어, 라틴어, 러시아어, 베트남어, 스페인어, 아랍어, 이탈리아어, 필리핀어, 인도네시아어, 프랑스어, 포루투갈어, 포루투갈어(브라질), 말레이어, 스웨덴어, 태국어, 아이슬란드어, 헝가리어

# ar 아랍어
# af 아프리카공용어
# pt 브라질
# tl 필리핀어

echo $1
LANG=af,ar,nl,en,tl,fr,de,el,hu,is,id,it,ja,ko,ms,la,pt,ru,es,sv,th,tr,uk,vi,tl
# LANG="af"
echo $LANG
# echo $2

python srt_translator.py --input ./data/$1/$1_SRT_Korean.srt --lang $LANG
python tnd_translator.py --input ./data/$1/tnd --lang $LANG
rm eng.srt
