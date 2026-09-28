# saucedemo test

простой тест покупки товара на https://www.saucedemo.com/

## как запустить

1. установить зависимости:
```
pip install -r requirements.txt
```

2. запуск теста (хром по умолчанию):
```
pytest test_buy_product.py -v
```

3. запуск в firefox:
```
pytest test_buy_product.py -v --browser=firefox
```

4. можно передать свой url:
```
pytest test_buy_product.py -v --url=https://www.saucedemo.com/
```

## что сделано
- скрипт покупки (логин, добавление в корзину, форма, покупка)
- фикстура браузера в conftest.py
- фикстура url
- хук pytest_addoption
- мультибраузерность (chrome / firefox)
- проверка текста "Thank you for your order!"
