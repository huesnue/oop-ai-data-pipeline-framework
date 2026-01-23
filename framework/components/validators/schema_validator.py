from framework.core.pipeline_component import PipelineComponent
from framework.core.descriptors import StringField

class SchemaValidator(PipelineComponent):
    expected_type = StringField(default="str")

    def run(self, data):
        if data is None:
            return None

        if self.expected_type == "str":
            if not all(isinstance(x, str) for x in data):
                raise ValueError("SchemaValidator: All items must be strings.")
        return data
