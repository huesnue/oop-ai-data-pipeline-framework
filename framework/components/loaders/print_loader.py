from framework.core.pipeline_component import PipelineComponent
from framework.core.descriptors import BoolField

class PrintLoader(PipelineComponent):
    enabled = BoolField(default=True)

    def run(self, data):
        if self.enabled:
            print("PrintLoader Output:", data)
        return data
