import MySQLdb
import pandas as pd
from sqlalchemy import create_engine

host = 'db1.ceobypqfxmry.us-east-2.rds.amazonaws.com'
port = '3306'
db = 'db'
user = 'admin'
password = 'msbd5001'

data_list = [
    # 'bureau_balance0',
    # 'credit_card_balance0',
    # 'installments_payments',
    # 'POS_CASH_balance',
    'previous_application',
]

for i in range(10,11):
    print(i)
    df = pd.read_csv('data/pre' + '%02d' % i)
    print(len(df))
    engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s") % (user, password, host, db))
    print(i)
    try:
        df.to_sql('previous_application', con=engine, if_exists='append', index=False)
    except Exception as e:
        print(e)
    print(i)
