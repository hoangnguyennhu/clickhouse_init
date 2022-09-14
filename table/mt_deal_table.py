from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from clickhouse import *




class MtDealTable(Base):
    __tablename__ = 'mt_deal_table'
    

    Server = Column(types.String, primary_key=True)
    ExternalId = Column(types.UInt64, primary_key=True)
    Timestamp = Column(types.DateTime64(3))
    OpenTime = Column(types.DateTime64(3), nullable=True)
    Login = Column(types.UInt64, primary_key=True)
    Dealer = Column(types.UInt64)
    Action = Column(types.UInt8)
    Symbol = Column(types.String)
    Digits = Column(types.UInt8)
    DigitsCurrency = Column(types.UInt8)
    Volume = Column(types.Float64)
    OpenPrice = Column(types.Float64)
    Reason = Column(types.UInt8)
    Comment = Column(types.String)
    Raw = Column(types.String)
    OrderId = Column(types.UInt64)
    OpenTradeId = Column(types.UInt64)
    ClosePrice = Column(types.Float64)
    CloseVolume = Column(types.Float64)
    CloseTime = Column(types.DateTime64(3))
    Entry = Column(types.UInt8)
    Profit = Column(types.Float64)
    ContractSize = Column(types.Float64)
    Storage = Column(types.Float64)
    Commission = Column(types.Float64)
    Fee = Column(types.Float64)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(ExternalId, Login, Server)
        ),
    )
# mt_deal =       ('CREATE TABLE IF NOT EXISTS {}.mt_deal '
#                 '( '
#                 'Server String, '
#                 'ExternalId UInt64, '
#                 'Timestamp DateTime64, '
#                 'OpenTime DateTime64, '
#                 'Login UInt64, '
#                 'Dealer UInt64, '
#                 'Action UInt8, '
#                 'Symbol String, '
#                 'Digits UInt8, '
#                 'DigitsCurrency UInt8, '
#                 'Volume Float64, '
#                 'OpenPrice Float64, '
#                 'Reason UInt8, '
#                 'Comment String, '
#                 'Raw String, '
#                 'OrderId UInt64, '
#                 'OpenTradeId UInt64, '
#                 'ClosePrice Float64, '
#                 'CloseVolume Float64, '
#                 'CloseTime DateTime64, '
#                 'Entry UInt8, '
#                 'Profit Float64, '
#                 'ContractSize Float64, '
#                 'Storage Float64, '
#                 'Commission Float64, '
#                 'Fee Float64 '
#                 ') ENGINE = Kafka() '
#                 'SETTINGS '
#                 'kafka_broker_list = \'{}\', '
#                 'kafka_topic_list = \'{}\', '
#                 'kafka_group_name = \'{}\', '
#                 'kafka_format = \'AvroConfluent\', '
#                 'format_avro_schema_registry_url = \'{}\' ')

# mt_deal_table = ('CREATE TABLE IF NOT EXISTS {}.mt_deal_table '
#                 '( '
#                 'Server String, '
#                 'ExternalId UInt64, '
#                 'Timestamp DateTime64, '
#                 'OpenTime DateTime64, '
#                 'Login UInt64, '
#                 'Dealer UInt64, '
#                 'Action UInt8, '
#                 'Symbol String, '
#                 'Digits UInt8, '
#                 'DigitsCurrency UInt8, '
#                 'Volume Float64, '
#                 'OpenPrice Float64, '
#                 'Reason UInt8, '
#                 'Comment String, '
#                 'Raw String, '
#                 'OrderId UInt64, '
#                 'OpenTradeId UInt64, '
#                 'ClosePrice Float64, '
#                 'CloseVolume Float64, '
#                 'CloseTime DateTime64, '
#                 'Entry UInt8, '
#                 'Profit Float64, '
#                 'ContractSize Float64, '
#                 'Storage Float64, '
#                 'Commission Float64, '
#                 'Fee Float64 '
#                 ') ENGINE = MergeTree() '
#                 'ORDER BY (ExternalId, Login, Server)')
# class MtDeal(Base):
#     __tablename__ = 'mt_deal'

#     Server = Column(types.String)
#     ExternalId = Column(types.UInt64)
#     Timestamp = Column(types.DateTime64(3))
#     OpenTime = Column(types.DateTime64(3), nullable=True)
#     Login = Column(types.Int32)
#     Dealer = Column(types.UInt64)
#     Action = Column(types.UInt8)
#     Symbol = Column(types.String)
#     Digits = Column(types.UInt8)
#     DigitsCurrency = Column(types.UInt8)
#     Volume = Column(types.Float64)
#     OpenPrice = Column(types.Float64)
#     Reason = Column(types.UInt8)
#     Comment = Column(types.String)
#     Raw = Column(types.String)
#     OrderId = Column(types.UInt64)
#     OpenTradeId = Column(types.UInt64)
#     ClosePrice = Column(types.Float64)
#     CloseVolume = Column(types.Float64)
#     CloseTime = Column(types.DateTime64(3))
#     Entry = Column(types.UInt8)
#     Profit = Column(types.Float64)
#     ContractSize = Column(types.Float64)
#     Storage = Column(types.Float64)
#     Commission = Column(types.Float64)
#     Fee = Column(types.Float64)

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

# MtDealMv = MaterializedView(MtDealTable, select([
#     MtDeal.Server.label('Server'),
#     MtDeal.ExternalId.label('ExternalId'),
#     MtDeal.Timestamp.label('Timestamp'),
#     MtDeal.OpenTime.label('OpenTime'),
#     MtDeal.Login.label('Login'),
#     MtDeal.Dealer.label('Dealer'),
#     MtDeal.Action.label('Action'),
#     MtDeal.Symbol.label('Symbol'),
#     MtDeal.Digits.label('Digits'),
#     MtDeal.DigitsCurrency.label('DigitsCurrency'),
#     MtDeal.Volume.label('Volume'),
#     MtDeal.OpenPrice.label('OpenPrice'),
#     MtDeal.Reason.label('Reason'),
#     MtDeal.Comment.label('Comment'),
#     MtDeal.Raw.label('Raw'),
#     MtDeal.OrderId.label('OrderId'),
#     MtDeal.OpenTradeId.label('OpenTradeId'),
#     MtDeal.ClosePrice.label('ClosePrice'),
#     MtDeal.CloseVolume.label('CloseVolume'),
#     MtDeal.CloseTime.label('CloseTime'),
#     MtDeal.Entry.label('Entry'),
#     MtDeal.Profit.label('Profit'),
#     MtDeal.ContractSize.label('ContractSize'),
#     MtDeal.Storage.label('Storage'),
#     MtDeal.Commission.label('Commission'),
#     MtDeal.Fee.label('Fee')
# ]))