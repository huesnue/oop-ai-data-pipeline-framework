from framework.core.pipeline_component import PipelineComponent
from framework.core.descriptors import IntField, ChoiceField

class DummyDataSource(PipelineComponent):
    batch_size = IntField(default=5, required=False)
    mode = ChoiceField(choices=["static", "range"], default="static")

    def run(self, data=None):
        if self.mode == "static":
            return ["A", "B", "C"][:self.batch_size]
        if self.mode == "range":
            return list(range(self.batch_size))
