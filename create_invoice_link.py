import json, getpass, urllib.parse, urllib.request

print("Створення місячної Premium-підписки Telegram Stars")
token = getpass.getpass("Вставте токен бота (він не зберігається): ").strip()
stars = input("Ціна в Stars [10]: ").strip() or "10"
if not stars.isdigit() or not (1 <= int(stars) <= 10000):
    raise SystemExit("Ціна має бути цілим числом від 1 до 10000 Stars.")
url = f"https://api.telegram.org/bot{token}/createInvoiceLink"
data = {
    "title": "ПРОСТІР — Преміум",
    "description": "Необмежені практичні поради у Mini App протягом 30 днів.",
    "payload": "prostir_premium_monthly",
    "currency": "XTR",
    "prices": json.dumps([{"label": "Преміум на 30 днів", "amount": int(stars)}], ensure_ascii=False),
    "subscription_period": 2592000,
}
req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(), method="POST")
with urllib.request.urlopen(req) as r:
    result = json.load(r)
if not result.get("ok"):
    raise SystemExit(json.dumps(result, ensure_ascii=False, indent=2))
print("\nГотове invoice-посилання:\n")
print(result["result"])
print("\nСкопіюйте його у config.js → premiumInvoiceUrl")
