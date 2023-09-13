# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def T4():
    print(chr(0x2605)*11)
    print(chr(0x2605)+'数据科学与工程导论'+chr(0x2605))
    print(chr(0x2605)*11)
    return

T4()
