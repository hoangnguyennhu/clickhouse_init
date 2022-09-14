from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)
from clickhouse import *




class MaxDailyEquityDrawdown(Base):
    __tablename__ = 'metric__max_daily_equity_drawdown'

    MaxDailyEquityDrawdown = Column(types.Float64)
    Timestamp_day = Column(types.DateTime64(3))
    Login = Column(types.UInt64, primary_key=True)
    Server = Column(types.String, primary_key=True)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server)
        ),
    )

metric__max_daily_equity_drawdown_mv =  ('CREATE MATERIALIZED VIEW cti.metric__max_daily_equity_drawdown_mv TO cti.metric__max_daily_equity_drawdown '
                                        'AS SELECT MaxDailyEquityDrawdown, Timestamp_day, Server, Login '
                                        'FROM ' 
                                        '( ' 
                                        'SELECT b.LastBalance - a.MinDayEquity as MaxDailyEquityDrawdown, a.Ts_day as Timestamp_day, a.Server as Server, a.Login as Login '
                                        'FROM '
                                        '( ' 
                                        '    SELECT Server, Login, toStartOfDay(Timestamp) as Ts_day, subtractDays(Ts_day, 1) as Yesterday, min(Equity) as MinDayEquity '
                                        '    FROM cti.mt_account_equity_table '
                                        '    WHERE toStartOfDay(Timestamp) = toStartOfDay(now()) '
                                        '    GROUP BY Login, Server, Ts_day '
                                        ') as a '
                                        'LEFT JOIN cti.metric__daily_balance as b '
                                        'ON a.Login = b.Login AND a.Server = b.Server AND a.Yesterday = b.Timestamp_day '
                                        ') ')