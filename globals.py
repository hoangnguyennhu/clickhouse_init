from asyncio.windows_events import NULL
from http import server
from re import T
from sqlalchemy import create_engine, Column, MetaData
import csv
import pandas
from datetime import datetime
from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import client, engine, session

from clickhouse_sqlalchemy import MaterializedView, select

# from test import MtDealTable, MatView, MtDealTableOther
from table.mt_deal_table import MtDealTable
from table.mt_account_balance_table import  MtAccountBalanceTable
from table.account_properties_table import AccountPropertiesTable
from table.mt_account_equity_table import   MtAccountEquityTable


from table.daily_balance import metric__daily_balance, metric__daily_balance_mv
from table.daily_equity import metric__daily_equity, metric__daily_equity_mv
from table.extrema_balance import metric__extrema_balance, metric__extrema_balance_mv
from table.extrema_equity import metric__extrema_equity, metric__extrema_equity_mv
from table.max_absolute_balance_drawdown import MaxAbsoluteBalanceDrawdown, metric__max_absolute_balance_drawdown_mv
from table.max_daily_balance_drawdown import MaxDailyBalanceDrawdown, metric__max_daily_balance_drawdown_mv
from table.max_daily_equity_drawdown import	MaxDailyEquityDrawdown, metric__max_daily_equity_drawdown_mv
from table.max_relative_balance_drawdown import metric__max_relative_balance_drawdown, metric__max_relative_balance_drawdown_mv
from table.oa_balance_drawdown import OABalanceDrawdown, metric__oa_balance_drawdown_mv
from table.oa_equity_drawdown import OAEquityDrawdown, metric__oa_equity_drawdown_mv
from table.or_balance_drawdown import ORBalanceDrawdown, metric__or_balance_drawdown_mv
from table.or_equity_drawdown import OREquityDrawdown, metric__or_equity_drawdown_mv
from table.ra_stopout_level_add import RAStopoutLevelADD, metric__ra_stopout_level_add_mv



# base tables
if not engine.dialect.has_table(engine, MtDealTable.__tablename__):
    MtDealTable.__table__.create()
if not engine.dialect.has_table(engine, MtAccountBalanceTable.__tablename__):
    MtAccountBalanceTable.__table__.create()	
if not engine.dialect.has_table(engine, AccountPropertiesTable.__tablename__):
    AccountPropertiesTable.__table__.create()
if not engine.dialect.has_table(engine, MtAccountEquityTable.__tablename__):
    MtAccountEquityTable.__table__.create()
			
# create metric tables
if not engine.dialect.has_table(engine, "metric__daily_balance"):
	client.execute(metric__daily_balance)
if not engine.dialect.has_table(engine, "metric__daily_equity"):
	client.execute(metric__daily_equity)
if not engine.dialect.has_table(engine, "metric__extrema_balance"):
	client.execute(metric__extrema_balance)
if not engine.dialect.has_table(engine, "metric__extrema_equity"):
	client.execute(metric__extrema_equity)
if not engine.dialect.has_table(engine, MaxAbsoluteBalanceDrawdown.__tablename__):
    MaxAbsoluteBalanceDrawdown.__table__.create()
if not engine.dialect.has_table(engine, MaxDailyBalanceDrawdown.__tablename__):
    MaxDailyBalanceDrawdown.__table__.create()	
if not engine.dialect.has_table(engine, MaxDailyEquityDrawdown.__tablename__):
    MaxDailyEquityDrawdown.__table__.create()	
if not engine.dialect.has_table(engine, "metric__max_relative_balance_drawdown"):
	client.execute(metric__max_relative_balance_drawdown)
if not engine.dialect.has_table(engine, OABalanceDrawdown.__tablename__):
    OABalanceDrawdown.__table__.create()	
if not engine.dialect.has_table(engine, OAEquityDrawdown.__tablename__):
    OAEquityDrawdown.__table__.create()
if not engine.dialect.has_table(engine, ORBalanceDrawdown.__tablename__):
    ORBalanceDrawdown.__table__.create()
if not engine.dialect.has_table(engine, OREquityDrawdown.__tablename__):
    OREquityDrawdown.__table__.create()
if not engine.dialect.has_table(engine, RAStopoutLevelADD.__tablename__):
    RAStopoutLevelADD.__table__.create()

# create materializer views
if not engine.dialect.has_table(engine, "metric__daily_balance_mv"):
	client.execute(metric__daily_balance_mv)
if not engine.dialect.has_table(engine, "metric__daily_equity_mv"):
	client.execute(metric__daily_equity_mv)
if not engine.dialect.has_table(engine, "metric__extrema_balance_mv"):
	client.execute(metric__extrema_balance_mv)
if not engine.dialect.has_table(engine, "metric__extrema_equity_mv"):
	client.execute(metric__extrema_equity_mv)
if not engine.dialect.has_table(engine, "metric__max_absolute_balance_drawdown_mv"):
	client.execute(metric__max_absolute_balance_drawdown_mv)
if not engine.dialect.has_table(engine, "metric__max_daily_balance_drawdown_mv"):
	client.execute(metric__max_daily_balance_drawdown_mv)
if not engine.dialect.has_table(engine, "metric__max_daily_equity_drawdown_mv"):
	client.execute(metric__max_daily_equity_drawdown_mv)
if not engine.dialect.has_table(engine, "metric__max_relative_balance_drawdown_mv"):
	client.execute(metric__max_relative_balance_drawdown_mv)
if not engine.dialect.has_table(engine, "metric__oa_balance_drawdown_mv"):
	client.execute(metric__oa_balance_drawdown_mv)
