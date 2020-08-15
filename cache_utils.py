import os.path
import pickle as pkl
import requests

def get_response(url, enable_dump=True):
    global saved_data
    if 'res_dict' not in saved_data:
        saved_data['res_dict'] = {}
    res_dict = saved_data['res_dict']
    if url in res_dict:
        response = res_dict[url]
    else:
        response = requests.get(url)
        res_dict[url] = response
    if enable_dump:
        dump_saved_data()
    return response

def saved_data_init():
    global saved_data
    if 'saved_data' not in globals():
        if os.path.exists('saved_data.pkl'):
            with open('saved_data.pkl', 'rb') as f:
                saved_data = pkl.load(f)
        else:
            saved_data = {}

def dump_saved_data():
    global saved_data
    with open('saved_data.pkl', 'wb') as f:
        pkl.dump(saved_data, f)

saved_data_init()