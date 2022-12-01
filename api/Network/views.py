import random
import string
from flask_restful import Resource
from flask import request, jsonify

import pandas as pd
import pm4py
import os

class NetworkGraphList(Resource):
    def get(self):
        data = request.get_json()
        df = pd.json_normalize(data['result'])

        event_log = pm4py.format_dataframe(df, case_id='case_id', activity_key='activity',timestamp_key='timestamp')    
        k = 20
        filtered_log = pm4py.filter_variants_top_k(event_log, k)
        dfg, start_activities, end_activities = pm4py.discover_dfg(filtered_log)
        # pm4py.view_dfg(dfg, start_activities, end_activities,format="PNG")

        map2 = pm4py.discover_heuristics_net(filtered_log)
        caseId = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        fn = str(caseId) + '.png'

        img_dir = "./static"
        img_path = os.path.join(img_dir, fn)

        url = "http://localhost/api/v1/graph/" + str(fn)

        pm4py.save_vis_heuristics_net(map2, img_path)
        return {"url": url}