if not engine.dialect.has_table(engine, "metric__oa_equity_drawdown_mv"):
	client.execute(metric__oa_equity_drawdown_mv)
if not engine.dialect.has_table(engine, "metric__ra_stopout_level_add_mv"):
	client.execute(metric__ra_stopout_level_add_mv)
if not engine.dialect.has_table(engine, "metric__or_balance_drawdown_mv"):
	client.execute(metric__or_balance_drawdown_mv)
if not engine.dialect.has_table(engine, "metric__or_equity_drawdown_mv"):
	client.execute(metric__or_equity_drawdown_mv)

with open(r"C:\Users\iboy7\OneDrive - EAERA Ltd\Desktop\Clickhouse\data_insert\account_properties_table.csv") as file_obj:
		# Create reader object by passing the file 
		# object to reader method
		reader_obj = csv.reader(file_obj)
		
		# Iterate over each row in the csv 
		# file using reader object

		for index, row in enumerate(reader_obj):
			if index == 0:
				continue
			table_row = {
				"Server": str(row[0]),
				"Login": int(row[1]),
				"Program": str(row[2]),
				"Level": str(row[3]),
				"AccountType": str(row[4]),
				"RegistrationDate": datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S'),
				"InitialDeposit": float(row[6]),
				"Leverage": int(row[7]),
				"Currency": str(row[8]),
				"ProfitTarget": float(row[9]),
				"MaxLoss": float(row[10]),
				"MaxDailyDrawdown": float(row[11]),
				"MinATD": int(row[12]),
				"PositionRisk": float(row[13]),
				"MaxViolations": int(row[14]),
				"TimeLimit": int(row[15]),
				"ExpiryDate": datetime.strptime(row[16], '%Y-%m-%d %H:%M:%S'),
				"ProfitShare": float(row[17]),
				"OutlierLogic": int(row[18])
			}
			session.execute(AccountPropertiesTable.__table__.insert(), table_row)

with open(r"C:\Users\iboy7\OneDrive - EAERA Ltd\Desktop\Clickhouse\data_insert\mt_deal_table.csv") as file_obj:
		# Create reader object by passing the file 
		# object to reader method
		reader_obj = csv.reader(file_obj)
		
		# Iterate over each row in the csv 
		# file using reader object

		for index, row in enumerate(reader_obj):
			if index == 0:
				continue
			table_row = {
				"Server": str(row[0]),
				"ExternalId": int(row[1]),
				"Timestamp": datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f'),
				"OpenTime": NULL,
				"Login": int(row[4]),
				"Dealer": int(row[5]),
				"Action": int(row[6]),
				"Symbol": str(row[7]),
				"Digits": int(row[8]),
				"DigitsCurrency": int(row[9]),
				"Volume": float(row[10]),
				"OpenPrice": float(row[11]),
				"Reason": int(row[12]),
				"Comment": str(row[13]),
				"Raw": str(row[14]),
				"OrderId": int(row[15]),
				"OpenTradeId": int(row[16]),
				"ClosePrice": float(row[17]),
				"CloseVolume": float(row[18]), 
				"CloseTime": datetime.strptime(row[19], '%Y-%m-%d %H:%M:%S.%f'),
				"Entry": int(row[20]),
				"Profit": float(row[21]), 
				"ContractSize": float(row[22]),
				"Storage": float(row[23]),
				"Commission": float(row[24]),
				"Fee": float(row[25])
			}
			session.execute(MtDealTable.__table__.insert(), table_row)

with open(r"C:\Users\iboy7\OneDrive - EAERA Ltd\Desktop\Clickhouse\data_insert\mt_account_balance_table.csv") as file_obj:
		# Create reader object by passing the file 
		# object to reader method
		reader_obj = csv.reader(file_obj)
		
		# Iterate over each row in the csv 
		# file using reader object

		for index, row in enumerate(reader_obj):
			if index == 0:
				continue
			table_row = {
				"Server": str(row[0]),
				"Currency": str(row[1]),
				"Group": str(row[2]),
				"Timestamp": datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f'),
				"Login": int(row[3]),
				"TotalBalance": float(row[5]),
				"Credit": float(row[6]),
				"Margin": float(row[7]),
				"Leverage": int(row[8]),
				"Equity": float(row[9]),
				"MarginFree": float(row[10]),
				"MarginLevel": float(row[11]),
				"Storage": float(row[12]),
				"Floating": float(row[13]),
                "Commission": float(row[14])
			}
			session.execute(MtAccountBalanceTable.__table__.insert(), table_row)

with open(r"C:\Users\iboy7\OneDrive - EAERA Ltd\Desktop\Clickhouse\data_insert\mt_account_equity_table.csv") as file_obj:
		# Create reader object by passing the file 
		# object to reader method
		reader_obj = csv.reader(file_obj)
		
		# Iterate over each row in the csv 
		# file using reader object

		for index, row in enumerate(reader_obj):
			if index == 0:
				continue
			table_row = {
				"Server": str(row[0]),
				"Currency": str(row[1]),
				"Group": str(row[2]),
				"Timestamp": datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f'),
				"Login": int(row[3]),
				"TotalBalance": float(row[5]),
				"Credit": float(row[6]),
				"Margin": float(row[7]),
				"Leverage": int(row[8]),
				"Equity": float(row[9]),
				"MarginFree": float(row[10]),
				"MarginLevel": float(row[11]),
				"Storage": float(row[12]),
				"Floating": float(row[13]),
                "Commission": float(row[14])
			}
			session.execute(MtAccountEquityTable.__table__.insert(), table_row)





res = client.execute("SHOW TABLES IN cti")
print(res)

# res = client.execute("SELECT * FROM cti.account_properties_table")
# print(res)