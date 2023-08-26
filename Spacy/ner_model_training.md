# Training Spacy 3.0 for Entity Recognition

## Generating Training Data

Training data can be created by various annotation tools like [ner-annotator](https://tecoholic.github.io/ner-annotator/)

```json
{
    "classes": [
        "SOFTWARE_COMPONENT",
        "PROGRAM",
        "MQTT_MESSAGE",
        "CLIENT_COMMAND",
        "ERROR"
    ],
    "annotations": [
        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: Workspace_Management: Terminating workspace 5 /workspace - new workspace",
            {
                "entities": [
                    [
                        35,
                        55,
                        "SOFTWARE_COMPONENT"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: Terminating workspace connections ",
            {
                "entities": [
                    [
                        27,
                        33,
                        "PROGRAM"
                    ]
                ]
            }
        ],

        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: mqtt: send_message: topic ",
            {
                "entities": [
                    [
                        27,
                        33,
                        "PROGRAM"
                    ],
                    [
                        61,
                        120,
                        "MQTT_MESSAGE"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: Command: /usr/local/bin/bb_kvm_client ",
            {
                "entities": [
                    [
                        44,
                        327,
                        "MQTT_MESSAGE"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: MONITOR: HDMI-3 (2): pos 1920x0 res 3840x2160",
            {
                "entities": [
                    [
                        27,
                        33,
                        "PROGRAM"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: TILE_CALC: pos: 1922x0 size: 1916x1055",
            {
                "entities": []
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: Command: /usr/local/bin/bb_kvm_client 9",
            {
                "entities": [
                    [
                        44,
                        330,
                        "CLIENT_COMMAND"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm app.py: Command: /usr/local/bin/bb_rdp_client ,
            {
                "entities": [
                    [
                        44,
                        327,
                        "CLIENT_COMMAND"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm bb_rdp_client[153486]: freerdp_abort_connect_context:freerdp_set_last_error_ex ERRCONNECT_CONNECT_CANCELLED [0x0002000B]",
            {
                "entities": [
                    [
                        80,
                        105,
                        "ERROR"
                    ],
                    [
                        106,
                        134,
                        "ERROR"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm bb_kvm_client[153482]: freerdp_check_fds() failed - 0",
            {
                "entities": [
                    [
                        70,
                        76,
                        "ERROR"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm bb_kvm_client[153482]: rdp_print_errinfo wCloudBB ERRINFO_PEER_DISCONNECTED (0x00001196):The peer connection was lost.",
            {
                "entities": [
                    [
                        50,
                        67,
                        "ERROR"
                    ],
                    [
                        77,
                        102,
                        "ERROR"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm bb_kvm_client[153488]: freerdp_check_fds() failed - 0",
            {
                "entities": [
                    [
                        70,
                        76,
                        "ERROR"
                    ]
                ]
            }
        ],
        [
            "Jul 11 16:38:47 snuc-sdkvm bb_kvm_client[153488]: rdp_print_errinfo wCloudBB ERRINFO_PEER_DISCONNECTED (0x00001196):The peer connection was lost.",
            {
                "entities": [
                    [
                        50,
                        67,
                        "CLIENT_COMMAND"
                    ],
                    [
                        77,
                        102,
                        "ERROR"
                    ]
                ]
            }
        ]
}
```

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


## Generating a Config File for the Model

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

## Train the Model


```bash
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy 
ℹ Saving to output directory: output
ℹ Using CPU

=========================== Initializing pipeline ===========================
[2023-08-26 14:15:44,947] [INFO] Set up nlp object from config
[2023-08-26 14:15:44,966] [INFO] Pipeline: ['tok2vec', 'ner']
[2023-08-26 14:15:44,971] [INFO] Created vocabulary
[2023-08-26 14:15:44,980] [INFO] Finished initializing nlp object
[2023-08-26 14:15:45,229] [INFO] Initialized pipeline components: ['tok2vec', 'ner']
✔ Initialized pipeline

============================= Training pipeline =============================
ℹ Pipeline: ['tok2vec', 'ner']
ℹ Initial learn rate: 0.001
E    #       LOSS TOK2VEC  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE 
---  ------  ------------  --------  ------  ------  ------  ------
  0       0          0.00     49.45    0.00    0.00    0.00    0.00
 32     200       2096.24   3005.62   82.35   80.77   84.00    0.82
 72     400       8897.19   2514.65   90.20   88.46   92.00    0.90
122     600      17885.16   4397.02   92.00   92.00   92.00    0.92
186     800       8564.16   2969.25   88.00   88.00   88.00    0.88
257    1000      31317.78   5540.93   88.00   88.00   88.00    0.88
357    1200      31496.34   8778.02   88.00   88.00   88.00    0.88
457    1400      20830.71   5129.60   88.00   88.00   88.00    0.88
585    1600      73978.23   9807.69   92.00   92.00   92.00    0.92
785    1800      67894.53  11027.76   92.00   92.00   92.00    0.92
985    2000      57954.77   9316.73   92.00   92.00   92.00    0.92
1185    2200      49331.61   8892.55   88.00   88.00   88.00    0.88
✔ Saved pipeline to output directory
```
