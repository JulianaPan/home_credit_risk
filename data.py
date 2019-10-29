import MySQLdb

host = 'db1.ceobypqfxmry.us-east-2.rds.amazonaws.com'
port = '3306'
db = 'db'
user = 'admin'
password = 'msbd5001'
connection = MySQLdb.Connect(host, user, password, db)
tb = 'credit_card_balance'
query_list = [
    'SK_ID_CURR',
    "sum(NAME_CONTRACT_STATUS = 'Active') / count(NAME_CONTRACT_STATUS)        as NAME_CONTRACT_STATUS_active",
    "sum(NAME_CONTRACT_STATUS = 'Completed') / count(NAME_CONTRACT_STATUS)     as NAME_CONTRACT_STATUS_completed",
    "sum(NAME_CONTRACT_STATUS = 'Demand') / count(NAME_CONTRACT_STATUS)        as NAME_CONTRACT_STATUS_demand",
    "sum(NAME_CONTRACT_STATUS = 'Signed') / count(NAME_CONTRACT_STATUS)        as NAME_CONTRACT_STATUS_signed",
    "sum(NAME_CONTRACT_STATUS = 'Sent proposal') / count(NAME_CONTRACT_STATUS) as NAME_CONTRACT_STATUS_sent_proposal",
    "sum(NAME_CONTRACT_STATUS = 'Refused') / count(NAME_CONTRACT_STATUS)       as NAME_CONTRACT_STATUS_refused",
    "sum(NAME_CONTRACT_STATUS = 'Approved') / count(NAME_CONTRACT_STATUS)      as NAME_CONTRACT_STATUS_approved"
]

funcs = ['min({}) as {}_{}_min', 'max({}) as {}_{}_max', 'avg({}) as {}_{}_avg', 'std({}) as {}_{}_std']
cols = [
    'AMT_BALANCE',
    'AMT_CREDIT_LIMIT_ACTUAL',
    'AMT_DRAWINGS_ATM_CURRENT',
    'AMT_DRAWINGS_CURRENT',
    'AMT_DRAWINGS_OTHER_CURRENT',
    'AMT_DRAWINGS_POS_CURRENT',
    'AMT_INST_MIN_REGULARITY',
    'AMT_PAYMENT_CURRENT',
    'AMT_PAYMENT_TOTAL_CURRENT',
    'AMT_RECEIVABLE_PRINCIPAL',
    'AMT_RECIVABLE',
    'AMT_TOTAL_RECEIVABLE',
    'CNT_DRAWINGS_ATM_CURRENT',
    'CNT_DRAWINGS_CURRENT',
    'CNT_DRAWINGS_OTHER_CURRENT',
    'CNT_DRAWINGS_POS_CURRENT',
    'CNT_INSTALMENT_MATURE_CUM',
]
query_list.extend(func.format(col, tb, col) for col in cols for func in funcs)

# IMPORTANT! change the name of new table
query = 'create table ccb_attr select ' + ', '.join(query_list) + ' from ' + tb + ' group by ' + 'SK_ID_CURR'
print(query)
connection.query(query)
connection.close()
