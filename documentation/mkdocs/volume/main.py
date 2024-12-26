import csv
import os
import sys

import yaml

from pathlib import Path

from pprint import pprint

def define_env(env):
    def calc_path_file(path):
        dir_current = Path(env.variables.page.file.abs_src_path).parent
        path_file = os.path.join(dir_current, path)
        return path_file

    @env.macro
    def csv2table(path_csv):
        # 相対パスで指定したcsvからtableを生成するマクロ
        # 1行目で記入されない項目については表示しない
        dir_current = Path(env.variables.page.file.abs_src_path).parent
        path_file = os.path.join(dir_current, path_csv)

        ## csv file -> markdown table
        with open(path_file, encoding='utf8', newline='') as f:
            def row2text(row):
                return '| '  + ' | '.join(row) + ' |'
            csvreader = [i for i in csv.reader(f)]
            cols = len(csvreader[0])
            split_row = row2text(['-' for i in range(cols)])
            table_rows = [row2text(row) for row in csvreader]
        table_rows.insert(1, split_row)
        return '\n'.join(table_rows)
    
    @env.macro
    def sdmyaml2md(path, section_header='##'):
        with open(calc_path_file(path), 'r') as yml:
            data_list = yaml.safe_load(yml)
            md = ''

            # 正規化
            # for d_i in data_list:

            def get_value(dictionary, key):
                try:
                    return dictionary[key]
                except KeyError:
                    return ""


            # create md
            for d_i in data_list:
                if d_i['title'] is None:
                    continue
                md += f"""
                {section_header} {d_i['title']}
                ![]({get_value(d_i, 'path_thumbnail')})

                [{d_i['title']}]({get_value(d_i, 'path_model')})

                {get_value(d_i, 'comment')}
                """
            # 先頭のインデントを削除する
            md = '  \n'.join([line.strip() for line in md.split('\n')])

            return md

    @env.macro
    def lorayaml2md(path, section_header='##'):
        with open(calc_path_file(path), 'r') as yml:
            data_list = yaml.safe_load(yml)
            md = ''

            def get_value(dictionary, key):
                try:
                    return dictionary[key]
                except KeyError:
                    return ""

            # create md
            for d_i in data_list:
                if d_i['lora_name'] is None:
                    continue
                md += f"""
                {section_header} {d_i['lora_name']}
                ![]({get_value(d_i, 'lora_path_thumbnail')})

                [{d_i['lora_path_model']}]({get_value(d_i, 'lora_path_model')})

                {get_value(d_i, 'comment')}
                """
            # 先頭のインデントを削除する
            md = '  \n'.join([line.strip() for line in md.split('\n')])

            return md

    @env.macro
    def textual_inversion_yaml2md(path, section_header='##'):
        with open(calc_path_file(path), 'r') as yml:
            data_list = yaml.safe_load(yml)
            md = ''

            def get_value(dictionary, key):
                try:
                    return dictionary[key]
                except KeyError:
                    return ""

            # create md
            pk = 'asset_name'
            for d_i in data_list:
                if d_i[pk] is None:
                    continue
                
                d_i['asset_path_thumbnail_md_link'] = ''
                if get_value(d_i, 'asset_path_thumbnail') != '':
                    d_i['asset_path_thumbnail_md_link'] = f"![]({get_value(d_i, 'asset_path_thumbnail')})"
                
                md += f"""
                {section_header} {d_i[pk]}

                {d_i['asset_path_thumbnail_md_link']}

                [{d_i['asset_path']}]({get_value(d_i, 'asset_path')})

                {get_value(d_i, 'comment')}
                """

                
            # 先頭のインデントを削除する
            md = '  \n'.join([line.strip() for line in md.split('\n')])

            # print(md)

            return md