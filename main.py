from jsonWrite import *
import entity

#TODO: make path selection user-defined 
path_to_json = r'your path here'

json_text_list = jsonExtractor(path_to_json)

jsons_dataframe = entity.entityExtractor(json_text_list)

NER_dataset_dict = filterDuplicates(jsons_dataframe)

writeToFile(NER_dataset_dict,'C:\\Users\\krono\\Desktop\\test.csv')
