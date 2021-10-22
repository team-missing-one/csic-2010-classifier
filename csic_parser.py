import io
import urllib.parse
import numpy as np


def parse(file_in, file_out):
    f = open("csic/" + file_in, 'r', encoding="utf8")
    lines = list(map(lambda line: line.strip(), f.readlines()))
    res = []
    for i in range(len(lines)):
        line = lines[i]
        words = line.split(' ')
        url_req = ''
        is_req = False
        if line.startswith("GET"):
            is_req = True
            url_req = words[0] + words[1]
        elif line.startswith("POST") or line.startswith("PUT"):
            is_req = True
            url_req = words[0] + words[1]
            idx = 1
            while not lines[i + idx].startswith("Content-Length"):
                idx += 1
            url_req += '?' + lines[i + idx + 2]
        if is_req:
            res.append(url_req)
    f.close()

    out = io.open(file_out, 'w', encoding="utf-8")
    for e in res:
        out.writelines(urllib.parse.unquote(e).replace('\n', '').lower() + '\n')
    print("Parsing complete.", len(res), "requests earned from", file_in)


def load_parsed(file):
    with open(file, 'r', encoding="utf8") as f:
        data = f.readlines()
    ret = []
    for i in data:
        i = i.strip()
        if i != '':
            ret.append(i)
    return ret


# 0: normal, 1: anomaly
def make_data_set(parsed: list, label: int):
    return {
        "data": parsed,
        "target": np.array([label] * len(parsed), dtype=np.uint8),
        "target_names": np.array(["normal", "anomaly"])
    }


def combine_data_set(data_l: dict, data_r: dict):
    if "target_names" not in data_l or "target_names" not in data_r:
        print("Invalid data set!")
        return False
    if not np.array_equal(data_l["target_names"], data_r["target_names"]):
        print("Invalid combining!")
        return False
    return {
        "data": data_l["data"] + data_r["data"],
        "target": np.append(data_l["target"], data_r["target"]),
        "target_names": data_l["target_names"].copy()
    }
