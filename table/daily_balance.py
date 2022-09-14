from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import *


metric__daily_balance =     ('CREATE TABLE IF NOT EXISTS cti.metric__daily_balance ' 
                            '( '
                            'LastBalance Float64, '
                            'MaxBalance SimpleAggregateFunction(max, Float64), '
                            'MinBalance SimpleAggregateFunction(min, Float64), '
                            'Timestamp_day DateTime64(3), '
                            'Server String, '
                            'Login UInt64 '
                            ') '
                            'ENGINE = AggregatingMergeTree() '
                            'ORDER BY (Login, Server, Timestamp_day)')

metric__daily_balance_mv = ('CREATE MATERIALIZED VIEW cti.metric__daily_balance_mv TO cti.metric__daily_balance '
                            'AS SELECT '  
                            'argMax(TotalBalance, Timestamp) as LastBalance, '
                            'max(TotalBalance) as MaxBalance, '
                            'min(TotalBalance) as MinBalance, '
                            'toStartOfDay(Timestamp) as Timestamp_day, '
                            'Server as Server, ' 
                            'Login as Login '
                            'FROM cti.mt_account_balance_table ' 
                            'GROUP BY Login, Server, Timestamp_day ')


