from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import *


metric__extrema_balance =   ('CREATE TABLE IF NOT EXISTS cti.metric__extrema_balance '
                            '( '
                            'MaxBalance SimpleAggregateFunction(max, Float64), '
                            'MinBalance SimpleAggregateFunction(min, Float64), '
                            'Server String, '
                            'Login UInt64 '
                            ') '
                            'ENGINE = AggregatingMergeTree() '
                            'ORDER BY (Login, Server) ')

metric__extrema_balance_mv = ('CREATE MATERIALIZED VIEW cti.metric__extrema_balance_mv TO cti.metric__extrema_balance '
                            'AS SELECT '  
                            'max(TotalBalance) as MaxBalance, min(TotalBalance) as MinBalance, Server as Server, Login as Login '
                            'FROM cti.mt_account_balance_table ' 
                            'GROUP BY Login, Server ')


