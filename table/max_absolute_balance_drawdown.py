from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import *




class MaxAbsoluteBalanceDrawdown(Base):
    __tablename__ = 'metric__max_absolute_balance_drawdown'

    MaxAbsolute = Column(types.Float64)
    Login = Column(types.UInt64, primary_key=True)
    Server = Column(types.String, primary_key=True)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server)
        ),
    )

metric__max_absolute_balance_drawdown_mv =      ('CREATE MATERIALIZED VIEW cti.metric__max_absolute_balance_drawdown_mv TO cti.metric__max_absolute_balance_drawdown '
                                                'AS SELECT MaxAbsolute, Server, Login '
                                                'FROM '
                                                '( '
                                                'SELECT b.InitialDeposit - a.MinBalance as MaxAbsolute, a.Server as Server, a.Login as Login '
                                                'FROM cti.metric__extrema_balance as a LEFT JOIN cti.account_properties_table as b ON a.Login = b.Login AND a.Server = b.Server ' 
                                                ') ')