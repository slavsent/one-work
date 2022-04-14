import sys
from task_6_6 import read_bekery

if len(sys.argv) == 1:
    read_bekery()
elif len(sys.argv) == 2:
    read_bekery(sys.argv[1])
elif len(sys.argv) == 3:
    read_bekery(sys.argv[1], sys.argv[2])
else:
    print('Введены не корректные данные')