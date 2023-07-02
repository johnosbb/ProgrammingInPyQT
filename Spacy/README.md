# Spacy

## Understand Ancestors and Children

Consider the sentence:

- The cat sat on the mat.


![image](https://github.com/johnosbb/ProgrammingInPyQT/assets/12407183/5e4bcfc2-f90c-4010-a250-0f9010fce5c8)

This has the following structure.

'''text

Text         | Index  | POS      | Dep      | Dep Detail               | Ancestors            | Children   
----------------------------------------------------------------------------------------------------------------------
The          | 0      | DET      | det      | determiner               | cat sat              |            
----------------------------------------------------------------------------------------------------------------------
cat          | 1      | NOUN     | nsubj    | nominal subject          | sat                  | The        
----------------------------------------------------------------------------------------------------------------------
sat          | 2      | VERB     | ROOT     | root                     |                      | cat on .   
----------------------------------------------------------------------------------------------------------------------
on           | 3      | ADP      | prep     | prepositional modifier   | sat                  | mat        
----------------------------------------------------------------------------------------------------------------------
a            | 4      | DET      | det      | determiner               | mat on sat           |            
----------------------------------------------------------------------------------------------------------------------
mat          | 5      | NOUN     | pobj     | object of preposition    | on sat               | a          
----------------------------------------------------------------------------------------------------------------------
.            | 6      | PUNCT    | punct    | punctuation              | sat                  |            
----------------------------------------------------------------------------------------------------------------------
```

## References


https://spacy.pythonhumanities.com
https://spacy.pythonhumanities.com/01_04_pipelines.html

https://www.youtube.com/watch?v=dIUTsFT2MeQ&t=3382s
