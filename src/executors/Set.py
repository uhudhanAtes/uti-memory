
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Memory.src.utils.response import build_response_set
from components.Memory.src.models.PackageModel import PackageModel


class Set(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.input_data = self.request.get_param("inputData")
        self.key = self.request.get_param("configKey")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        self.redis_db.redis_set_flag(self.key, self.input_data)
        self.data = []
        packageModel = build_response_set(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()