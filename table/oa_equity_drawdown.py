from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from clickhouse import *

class OAEquityDrawdown(Base):
    __tablename__ = 'metric__oa_equity_drawdown'

    OverallAbsolute  = Column(types.Float64)
    Login = Column(types.UInt64, primary_key=True)
    Server = Column(types.String, primary_key=True)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server)
        ),
    )

metric__oa_equity_drawdown_mv =     ('CREATE MATERIALIZED VIEW cti.metric__oa_equity_drawdown_mv TO cti.metric__oa_equity_drawdown '
                                    'AS SELECT '
                                    'b.InitialDeposit - a.LastEquity as OverallAbsolute, '
                                    'a.Server as Server, '
                                    'a.Login as Login '
                                    'FROM ' 
                                    '( '
                                    'SELECT Server , Login , argMax(Equity , Timestamp ) as LastEquity, max(Timestamp) as Ts '
                                    'FROM cti.mt_account_equity_table GROUP BY Login, Server  '
                                    ') as a LEFT JOIN cti.account_properties_table  as b ON a.Login = b.Login AND a.Server = b.Server ')