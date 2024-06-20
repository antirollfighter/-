# -*- coding: utf-8 -*-


import pandas as pd
import json
import os
from idMid import id2mid

input_config_json = 'forward_config.json'

# result_config_json = "forward_config1.json"

forward_folder = 'forward'

with open(input_config_json, 'r', encoding='utf-8-sig') as f:
    config_json = json.loads(f.read())

root_mid = config_json['mids'][0]

df = pd.read_csv(os.path.join(forward_folder, root_mid + '.csv'))

## csv 文件中地这个 mid 字段名称应该改成 id 才更合理
child_ids = df['mid'].values.tolist()
child_mids = []
for child_id in child_ids:
    child_mid = id2mid(str(child_id))
    print(f'parse id: {child_id} to mid: {child_mid}')
    child_mids.append(child_mid)

config_json['mids'] = child_mids
with open(input_config_json, 'w', encoding='utf-8-sig') as f:
    f.write(json.dumps(config_json, indent=2))
