import datetime
import numpy as np
import pandas as pd
import requests
# import xlrd
from bs4 import BeautifulSoup
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
from urllib.parse import urlencode

from .constants import (FILE_PRICES, FOLDER, URL_BASE, URL_PRICES,
                        PRODUCT_SIGN_COLUMN, PRODUCT_IMAGE_COLUMN,
                        PRODUCT_NAME_COLUMN, PRODUCT_SIZE_RANGE,
                        PRODUCT_PRICE_COLUMN, PRODUCT_COLOR_COLUMN,
                        PRODUCT_START_REMAINS_COLUMN, PRODUCT_SKIP_HEAD_ROWS)
from .models import CodeSupplierFile, CodeSupplierBase, PriceSupplier

CODE_SUPPLIER = 564


def get_prices_text(url=URL_PRICES):
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        raise ConnectionError(f'Connection error: {url}')
    if response.status_code != 200:
        raise ConnectionError(f'Error status code: {url}')
    return response.text


def get_file_url(url, file_name_new):
    try:
        download_response = requests.get(url)
    except requests.ConnectionError:
        raise ConnectionError(f'Connection error: {url}')
    if download_response.status_code != 200:
        raise ConnectionError(f'Error status code: {url}')
    try:
        with open(file_name_new, 'wb') as f:
            f.write(download_response.content)
            return True
    except Exception:
        raise ConnectionError(f'Error save file: {file_name_new}')


def get_file(public_key, file_name):
    """Get file from Yandex disk

    arguments:
    public_key -- link to the file on yandex.disk
    file_name -- name of file for save.
    """

    final_url = URL_BASE + urlencode(dict(public_key=public_key))
    try:
        response = requests.get(final_url)
    except requests.ConnectionError:
        raise ConnectionError(f'Connection error: {final_url}')
    if response.status_code != 200:
        raise ConnectionError(f'Error status code: {final_url}')
    download_url = response.json()['href']
    return get_file_url(download_url, f'{FOLDER}tmp/{file_name}')


def get_files():
    files = []
    soup = BeautifulSoup(get_prices_text(), 'lxml')
    mydivs = soup.find_all("div", {"class": "right_block wide_"})[0]
    for tag in mydivs.find_all("li"):
        try:
            content = tag.contents[2].attrs['href']
            text = tag.text
            files.append((text, content))
        except Exception:
            ...
    return files


def save_files():
    files = get_files()
    for text, content in files:
        for name, file_price in FILE_PRICES:
            if name in text:
                get_file(content, file_price)
                # file_new = f'{FOLDER}tmp/{file_price}'
                # file_old = f'{FOLDER}{file_price}'
                # print(file_price)
                # check_file(file_new, file_old)
                break
        # break


def get_code(supplier, product, size, color):
    try:
        vals = CodeSupplierFile.objects.filter(
            supplier=supplier,
            name=f'{product} {size} {color}',
            #product_summary=product,
            #size=size,
            #color=color,
        )
        if vals:
            val = vals.first()
            return (val.code, val.brand, val.subgroup)
    except ObjectDoesNotExist:
        ...
        # return None
    except Exception as e:
        print(f'File: {product} {size} {color} :{e}')
    return None


def get_brand(supplier, code):
    try:
        val = CodeSupplierBase.objects.get(code=code, supplier=supplier)
        return (val.brand, val.subgroup)
    except ObjectDoesNotExist:
        return None
    except Exception as e:
        print(f'Base: {code} :{e}')
        return None


def parse_file(file, current_code):
    print(datetime.datetime.now().time())
    print(f'----------- {file} ---------------')
    inf = pd.read_excel(file, skiprows=PRODUCT_SKIP_HEAD_ROWS)
    sizes = []
    product_name = ''
    product_price = 0
    price_supplier = []
    for s in inf.itertuples():
        if not np.isnan(s[PRODUCT_SIGN_COLUMN]):
            product_name = s[PRODUCT_NAME_COLUMN]
            product_price = s[PRODUCT_PRICE_COLUMN]
            product_price = 0 if np.isnan(product_price) else product_price
            sizes.clear()
            for i in PRODUCT_SIZE_RANGE:
                size = s[i]
                # print(type(size))
                if isinstance(size, str):
                    # if not np.isnan(size):
                    sizes.append(size)
        else:
            if product_price > 0:
                product_color = s[PRODUCT_COLOR_COLUMN]
                for i, size in enumerate(sizes):
                    remains = s[i + PRODUCT_START_REMAINS_COLUMN]
                    if isinstance(remains, str):
                        codes = get_code(
                            CODE_SUPPLIER, product_name, size, product_color
                            )
                        if codes:
                            code, brand, subgroup = codes
                            brands = get_brand(CODE_SUPPLIER, code)
                            if brands:
                                brand, subgroup = brands
                            # print(f'{code} {brand} {subgroup } ------------')
                        else:
                            code, brand, subgroup = current_code, '?', '?'
                            current_code += 1
                            # print(f'{product_name} {product_price} '
                            #      f'{product_color} {size}')
                        price_supplier.append(PriceSupplier(
                            code=code,
                            name=f'{product_name} {size} {product_color}',
                            brand=brand,
                            subgroup=subgroup,
                            supplier=CODE_SUPPLIER,
                            product_summary=product_name,
                            size=size,
                            color=product_color,
                            price=product_price,
                        ))
    PriceSupplier.objects.bulk_create(price_supplier)
    return current_code


def parse_files():
    code_max = CodeSupplierFile.objects.filter(
        supplier=CODE_SUPPLIER
        ).aggregate(Max('code'))
    current_code = code_max['code__max'] + 1
    PriceSupplier.objects.all().delete()
    for _, file in FILE_PRICES:
        current_code = parse_file(f'{FOLDER}tmp/{file}', current_code)
        # break
