<h1>Парсер мобильного приложения Лента Онлайн</h1>

<h3>Использованные для анализа технологии:</h3>

1. Burp Suite Community Edition
2. Приложение Лента Онлайн
3. Xiaomi 15T
4. Python
5. Requests

<h3>Burp Suite:</h3>

1. Заходим в приложение и переходим в раздел Proxy
2. Переходим в подраздел Proxy Settings
3. Устанавливаем Proxy listeners на All interfaces
   <img width="1475" height="937" alt="image" src="https://github.com/user-attachments/assets/8a7f266c-739d-4d72-8c5f-e2e7a8f897fd" />
4. Включаем прослушку прокси

<h3>Настройка Android: </h3>

1. Необходимо присоединиться к той же сети Wi-Fi, что и наш ПК
2. Перейдите в настройки сети Wi-Fi и вставьте локальный IP вашего компьютера с портом 8080 в пустые поля (для просмотра ip вашего ПК в cmd пропишите ipconfig)
3. После установки проксирования запросов зайдите в браузер на страницу http://burpsuite, там будет кнопка CA Certificate, нажмите на нее и установите сертификат через настройки
4. В случае Android (в моём случае) необходимо пропатчить приложение "Лента Онлайн":
5. В меню разработчика включите пункт "Отладка по USB" и "Установка по USB"
6. Необходимо получить APK приложения Лента Онлайн и переместить его на свой ПК
7. Прописать в PowerShell команду ```npx apk-mitm lenta.apk``` для получения пачнутой версии приложения (могут понадобиться дополнительные инстументы: [Andrioid ADB](https://developer.android.com/tools/releases/platform-tools?spm=a2ty_o01.29997173.0.0.5046517165S2nG&hl=ru)
и [Amazon Coretto для Windows](https://wingetgui.com/apps/Amazon-Corretto-11-JDK)
8. Установить новое приложение на смартфон ```.\adb install lenta-patched.apk``` (в случае если установка не прошла, необходимо удалить старое приложение)

<h3>Использование парсера:</h3>

1. Теперь запустить приложение и выбрать Категории -> Кошки -> Все товары категории
2. Из Burp Suite скопировать первый POST запрос, который получили при заходе на страницу "Все товары категории", при помощи curl и вставить в https://curlconverter.com/
<img width="1787" height="831" alt="image" src="https://github.com/user-attachments/assets/2a1fb6d5-b423-4d22-a84a-9a2666873298" />
3. Из полученного Python кода мы копируем и вставляем в Parser, вместо уже существующих полей

```python
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
```

4. Для запуска проекта необходимо установить зависимости ```pip install -r requirements.txt```
5. Далее запускаем наш парсер ```py parser.py```
6. После успешного парсинга, полученные данные сохраняются в файле ```products.json```

<h3>Результат работы:</h3>
 
1. После успешного парсинга страницы мы получаем сообщение об успешной операции и файл  ```products.json```
<img width="1104" height="792" alt="image" src="https://github.com/user-attachments/assets/73b59e78-ece4-4895-934a-dfae725f7934" />


