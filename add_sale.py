import sys
from task_6_6 import write_bekery

if len(sys.argv) == 2:
    write_bekery(sys.argv[1])
else:
    print('Введены не корректные данные')