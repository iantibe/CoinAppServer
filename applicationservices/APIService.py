from dependency_injector import containers, providers

from applicationservices.CoreProviders import CoreProviders
from applicationservices.LogonProviders import LogonProviders
from applicationservices.TransactionProviders import TransactionProviders
from jsonincommingdefine.jsonlogout import jsonlogout



class APIService(containers.DeclarativeContainer):
    config = providers.Configuration()

    coreproviders = providers.Container(CoreProviders)

    transactionproviders = providers.Container(TransactionProviders, coreproviders=coreproviders)

    logonproviders = providers.Container(LogonProviders, coreproviders=coreproviders)


if __name__ == '__main__':
    ls = APIService()
    #print(ls.logonproviders.apinewuser().activate({"username": "ftibi", "password": "toyotacar", "firstname": "fsdf", "lastname": "fdsfsd"}, "4bbe7b23-1b5e-44f6-a9c0-f7c9fe0b234f"))
    print(ls.transactionproviders.transaction())



