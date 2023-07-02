# Spacy

## Understand Ancestors and Children

Consider the sentence:

- The cat sat on the mat.


![image](https://github.com/johnosbb/ProgrammingInPyQT/assets/12407183/57794b3d-59d4-41d5-944c-3b26eb2f1192)


This has the following structure.



| Text         | Index  | POS      | Dep      | Dep Detail               | Ancestors            | Children   |
| ------------ | -------- | ------ | -------- | ------------------- |-------------- | --------- |
| The          | 0      | DET      | det      | determiner               | cat sat              |            |
| cat          | 1      | NOUN     | nsubj    | nominal subject          | sat                  | The        |
| sat          | 2      | VERB     | ROOT     | root                     |                      | cat on .   |
| on           | 3      | ADP      | prep     | prepositional modifier   | sat                  | mat        |
| a            | 4      | DET      | det      | determiner               | mat on sat           |            |
| mat          | 5      | NOUN     | pobj     | object of preposition    | on sat               | a          |
| .            | 6      | PUNCT    | punct    | punctuation              | sat                  |            |

```

- 'The' has ancestors 'cat' and 'sat', but it has no children as seen on the graph, there is no arrow starting from 'The and travelling to another token.
- 'cat' has an ancestor 'sat' as seen in the arrow that starts from sat and points back to 'sat'. 'cat' also has a 'The' with the arrow originating at 'sat and pointing back to 'cat'.
- 'sat' the ROOT has no ancestors, but it does have two children, one on each side.
- Similarly 'sat' is an ancestor of 'on'
- 'mat' has ancestors 'on' through a direct dependency and sat indirectly via 'on's relationship with 'sat'. 'mat' also has a child 'a'.


## References


https://spacy.pythonhumanities.com
https://spacy.pythonhumanities.com/01_04_pipelines.html

https://www.youtube.com/watch?v=dIUTsFT2MeQ&t=3382s
