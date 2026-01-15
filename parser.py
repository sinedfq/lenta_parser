import requests
import json
import urllib.parse

# Перед проверкой необходимо обновить HEADER, подробнее про это написано в инструкции
HEADERS = {
    "Host": "lentochka.lenta.com",
    "Advertisingid": "004ced79-f42e-4a53-a39d-272ef3ff44c4",
    "Appsflyerid": "1768494810424-6799929508781337628",
    "Marketingpartnerkey": "mp30-5332b7f24ba54351047601d78f90dafbfd7fcc295f966d3af19aeb",
    "X-Mob-Sgm": "7a6c197eb996a8cc",
    "Deviceid": "A-2fd1d889-bf54-4439-8698-300b9c58657a",
    "Experiments": "exp_a_a.default,exp_address_intercom.test,...",  
    "Client": "android_16_5.26.1",
    "Localtime": "2026-01-16T00:11:26+07:00",
    "Sessiontoken": "251BBE1681EE9457CFF95D3899E8142E",
    "Adid": "4f68ec0b149cf280fa3bb926116ca870",
    "X-Retail-Brand": "lo",
    "App-Version": "5.26.1",
    "Timestamp": "1768497086",
    "Qrator-Token": "b6b8f508fcec32633ff9e831a86256ee",
    "Traceparent": "00-645262fb0230482299a4aa524d16ffc3-709f29ea23ff44cc-01",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "okhttp/4.10.0"
}

RAW_DATA = "request=%7B%22Body%22%3A%7B%22Count%22%3A100%2C%22GoodsCategoryId%22%3A%22201000001%22%2C%22IncludePreorder%22%3Atrue%2C%22Offset%22%3A0%2C%22OrderPreset%22%3A%22category-popular%22%2C%22Return%22%3A%7B%22AllProperties%22%3Atrue%7D%7D%2C%22Head%22%3A%7B%22ADID%22%3A%224f68ec0b149cf280fa3bb926116ca870%22%2C%22AdvertisingId%22%3A%22004ced79-f42e-4a53-a39d-272ef3ff44c4%22%2C%22AppsFlyerId%22%3A%221768494810424-6799929508781337628%22%2C%22Client%22%3A%22android_16_5.26.1%22%2C%22DeviceId%22%3A%22A-2fd1d889-bf54-4439-8698-300b9c58657a%22%2C%22Experiments%22%3A%22exp_a_a.default%2C...%22%2C%22MarketingPartnerKey%22%3A%22mp30-5332b7f24ba54351047601d78f90dafbfd7fcc295f966d3af19aeb%22%2C%22Method%22%3A%22GoodsItemSearch%22%2C%22RequestId%22%3A%220638a827953f45c980eecf5c39035f69%22%7D%7D"

# API мобильного приложения Лента
url = "https://lentochka.lenta.com/api/rest"
response = requests.post(url, headers=HEADERS, data=RAW_DATA)


if response.status_code != 200:
    print(f"❌ Ошибка: {response.status_code}")
    print(response.text[:500])
    exit()


try:
    data = response.json()
    items = data["Body"]["GoodsItemList"]
except (KeyError, json.JSONDecodeError) as e:
    print("❌ Не удалось распарсить ответ:", e)
    exit()

# Формируем словарь для дальнейшнего сохранения в JSON
products = []
for item in items:
    product = {
        "id": item.get("Id"),
        "наименование": item.get("Name", ""),
        "регулярная_цена": item.get("OldPrice") or item.get("Price"), # Если нет старой цены, то ставим актуальную 
        "промо_цена": item.get("Price"),                            
        "бренд": item.get("Brand", "")
    }
    products.append(product)

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"✅ Успешно сохранено {len(products)} товаров в products.json")