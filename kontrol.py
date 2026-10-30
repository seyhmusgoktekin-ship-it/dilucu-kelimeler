"""gunluk.json'u denetler: JSON geçerli mi, alanlar tam mı, hl örnekte geçiyor mu."""
import datetime
import json
import sys

items = json.load(open("gunluk.json", encoding="utf-8"))["items"]
errors = []
seen = set()
for n, e in enumerate(items, 1):
    where = f"{n}. girdi ({e.get('en', '?')})"
    try:
        datetime.date.fromisoformat(e["date"])
    except (KeyError, ValueError):
        errors.append(f"{where}: date yok ya da YYYY-AA-GG değil")
    if (e.get("date"), e.get("en")) in seen:
        errors.append(f"{where}: aynı gün iki kez")
    seen.add((e.get("date"), e.get("en")))
    if e.get("kind") not in ("word", "phrase", "sentence"):
        errors.append(f"{where}: kind geçersiz")
    if e.get("tone", "neutral") not in ("neutral", "informal", "slang"):
        errors.append(f"{where}: tone geçersiz")
    for s in e.get("senses") or [None]:
        if not s or not s.get("tr"):
            errors.append(f"{where}: Türkçe anlam (tr) yok")
        elif s.get("hl") and s["hl"] not in s.get("example", ""):
            errors.append(f"{where}: hl örnek cümlede geçmiyor")
print("\n".join(errors) or f"Tamam: {len(items)} girdi.")
sys.exit(1 if errors else 0)
