class PipelineError(Exception):
    """Raised when a pipeline stage fails processing an item."""

    def __init__(self, stage: str, index: int, original: Exception) -> None:
        super().__init__(f"Stage {stage} failed on item {index}: {original}")
        self.stage = stage
        self.index = index
        self.original = original
