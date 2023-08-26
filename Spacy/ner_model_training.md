# Train Spacy 3.0 for Entity Recognition

## Generating Training Data

Training data can be created by various annotation tools like [ner-annotator](https://tecoholic.github.io/ner-annotator/)

### Converting the data to Spacy Format

```python

import pandas as pd
import json
import os
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin


DATA_PATH = "./data/Syslog/annotations.json"

with open(DATA_PATH, 'r') as f:
    data = json.load(f)

train_data = data['annotations']
train_data = [tuple(i) for i in train_data]

nlp = spacy.blank("en")  # load a new spacy model
# nlp = spacy.load("en_core_web_sm") # load other spacy model

db = DocBin()  # create a DocBin object

for text, annot in tqdm(train_data):  # data in previous format
    doc = nlp.make_doc(text)  # create doc object from text
    ents = []
    for start, end, label in annot["entities"]:  # add character indexes
        span = doc.char_span(start, end, label=label,
                             alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents  # label the text with the ents
    db.add(doc)

db.to_disk("./data/Syslog/train.spacy")  # save the docbin object

```

Generate a base_config.cfg file using this link [Config Generator](https://spacy.io/usage/training#config)

Create a custom config file based on the base config by running the following command.

``bash
python -m spacy init fill-config base_config.cfg config.cfg
```

```bash
python -m spacy init fill-config base_config.cfg config.cfg
✔ Auto-filled config with all values
✔ Saved config
config.cfg
You can now add your data and train your pipeline:
python -m spacy train config.cfg --paths.train ./train.spacy --paths.dev ./dev.spacy

```
