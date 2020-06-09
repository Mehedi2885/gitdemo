# import gzip
# from subprocess import Popen, PIPE
# from sys import path
#
# cmd = "mysqldump --user=root --password=Hassan2885 demo".format(**locals())
# p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
# with gzip.open(path, "wb") as f:
#     f.writelines(p.stdout)
#

from subprocess import Popen
# proc = Popen('mysqldump -h localhost -P 3306 -u root -pHassan2885 demo > ~/mysqldump.sql', shell=True)
proc = Popen('mysqldump -h 127.0.0.1 -u root -pHassan2885 demo > /Users/mehedihassan/Projects/mysql_backup.sql', shell=True)
import os
print(__file__)
print(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.abspath(os.path.dirname(__file__)))