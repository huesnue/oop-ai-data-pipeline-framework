from framework.core.pipeline_component import PipelineComponent
from framework.core.descriptors import ChoiceField

class SimpleTransformer(PipelineComponent):
    mode = ChoiceField(choices=["upper", "lower"], default="upper")

    def run(self, data):
        if data is None:
            return None

        if self.mode == "upper":
            return [str(x).upper() for x in data]
        if self.mode == "lower":
            return [str(x).lower() for x in data]
