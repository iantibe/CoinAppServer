from dependency_injector import containers, providers

from DatabaseTransactions import DatabaseTransactions
from Transaction import Transaction


class TransactionProviders(containers.DeclarativeContainer):
    config = providers.Configuration()
    coreproviders = providers.DependenciesContainer()
    databasetransactions = providers.Factory(DatabaseTransactions,dbc=coreproviders.databasecomponent, log=coreproviders.logger)
    transaction = providers.Factory(Transaction, databasetransactions=databasetransactions)
