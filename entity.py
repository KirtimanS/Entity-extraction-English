from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import pandas as pd


def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk


def entityExtractor(json_text):
    jsons_data = pd.DataFrame(columns=['paper_id', 'text_content'])

    for objects in range(len(json_text)):
        paper_id = json_text[objects]['_id']

        text_content = json_text[objects]['text_content']
        text_content = get_continuous_chunks(text_content)

        jsons_data.loc[objects] = [paper_id, text_content]

    return (jsons_data)