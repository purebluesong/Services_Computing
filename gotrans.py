#coding=UTF-8
# from urllib import request
import requests
from sys import argv
import sys
import time
import ctypes
import execjs

params = {
	'sl':'en' ,
    'tl':'zh-CN' ,
    'hl':'zh-CN' ,
    'dt':'at' ,
    'dt':'bd' ,
    'dt':'ex' ,
    'dt':'ld' ,
    'dt':'md' ,
    'dt':'qca' ,
    'dt':'rw' ,
    'dt':'rm' ,
    'dt':'ss' ,
    'dt':'t' ,
    'ie':'UTF-8' ,
    'oe':'UTF-8' ,
    'source':'bh' ,
    'ssel':'0' ,
    'tsel':'0' ,
    'otf':'1' ,
    'kc':'1' ,
    'tk':'1' ,
    'q':'1' ,
}
googleTranslateUrl = "http://translate.google.cn/translate_a/single?client=t"


ctx = execjs.compile("""
var TKK = ((function() {
  var a = 561666268;
  var b = 1526272306;
  return 406398 + '.' + (a + b);
})());

function b(a, b) {
  for (var d = 0; d < b.length - 2; d += 3) {
      var c = b.charAt(d + 2),
          c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
          c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
      a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
  }
  return a
}

function tk(a) {
    for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
        var c = a.charCodeAt(f);
        128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ? (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240, g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
    }
    a = h;
    for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
    a = b(a, "+-3^+b+-f");
    a ^= Number(e[1]) || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1E6;
    return a.toString() + "." + (a ^ h)
}
""")

def tranlateCommand(argv):
	text = ' '.join(argv)
	params['q'] = text
	params['tk'] = ctx.call("tk",text)
	answer = requests.get(googleTranslateUrl,params).text
	print answer.replace('[','').replace(']','').split(',')[0]

def tranlate():
	while(True):
		text = raw_input("Input tranlate:")
		params['q'] = text
		params['tk'] = ctx.call("tk",text)
		print(params['tk'])
		print(requests.get(googleTranslateUrl,params).text)

if __name__ == "__main__":
	if 'gotrans.py' in argv:
		argv.remove('gotrans.py')
	if len(argv) != 0 :
		tranlateCommand(argv[1:])
	else:
		tranlate()
