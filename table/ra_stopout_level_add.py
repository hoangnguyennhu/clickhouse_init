from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from clickhouse import *


class RAStopoutLevelADD(Base):
    __tablename__ = 'metric__ra_stopout_level_add'

    Relative = Column(types.Float64)
    Absolute = Column(types.Float64)
    Login = Column(types.UInt64, primary_key=True)
    Server = Column(types.String, primary_key=True)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server)
        ),
    )

metric__ra_stopout_level_add_mv =   ('CREATE MATERIALIZED VIEW cti.metric__ra_stopout_level_add_mv TO cti.metric__ra_stopout_level_add ' 
                                    'AS SELECT Relative, Absolute, Server, Login '
                                    'FROM ' 
                                    '( ' 
                                    'SELECT a.MaxBalance - b.MaxLoss as Relative, b.InitialDeposit - b.MaxLoss as Absolute, a.Server as Server, a.Login as Login '
                                    'FROM cti.metric__extrema_balance as a LEFT JOIN cti.account_properties_table as b ON a.Login = b.Login AND a.Server = b.Server ' 
                                    ') ')