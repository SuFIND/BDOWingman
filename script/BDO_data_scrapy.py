# -*- coding: utf-8 -*-
"""
@Project : BDOWingman
@File : BDO_data_scrapy.py
@Author : FF
@Time : 2023/1/18 14:27
"""
import copy
import datetime
import json
import time

import requests
import tqdm
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_model.model import Culinary, Items, MaterialGroup

TABLE_NICKNAME_TRANS = {
    'item': Items,
    'culinary': Culinary,
    'materialgroup': MaterialGroup
}


def fetch_BDO_website_items_data():
    item_url = "http://bdocodex.com/query.php?a=items&l=tw"
    r = requests.get(item_url)
    if r.status_code != 200:
        raise ConnectionError(f"can't not connect {item_url}")
    str_data = r.text
    str_data = str_data.encode("utf-8")
    json_obj = json.loads(str_data)
    with open(f'dev_data/BDO_items_{datetime.date.today().strftime("%Y_%m_%d")}.json', 'w',
              encoding="utf-8") as fp:
        json.dump(json_obj, fp, ensure_ascii=False)


def import_item_to_sqlite():
    with open("dev_data/BDO_items_2023_01_18.json", encoding="utf8") as fp:
        json_obj = json.load(fp)

    from db_model.model import Items

    engine = create_engine("sqlite:///data/BDOdata.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()

    after_sort_data = copy.deepcopy(json_obj["aaData"])
    after_sort_data.sort(key=lambda x: x[0])

    for item in after_sort_data:
        item_id = item[0]
        item_title_html = item[2]

        soup = BeautifulSoup(item_title_html, features="html.parser")
        item_title_tc = soup.find('b').get_text()
        detail_url = soup.find('a').get('href')
        if detail_url is not None:
            detail_url = f"https://bdocodex.com{detail_url}"
        row = Items(id=item_id, title_tc=item_title_tc, ref_url_tc=detail_url)
        session.add(row)

    session.commit()
    session.close()


def fetch_BDO_website_culinary_data():
    item_url = "http://bdocodex.com/query.php?a=recipes&type=culinary&id=1&l=tw"
    r = requests.get(item_url)
    if r.status_code != 200:
        raise ConnectionError(f"can't not connect {item_url}")
    str_data = r.text
    str_data = str_data.encode("utf-8")
    json_obj = json.loads(str_data)
    with open(f'dev_data/BDO_culinary_{datetime.date.today().strftime("%Y_%m_%d")}.json', 'w',
              encoding="utf-8") as fp:
        json.dump(json_obj, fp, ensure_ascii=False)


def import_culinary_to_sqlite():
    with open("dev_data/BDO_culinary_2023_01_18.json", encoding="utf8") as fp:
        json_obj = json.load(fp)

    from db_model.model import Culinary, Items

    engine = create_engine("sqlite:///data/BDOdata.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()

    after_sort_data = copy.deepcopy(json_obj["aaData"])
    after_sort_data.sort(key=lambda x: x[0])

    for item in after_sort_data:
        item_id = item[0]
        item_title_html = item[2]
        item_material_html = item[6]

        title_tc_soup = BeautifulSoup(item_title_html, features="html.parser")
        item_title_tc = title_tc_soup.find('b').get_text()

        material_soup = BeautifulSoup(item_material_html, features="html.parser")
        material_elems = material_soup.find_all('a')

        row = Culinary(id=item_id,
                       title_tc=item_title_tc)

        for elem_idx, material_elem in enumerate(material_elems):
            material_elem_id = elem_idx + 1
            material_id = material_elem.get('data-id')
            table_nickname, id_in_table = material_id.split("--")
            if table_nickname not in TABLE_NICKNAME_TRANS:
                print(material_id, item_title_tc)
            table_obj = TABLE_NICKNAME_TRANS[table_nickname]
            table_name = table_obj.__tablename__

            material_title_tc = ""
            if table_obj == Items:
                ref_row = session.query(getattr(table_obj, "title_tc")).filter(getattr(table_obj, "id") == id_in_table).first()
                if ref_row is None:
                    print('ref row is None', material_id)
                    continue
                material_title_tc = ref_row.title_tc
            elif table_obj == MaterialGroup:
                ref_row = session.query(getattr(table_obj, "group_title_tc")).filter(getattr(table_obj, "group_id") == id_in_table).first()
                if ref_row is None:
                    print('ref row is None', material_id)
                    continue
                material_title_tc = ref_row.group_title_tc
            else:
                print(f"not support import data about {table_nickname}", material_elem_id)

            material_weight_elem = material_elem.find('div', attrs={"class": "quantity_small nowrap"})
            material_weight = material_weight_elem.get_text()

            setattr(row, f'material_{material_elem_id}_id', id_in_table)
            setattr(row, f'material_{material_elem_id}_type', table_name)
            setattr(row, f'material_{material_elem_id}_title_tc', material_title_tc)
            setattr(row, f'material_{material_elem_id}_weight', material_weight)

        session.add(row)

    session.commit()
    session.close()


def import_materialgroup_to_sqlite():
    cur = 1
    max_find = 50

    engine = create_engine("sqlite:///data/BDOdata.sqlite")
    Session = sessionmaker(bind=engine)
    session = Session()

    while cur <= max_find:
        scrap_url = f"https://bdocodex.com/tw/materialgroup/{cur}/"
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        r = requests.get(scrap_url, headers=headers)
        if r.status_code != 200:
            raise ConnectionError
        html = r.text
        soup = BeautifulSoup(html, features="html.parser")
        group_title_elem = soup.find('li', attrs={"class": "breadcrumb-item active", "aria-current": "page"})
        if group_title_elem is None:
            print(f"skip {scrap_url}")
            cur += 1
            continue
        group_title_tc = group_title_elem.get_text()

        td_elem = soup.find("td", attrs={"colspan": "2"})
        if td_elem is None:
            print(f"skip {scrap_url}")
            cur += 1
            continue
        a_elems = td_elem.find_all("a", attrs={"class": ['qtooltip', 'item_grade_0']})
        for a_elem in a_elems:
            a_elem_class = a_elem.get('class', [])
            if 'item_grade_1' in a_elem_class \
                    or 'item_grade_0' in a_elem_class \
                    or 'item_grade_2' in a_elem_class:
                continue
            data_id = a_elem["data-id"]
            table_nickname, id_in_table = data_id.split("--")
            table_obj = TABLE_NICKNAME_TRANS[table_nickname]
            if table_obj == Items:
                row = MaterialGroup(group_id=cur, group_title_tc=group_title_tc, item_id=int(id_in_table),
                                    item_title_tc=a_elem.get_text())
                session.add(row)
            else:
                print(group_title_tc, table_nickname, id_in_table)
        cur += 1
        time.sleep(1)

    session.commit()


if __name__ == '__main__':
    task = 5
    if task == 1:
        fetch_BDO_website_items_data()
    elif task == 2:
        import_item_to_sqlite()
    elif task == 3:
        fetch_BDO_website_culinary_data()
    elif task == 4:
        import_culinary_to_sqlite()
    elif task == 5:
        import_materialgroup_to_sqlite()
    else:
        print("no support task")
