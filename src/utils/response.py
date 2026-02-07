
from sdks.novavision.src.helper.package import PackageHelper
from components.Memory.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, GetOutputs, GetResponse, GetExecutor, SetOutputs, SetResponse, SetExecutor, OutputData


def build_response_get(context):
    outputData = OutputData(value=context.data)
    outputs = GetOutputs(outputData=outputData)
    packageResponse = GetResponse(outputs=outputs)
    packageExecutor = GetExecutor(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel


def build_response_set(context):
    outputData = OutputData(value=context.data)
    outputs = SetOutputs(outputData=outputData)
    packageResponse = SetResponse(outputs=outputs)
    packageExecutor = SetExecutor(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
