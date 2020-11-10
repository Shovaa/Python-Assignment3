#finding the number of occurence in the given set of string:

def count_char(text):
  for i in range(len(text)):
    if len(text) == 0:
      break;
    ch = text[0]
    if ch == ' ' or ch == '\t':
      continue
    result= ({ch :  text.count(ch)})
    print (dict(result))
    text = text.replace(ch, '').strip()

count_char('pineapple')