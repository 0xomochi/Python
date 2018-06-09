# learn zip() function
# reference : https://note.nkmk.me/python-zip-usage-for/

print("name / shinchoku / tamupoint")

names = ['yume', 'tamu', 'mochi']
shinchokus = [800, 600, 1000]
tamupoints = [400, 1000, 800]

for name, shinchoku, tamupoint in zip(names, shinchokus, tamupoints):
  print(name,  shinchoku, tamupoint)
