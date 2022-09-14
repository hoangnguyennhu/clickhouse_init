from clickhouse import *
client.execute('DROP DATABASE cti')
res = client.execute('SHOW DATABASES')
print(res)