from dependency_injector import containers, providers

from Constants import Constants
from DatabaseComponents import DatabaseComponents
from GenerateDataObjectComponent import GenerateDataObjectComponent
from GenerateJson import GenerateJson
from Logger import Logger


class CoreProviders(containers.DeclarativeContainer):
    config = providers.Configuration()
    generatejson = providers.Factory(GenerateJson)
    generatedataobjectcomponent = providers.Factory(GenerateDataObjectComponent)
    logger = providers.Factory(Logger)
    databasecomponent = providers.Factory(DatabaseComponents, logger=logger)


