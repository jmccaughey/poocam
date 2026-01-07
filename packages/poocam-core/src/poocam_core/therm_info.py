from dataclasses import dataclass, asdict, field
import json
import time

@dataclass(frozen=True)
class ThermInfo:
    values: list[list[float]]
    epoch: float = field(default_factory=time.time)

    def to_json(self) -> str:
        return json.dumps(asdict(self), separators=(',', ':'))