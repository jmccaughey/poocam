from poocam_core.therm_info import ThermInfo


class JsonWrapper:
    def wrap(self, data: list[list[float]]) -> str:
        info: ThermInfo = ThermInfo(data)
        return info.to_json()
