from dependency_injector import containers, providers

from APILogin import APILogin
from APILogout import APILogout
from APINewUser import APINewUser
from DatabaseLogon import DatabaseLogon

from HashComponents import HashComponents
from HashPassword import HashPassword




class LogonProviders(containers.DeclarativeContainer):
    config = providers.Configuration()
    coreproviders = providers.DependenciesContainer()
    databaselogon = providers.Factory(DatabaseLogon, databasecomponents=coreproviders.databasecomponent, log=coreproviders.logger)
    hashcomponents = providers.Factory(HashComponents)
    hashpassword = providers.Factory(HashPassword, hashcomponents=hashcomponents)
    apilogin = providers.Factory(APILogin, database=databaselogon, APIlogger=coreproviders.logger, log=coreproviders.logger, hash=hashpassword, generatejson=coreproviders.generatejson, generatedataobjectcomponent=coreproviders.generatedataobjectcomponent)
    apilogout = providers.Factory(APILogout,  database=databaselogon, log=coreproviders.logger, generatejson=coreproviders.generatejson,  generatedataobjectcomponent=coreproviders.generatedataobjectcomponent)
    apinewuser = providers.Factory(APINewUser, database=databaselogon, log=coreproviders.logger, generatejson=coreproviders.generatejson, hash=hashpassword, generatedataobjectcomponent=coreproviders.generatedataobjectcomponent)