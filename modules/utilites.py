#################################################
#                 created by                    #
#                     ZZS                       #
#                     SBR                       #
#################################################
import datetime
import json
import parawrap
import xlwt
from time import gmtime, strftime
############static variables#####################

#################################################


def get_rtc():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def get_data_main_page(db):
    cat_quantity = {'ksg': 0, 'mkb': 0, 'service': 0, 'region': 0, 'area': 0, 'med_profile': 0, 'users': 0}
    temp = list()
    for cat in cat_quantity.keys():
        if cat == 'users':
            for role in range(4):
                temp.append(db.get_quantity(cat, ['role', role]))
            cat_quantity[cat] = temp  # 0 - admin, 1 - moderator, 2 - curator, 3 - user
        else:
            cat_quantity[cat] = db.get_quantity(cat)
    return cat_quantity


def unparse_json(data):
    return json.loads(data)


def parse_json(data):
    return json.dumps(data)


def update_profile(new_data, old_data, db):
    out = list()
    f_old = old_data[0:2] + [old_data[5]]
    compare = {0: 'login', 1: 'full_name', 2: 'password'}
    for diff in range(len(new_data)):
        if diff == 1:
            out.append([])
            for i in range(len(new_data[diff])):
                if new_data[diff][i] != '':
                    out[diff].append(new_data[diff][i])
                else:
                    out[diff].append(f_old[diff][i])
            db.add_db_entry(f'UPDATE users SET {compare[diff]} = %s WHERE id = {old_data[4]}', (parse_json(out[diff]), ))
        else:
            if new_data[diff] != '':
                out.append(new_data[diff])
                db.add_db_entry(f'UPDATE users SET {compare[diff]} = %s WHERE id = %s', (new_data[diff], old_data[5]))
            else:
                out.append(f_old[diff])
    for i in range(3):
        out.insert(i + 2, old_data[i + 2])
    return out


def word_wrap(text, max_len):
    s = ''
    data = parawrap.wrap(text, max_len)
    for i in data:
        s += i + '\n'
    return s


def save_export_xlsx(path, data, typ):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet")
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i, j, data[i][j])
    workbook.save(path + f'export_{typ}({strftime("%Y_%m_%d_%H_%M_%S", gmtime())}).xlsx')


def switch_btns_user(data, value, db):
    fields = {'1': 'agent', '2': 'blocked'}
    db.add_db_entry(f'UPDATE users SET {fields[data[1]]} = {value} WHERE id = "{data[0]}"', ())


def switch_btns_ksg(data, value, db):
    db.add_db_entry(f'UPDATE ksg SET ratio_switch = {value} WHERE id = "{data}"', ())




