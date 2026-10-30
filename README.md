# Dilucu: günün kelimeleri

Dilucu uygulaması bu depodaki `gunluk.json` dosyasını günde birkaç kez okur.

- Her girdinin `date` alanı vardır ("2026-10-31"). O gün gelmeden girdi uygulamada görünmez; yani ileriki günleri önceden ekleyebilirsin.
- Bugünün kelimeleri ana sayfadaki kartlarda en önde çıkar.
- Uygulama son indirdiği kopyayı saklar; internet yokken de çalışır.

## Kelime eklemek

`gunluk.json` içindeki `items` listesine yeni girdi ekle:

```json
{
 "date": "2026-11-01",
 "en": "spill the tea",
 "kind": "phrase",
 "tone": "slang",
 "senses": [{
   "tr": "dedikoduyu anlatmak",
   "pos": "idiom",
   "example": "Okay, spill the tea. What happened at the party?",
   "exampleTr": "Hadi anlat bakalım. Partide ne oldu?",
   "hl": "spill the tea"
 }],
 "alternatives": ["dish"],
 "note": "Kısa bir kullanım notu."
}
```

- `kind`: `word`, `phrase` ya da `sentence`
- `tone`: `neutral`, `informal` ya da `slang`
- `hl`: örnek cümlede vurgulanacak kısım; cümlede aynen geçmeli.

Göndermeden önce kontrol et:

```bash
python3 kontrol.py
```
