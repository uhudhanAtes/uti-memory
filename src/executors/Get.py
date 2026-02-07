
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Memory.src.utils.response import build_response_get
from components.Memory.src.models.PackageModel import PackageModel


class Get(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.key = self.request.get_param("key")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        print(self.key)
        packageModel = build_response_get(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()