from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import *


metric__daily_equity =      ('CREATE TABLE IF NOT EXISTS cti.metric__daily_equity '
                            '( '
                            'LastEquity Float64, '
                            'MaxEquity SimpleAggregateFunction(max, Float64), '
                            'MinEquity SimpleAggregateFunction(min, Float64), '
                            'Timestamp_day DateTime64(3), ' 
                            'Server String, '
                            'Login UInt64 '
                            ') '
                            'ENGINE = AggregatingMergeTree() '
                            'ORDER BY (Login, Server, Timestamp_day)')

metric__daily_equity_mv =   ('CREATE MATERIALIZED VIEW cti.metric__daily_equity_mv TO cti.metric__daily_equity '
                            'AS SELECT '
                            'argMax(Equity, Timestamp) as LastEquity, '
                            'max(Equity) as MaxEquity, '
                            'min(Equity) as MinEquity, '
                            'toStartOfDay(Timestamp) as Timestamp_day, '
                            'Server as Server, '
                            'Login as Login '
                            'FROM cti.mt_account_equity_table '
                            'GROUP BY Login, Server, Timestamp_day')


