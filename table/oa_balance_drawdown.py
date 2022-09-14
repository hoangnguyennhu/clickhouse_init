from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from clickhouse import *


class OABalanceDrawdown(Base):
    __tablename__ = 'metric__oa_balance_drawdown'

    OverallAbsolute  = Column(types.Float64)
    Login = Column(types.UInt64, primary_key=True)
    Server = Column(types.String, primary_key=True)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server)
        ),
    )

metric__oa_balance_drawdown_mv =   ('CREATE MATERIALIZED VIEW cti.metric__oa_balance_drawdown_mv TO cti.metric__oa_balance_drawdown '
                                    'AS '
                                    'SELECT '
                                    'b.InitialDeposit - a.Balance as OverallAbsolute, '
                                    'a.Server as Server, '
                                    'a.Login as Login '
                                    'FROM '
                                    '( '
                                    'SELECT Server, Login, argMax(TotalBalance, Timestamp) as Balance  , max(Timestamp) as ts '
                                    'FROM cti.mt_account_balance_table '
                                    'GROUP BY Login , Server '
                                    ') as a LEFT JOIN cti.account_properties_table  as b ON a.Login = b.Login AND a.Server = b.Server ')