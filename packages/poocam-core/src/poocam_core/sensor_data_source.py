from abc import ABC, abstractmethod
from typing import List
import socket
import time

from poocam_core.interpolator import Interpolator
from poocam_core.sensor_data_formatter import SensorDataFormatter
from poocam_core.truncator import Truncator


class SensorDataSource(ABC):
    def __init__(self, host: str = "0.0.0.0", port: int = 9090, zoom: int = 1) -> None:
        self.sensor_data_formatter: SensorDataFormatter = SensorDataFormatter()
        self.socket: socket.socket | None = None
        self.stop_requested = False
        self.host = host
        self.port = port
        if zoom > 1:
            self.interpolator = Interpolator(zoom, zoom)
        else:
            self.interpolator = None
        self.truncator = Truncator()

    @abstractmethod
    def read(self) -> List[List[float]]:
        pass

    def handle_client(self, conn, addr):
        print(f"Connected by {addr}")
        try:
            while True:
                sensor_data: list[list[float]] = self.read()
                # TODO: truncate floats to one decimal place
                if self.interpolator:
                    sensor_data = self.interpolator.interpolate(sensor_data)
                self.truncator.truncate(sensor_data)
                formatted_data: str = self.sensor_data_formatter.format_sensor_data(sensor_data)
                conn.sendall(formatted_data.encode())
                time.sleep(.15) # the back pressure. Otherwise, reads get into tight loop
        except (OSError, socket.error) as e:
            print(f"Error with client {addr}: {e}")
        finally:
            print(f"Client {addr} disconnected.")
            conn.close()

    def stop_server(self):
        self.stop_requested = True
        self.socket.close()

    def serve(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            self.socket = s
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows immediate reuse of the address
            try:
                s.bind((self.host, self.port))
                s.listen()
                print(f"Server listening on {self.host}:{self.port}")
                while not self.stop_requested:
                    try:
                        conn, addr = s.accept()
                        self.handle_client(conn, addr)
                    except (socket.error) as e:
                        print(f"Error accepting connection: {e}")
                        # The server will continue to listen for new connections
                    except KeyboardInterrupt:
                        print("Server shutting down...")
                        break
            except (OSError, socket.error) as e:
                print(f"Server binding or listening error: {e}")
            finally:
                s.close()
