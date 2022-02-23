import sys
from task_6_6 import edit_bekery_new

if len(sys.argv) == 3:
    edit_bekery_new(sys.argv[1], sys.argv[2])
else:
    print('Введены не корректные данные')