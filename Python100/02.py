# 02.py
# "yume" + "tamu" の文字を先頭から交互に連結して文字列"ytuammeu"を得よ.

str1 = 'yume'
str2 = 'tamu'
sum = ''
for c1, c2 in zip(str1, str2):
  sum += c1 + c2                        # "a += b" means "a = a + b"
  print(sum)

