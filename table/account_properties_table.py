from locale import currency
from sqlalchemy import create_engine, Column, MetaData
from clickhouse_sqlalchemy import MaterializedView, select

from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

# from clickhouse import *
from clickhouse import *


class AccountPropertiesTable(Base):
    __tablename__ = 'account_properties_table'


    Server = Column(types.String, primary_key=True)
    Login = Column(types.UInt64, primary_key=True)
    Program = Column(types.String)
    Level = Column(types.String)
    AccountType = Column(types.String)
    RegistrationDate = Column(types.DateTime64(3))
    InitialDeposit = Column(types.Float64)
    Leverage = Column(types.UInt16)
    Currency = Column(types.String)
    ProfitTarget = Column(types.Float64)
    MaxLoss = Column(types.Float64)
    MaxDailyDrawdown = Column(types.Float64)
    MinATD = Column(types.UInt16)
    PositionRisk = Column(types. Float64)
    MaxViolations = Column(types.UInt16)
    TimeLimit = Column(types.UInt16)
    ExpiryDate = Column(types.DateTime64(3))
    ProfitShare = Column(types.Float64)
    OutlierLogic = Column(types.UInt8)

    __table_args__ = (
        engines.ReplacingMergeTree(
            order_by=(Login, Server)
        ),
    )

# class AccountProperties(Base):
#     __tablename__ = 'account_properties'


#     Server = Column(types.String, primary_key=True)
#     Login = Column(types.UInt64, primary_key=True)
#     Program = Column(types.String)
#     Level = Column(types.String)
#     AccountType = Column(types.String)
#     RegistrationDate = Column(types.DateTime64(3))
#     InitialDeposit = Column(types.Float64)
#     Leverage = Column(types.UInt16)
#     Currency = Column(types.String)
#     ProfitTarget = Column(types.Float64)
#     MaxLoss = Column(types.Float64)
#     MaxDailyDrawdown = Column(types.Float64)
#     MinATD = Column(types.UInt16)
#     PositionRisk = Column(types. Float64)
#     MaxViolations = Column(types.UInt16)
#     TimeLimit = Column(types.UInt16)
#     ExpiryDate = Column(types.DateTime64(3))
#     ProfitShare = Column(types.Float64)
#     OutlierLogic = Column(types.UInt8)

#     __table_args__ = (
#         engines.Kafka(
#             broker_list=BROKER_LIST,
#             topic_list = '',
#             group_name = '',
#             format = FORMAT,
#             avro_schema_registry_url = AVRO_SCHEMA_REGISTRY_URL
#         )
#     )

# MtAccountBalanceMv = MaterializedView(AccountPropertiesTable, select([
#     AccountProperties.Server.label('Server'),
#     AccountProperties.Login.label('Login'),
#     AccountProperties.Program.label('Program'),
#     AccountProperties.Level.label('Level'),
#     AccountProperties.AccountType.label('AccountType'),
#     AccountProperties.RegistrationDate.label('RegistrationDate'),
#     AccountProperties.InitialDeposit.label('InitialDeposit'),
#     AccountProperties.Leverage.label('Leverage'),
#     AccountProperties.Currency.label('Currency'),
#     AccountProperties.ProfitTarget.label('ProfitTarget'),
#     AccountProperties.MaxLoss.label('MaxLoss'),
#     AccountProperties.MaxDailyDrawdown.label('MaxDailyDrawdown'),
#     AccountProperties.MinATD.label('MinATD'),
#     AccountProperties.PositionRisk.label('PositionRisk'),
#     AccountProperties.MaxViolations.label('MaxViolations'),
#     AccountProperties.TimeLimit.label('TimeLimit'),
#     AccountProperties.ExpiryDate.label('ExpiryDate'),
#     AccountProperties.ProfitShare.label('ProfitShare'),
#     AccountProperties.OutlierLogic.label('OutlierLogic')
# ]))
