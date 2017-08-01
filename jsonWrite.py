import os, json
import csv


def jsonExtractor(file_path):

    json_files = [pos_json for pos_json in os.listdir(file_path) if pos_json.endswith('.json')]

    json_text = []

    for index, js in enumerate(json_files):
        with open(os.path.join(file_path, js), encoding='utf8') as json_file:
            json_text += json.load(json_file)

    return (json_text)



def filterDuplicates(jsons_data):
    NER_dict = {}

    for index, row in jsons_data.iterrows():
        for NER in row['text_content']:
            if (NER not in NER_dict):
                NER_dict[NER] = [row['paper_id']]
            else:
                NER_dict[NER].append(row['paper_id'])

    NER_dict = {k: v for k, v in NER_dict.items() if (len(v) > 1)}

    return(NER_dict)

def writeToFile(NER_dict, path):

    with open(path, 'w') as f:
        writer = csv.writer(f)
        for row in NER_dict.items():
            writer.writerow(row)



