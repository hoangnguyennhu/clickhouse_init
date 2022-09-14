from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import *



metric__max_relative_balance_drawdown =     ('CREATE TABLE cti.metric__max_relative_balance_drawdown '
                                            '( '
                                            'MaxRelativeBalanceDrawdown SimpleAggregateFunction(max, Float64), '
                                            'Login  UInt64, '
                                            'Server String '
                                            ') ENGINE = AggregatingMergeTree() '
                                            'ORDER BY (Login, Server)')

metric__max_relative_balance_drawdown_mv =  ('CREATE MATERIALIZED VIEW cti.metric__max_relative_balance_drawdown_mv TO cti.metric__max_relative_balance_drawdown '
                                            'AS SELECT max(OverallRelative) as MaxRelativeBalanceDrawdown, Login, Server '
                                            'FROM cti.metric__or_balance_drawdown '
                                            'GROUP BY Login, Server')