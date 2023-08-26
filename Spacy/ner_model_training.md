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
