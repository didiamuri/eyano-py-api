import json
from flask_restful import Resource
from flask import request, jsonify
import numpy as np

import pandas as pd
import pm4py

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class CustomerGraph(Resource):
    def get(self):
        data = request.get_json()
        df = pd.json_normalize(data['result'])

        event_log = pm4py.format_dataframe(df, case_id='case_id', activity_key='activity',timestamp_key='timestamp')    
        k = data['k']
        filtered_log = pm4py.filter_variants_top_k(event_log, k)
        dfg, start_activities, end_activities = pm4py.discover_dfg(filtered_log)

        data = []
        list = [(k, v) for k, v in dfg.items()]

        startData = json.loads(json.dumps(start_activities, cls=NpEncoder))
        endData = json.loads(json.dumps(end_activities, cls=NpEncoder))
        

        for val in list:
            data.append({"source": val[0][0], "target": val[0][1], "label": val[1]})

        return {"dfg": data, "start": startData, "end": endData }