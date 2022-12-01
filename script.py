import pandas as pd
import pm4py
import os


file_path = "data.csv"

def getImagePM(file_path,k_in):
    event_log = pm4py.format_dataframe(pd.read_csv(file_path, sep=','), case_id='case_id', activity_key='activity',timestamp_key='timstamp')    
    k = 2
    filtered_log = pm4py.filter_variants_top_k(event_log, k)
    dfg, start_activities, end_activities = pm4py.discover_dfg(filtered_log)
    pm4py.view_dfg(dfg, start_activities, end_activities,format="PNG")

    map2 = pm4py.discover_heuristics_net(filtered_log)
    fn = 'map1.png'

    img_dir = "./static"
    img_path = os.path.join(img_dir, fn)

    pm4py.save_vis_heuristics_net(map2, img_path)

getImagePM(file_path, 2)