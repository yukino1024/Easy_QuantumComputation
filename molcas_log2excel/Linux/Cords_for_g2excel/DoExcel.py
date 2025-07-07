from molcas_log import do_write
import sys

if len(sys.argv) < 2:
    print("请提供参数！")
else:
    adress = sys.argv[1]

do_write(adress)
