
from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Configs, Outputs, Response, Request, Output, Input, Config


class InputData(Input):
    name: Literal["inputData"] = "inputData"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Data"


class OutputData(Output):
    name: Literal["outputData"] = "outputData"
    value: Union[list, dict]
    type: str = "object"

    class Config:
        title = "Data"


class ConfigKey(Config):
    """
        ...
    """
    name: Literal["configKey"] = "configKey"
    value: str = ""
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Key"
        json_schema_extra = {
            "shortDescription": "..."
        }


class SetInputs(Configs):
    inputData: InputData


class SetConfigs(Configs):
    configKey: ConfigKey


class SetOutputs(Outputs):
    outputData: OutputData


class GetConfigs(Configs):
    configKey: ConfigKey


class GetOutputs(Outputs):
    outputData: OutputData


class SetRequest(Request):
    inputs: Optional[SetInputs]
    configs: SetConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class SetResponse(Response):
    outputs: SetOutputs


class SetExecutor(Config):
    name: Literal["Set"] = "Set"
    value: Union[SetRequest, SetResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Set"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class GetRequest(Request):
    configs: GetConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class GetResponse(Response):
    outputs: GetOutputs


class GetExecutor(Config):
    name: Literal["Get"] = "Get"
    value: Union[GetRequest, GetResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Get"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    """
        (Description) ...
    """

    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[GetExecutor, SetExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    restart: Literal[True] = True

    class Config:
        title = "Mode"
        json_schema_extra = {"shortDescription": "..."}


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Memory"] = "Memory"