from jsonWrite import *
import entity

path_to_json = r'C:\Users\krono\Downloads\New folder'

json_text_list = jsonExtractor(path_to_json)

jsons_dataframe = entity.entityExtractor(json_text_list)

NER_dataset_dict = filterDuplicates(jsons_dataframe)

writeToFile(NER_dataset_dict,'C:\\Users\\krono\\Desktop\\test.csv')
