# Extending Spacy with A Custom Factory and Custom Attributes

## We define a custom factory in a sepearate file. In this instance sentiment_analyser.py

```python
# Register a custom attribute 'is_positive' for tokens
import spacy
from spacy.tokens import Token
from spacy.language import Language


Token.set_extension("is_positive", default=False)

# Define your data transformation logic


@Language.component("sentiment_analyzer")
def sentiment_analyzer(doc):
    for token in doc:
        # Perform sentiment analysis here and set a custom attribute 'is_positive'
        # For this example, we'll assume positive sentiment for tokens containing 'good'
        if 'good' in token.text.lower():
            token._.is_positive = True
        else:

            token._.is_positive = False
    return doc


```

## Adding the new sentiment analyser pipeline to out model

```python
import spacy
from spacy.tokens import Token
from spacy.language import Language
import sentiment_analyser # Import the file containing the factory component


# Load the base English model
nlp = spacy.load("en_core_web_sm")


# Add the custom component to the pipeline
nlp.add_pipe("sentiment_analyzer", last=True)

# Process the text
text = "She was feeling happy after the good news."
doc = nlp(text)

nlp.to_disk("./Models/model_with_custom_factory")
for token in doc:
    print(token.text, token._.is_positive)
```

## Using the extended Model

```python
import spacy
from spacy.language import Language
import sentiment_analyser

nlp_new = spacy.load("./Models/model_with_custom_factory")
text = "This is a string with good or positive sentiment"
doc = nlp_new(text)
for token in doc:
    print(token.text, token._.is_positive)
```


## Packaging the Model

We can package the model with the custom factory by calling:


Before doing this we can change the name and description in the meta.json file of the source model ./Models/model_with_custom_factory

```json
  "name": "core_web_sm_ex",
  "version": "3.5.0",
  "description": "English pipeline optimized for CPU with custom factory extension. ...."
```
We can then run:

```bash
python -m spacy package ./Models/model_with_custom_factory ./Models/packages --code sentiment_analyser.py
```

This creates a model called core_web_sm_ex with the necessary factory that can be pip installed with 

```bash
pip install en_core_web_sm_ex-3.5.0.tar.gz
```

## Using the packaged Model

We can then use the installed model without having to reference the custom factory code directly as an import.

```python

import spacy
from spacy.language import Language

nlp_new = spacy.load("en_core_web_sm_ex")
text = "This is a string with good or positive sentiment"
doc = nlp_new(text)
for token in doc:
    print(token.text, token._.is_positive)
```


## References

- [Spacy Serialization Records](https://spacy.io/usage/saving-loading#serialization-methods)

# Extending Spacy with a Custom Entity Ruler

## Define the Rules in a JSON file called syslog_entities.json


```json
[
    "Status",
    "Workspace_Management",
    "client",
    "OSD",
    "workspace",
    "app.py:"
]
```


## We can add a Custom Entity Ruler based on the json data


```python
# How to add a custom NER Ruler (based on patterns stored in a json file) to an existing Model to extend NER

import spacy
import json
import os
from spacy.pipeline import EntityRuler


# format of Spacy yTraining Data
# TRAIN_DATA = [(text, {"entities": [(start,end,label)]})]

def save_data(file,data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data,f, indent=4)

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (data)  

def create_training_data(file,type):
    data = load_data(file)
    patterns = []
    for item in data:
        pattern = {"label" : type , "pattern" : item} # this is what spacy expects
        patterns.append(pattern)
    return patterns    
        
       
def generate_rules(nlp,patterns):
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns)
    nlp.to_disk("syslog_ner") # save the model for later use

nlp = spacy.load("en_core_web_sm", disable=["tagger","parser","lemmatizer","tok2vec", "tagger"])        # if we wish we can disable unused components
patterns = create_training_data("ReferenceFiles/syslog_entities.json","COMPONENT") 
generate_rules(nlp,patterns)  
print(nlp.pipe_names) 
```

## Using the Extended Model

We can then use the extended model by loading it in another program

```python
# How to use the previously extended model

import spacy
import json
import os
from spacy.pipeline import EntityRuler

def test_model(nlp, text):
    doc = nlp(text)
    results = []
    entities = []

    for ent in doc.ents:
        if(ent.label_ != "CARDINAL"):
            print(f"text: {ent.text}, label {ent.label_}")
            results.append(f"text: {ent.text}, label {ent.label_}")
    return (results)  

nlp = spacy.load("syslog_ner")
with open("syslog", "r") as f: #read in a file to test our model on
    text = f.read()
doc = nlp(text)    
    
test_model(nlp, text)
```

