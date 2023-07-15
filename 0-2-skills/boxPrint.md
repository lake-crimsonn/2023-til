```python
def boxPrint(data,num):
    wrapped_sentence = textwrap.fill(data['facts'][num], width=80)
    print('fp: ', data['first_party'][num], 'sp: ',data['second_party'][num])
    print(wrapped_sentence)
    print('-'*100)
```