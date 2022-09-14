from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import *




metric__extrema_equity =    ('CREATE TABLE cti.metric__extrema_equity '
                            '( '
                            'MaxEquity SimpleAggregateFunction(max, Float64), '
                            'MinEquity SimpleAggregateFunction(min, Float64), '
                            'Server String, '
                            'Login UInt64 '
                            ') '
                            'ENGINE = AggregatingMergeTree() '
                            'ORDER BY (Login, Server)')

metric__extrema_equity_mv = ('CREATE MATERIALIZED VIEW cti.metric__extrema_equity_mv TO cti.metric__extrema_equity '
                            'AS SELECT max(Equity) as MaxEquity, min(Equity) as MinEquity, Server as Server, Login as Login '
                            'FROM cti.mt_account_equity_table '
                            'GROUP BY Login, Server')


