
import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Memory.src.utils.response import build_response_get
from components.Memory.src.models.PackageModel import PackageModel


class Get(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.key = self.request.get_param("configKey")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def try_parse_json(self, value):
        if value is None:
            return None
        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return value

    def run(self):
        self.data = self.try_parse_json(self.redis_db.redis_get_flag(self.key)) or []
        packageModel = build_response_get(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()