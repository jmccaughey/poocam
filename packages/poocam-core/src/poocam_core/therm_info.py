from dataclasses import dataclass, asdict, field
import json
import time

def current_time_ms() -> int:
    return round(time.time() * 1000)

@dataclass(frozen=True)
class ThermInfo:
    values: list[list[float]]
    ts: int = field(default_factory=current_time_ms)

    def to_json(self) -> str:
        return json.dumps(asdict(self), separators=(',', ':'))