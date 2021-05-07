sqlsample ='''
select name  from T1 where  120 >age >100 ;  
'''

import sqlparse
import os
from PyQt5.QtSql import *
import re
parsql = sqlparse.parse(sqlsample

)
print(parsql)