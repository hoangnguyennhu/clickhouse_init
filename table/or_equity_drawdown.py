from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from clickhouse import *


class OREquityDrawdown(Base):
    __tablename__ = 'metric__or_equity_drawdown'

    OverallRelative = Column(types.Float64)
    Timestamp = Column(types.DateTime64(3))
    Login = Column(types.UInt64, primary_key=True)
    Server = Column(types.String, primary_key=True)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server)
        ),
    )

metric__or_equity_drawdown_mv  =   ('CREATE MATERIALIZED VIEW cti.metric__or_equity_drawdown_mv  TO  cti.metric__or_equity_drawdown '
                                    'AS SELECT argMax(OR, ts) as OverallRelative, max(ts) as Timestamp, Server, Login '
                                    'FROM ' 
                                    '( '
                                    'SELECT b.MaxBalance - a.Equity as OR, a.Timestamp as ts, a.Server as Server, a.Login as Login '
                                    'FROM cti.mt_account_equity_table as a LEFT JOIN cti.metric__extrema_balance as b ON a.Login = b.Login AND a.Server = b.Server ' 
                                    ') '
                                    'GROUP BY Login, Server ')