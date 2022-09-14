from locale import currency
from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from clickhouse import *


class MtAccountEquityTable(Base):
    __tablename__ = 'mt_account_equity_table'

    Server = Column(types.String, primary_key=True)
    Currency = Column(types.String)
    Group = Column(types.String)
    Timestamp = Column(types.DateTime64(3), primary_key=True)
    Login = Column(types.UInt64, primary_key=True)
    TotalBalance = Column(types.Float64)
    Credit = Column(types.Float64)
    Margin = Column(types.Float64)
    Leverage = Column(types.UInt16)
    Equity = Column(types.Float64)
    MarginFree = Column(types.Float64)
    MarginLevel = Column(types.Float64)
    Storage = Column(types.Float64)
    Floating = Column(types.Float64)
    Commission = Column(types.Float64)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server, Timestamp)
        ),
    )


# class MtAccountEquity(Base):
#     __tablename__ = 'mt_account_equity'

#     Server = Column(types.String, primary_key=True)
#     Login = Column(types.Int32, primary_key=True)

#     Currency = Column(types.String)
#     Group = Column(types.String)
#     Timestamp = Column(types.DateTime64(3))
#     TotalBalance = Column(types.Float64)
#     Margin = Column(types.Float64)
#     Leverage = Column(types.UInt16)
#     Equity = Column(types.Float64)
#     MarginFree = Column(types.Float64)
#     MarginLevel = Column(types.Float64)
#     Storage = Column(types.Float64)
#     Floating = Column(types.Float64)

#     __table_args__ = (
#         engines.Kafka(
#             broker_list=BROKER_LIST,
#             topic_list = '',
#             group_name = '',
#             format = FORMAT,
#             avro_schema_registry_url = AVRO_SCHEMA_REGISTRY_URL
#         )
#     )

# from clickhouse_sqlalchemy import MaterializedView, select

# MtAccountEquityMv = MaterializedView(MtAccountEquityTable, select([
#     MtAccountEquity.Server.label('Server'),
#     MtAccountEquity.Login.label('Login'),
#     MtAccountEquity.Currency.label('Currency'),
#     MtAccountEquity.Group.label('Group'),
#     MtAccountEquity.Timestamp.label('Timestamp'),
#     MtAccountEquity.TotalBalance.label('TotalBalance'),
#     MtAccountEquity.Margin.label('Margin'),
#     MtAccountEquity.Leverage.label('Leverage'),
#     MtAccountEquity.Equity.label('Equity'),
#     MtAccountEquity.MarginFree.label('MarginFree'),
#     MtAccountEquity.MarginLevel.label('MarginLevel'),
#     MtAccountEquity.Storage.label('Storage'),
#     MtAccountEquity.Floating.label('Floating')
# ]))