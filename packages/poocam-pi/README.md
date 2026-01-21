## How to Provision Raspberry Pi Zero

### Networking Over USB Cable
[see https://forums.raspberrypi.com/viewtopic.php?t=376578]


### Software Install
1. sudo apt-get update
1. sudo apt install git
1. curl -LsSf https://astral.sh/uv/install.sh | sh
1. sudo apt-get install python3.11
1. export UV_INDEX_URL=https://piwheels.org/simple
1. sudo apt-get install libopenblas-dev


raw history:
```
sudo apt-get update
   29  sudo apt install git
   30  git clone https://github.com/jmccaughey/poocam.git
   31  ls
   32  uv
   33  curl -LsSf https://astral.sh/uv/install.sh | sh
   34  uv run -m poocam_core.random_sensor_process
   35  source $HOME/.local/bin/env
   36  uv run -m poocam_core.random_sensor_process
   37  cd poocam/
   38  uv run -m poocam_core.random_sensor_process
   39  grep -rn 3.14 *
   40  uv python install 3.13
   41  uv python install 3.12
   42  uv python install 3.10
   43  uv python install 3.11
   44  uv python install 3
   45  sudo apt install python3.14
   46  sudo apt install python3.13
   47  error: No download found for request: cpython-3.13-linux-arm-gnueabihf
   48  uv python list --all-versions --all-arches --all-platforms
   49  uname -m
   50  lscpu
   51  uv help
   52  uv help list
   53  uv help python
   54  sudo apt-get install python3
   55  sudo apt-get install python3.13
   56  sudo apt-get install python3.12
   57  sudo apt-get install python3.11
   58  grep -rn 3.14 *|less
   59  git pull
   60  uv run -m poocam_core.random_sensor_process
   61  getconf PAGE_SIZE
   62  CFLAGS="-D_SC_PAGE_SIZE=4096 -D_SC_PAGESIZE=4096" uv pip install sysv-ipc
   63  sudo apt install python3-dev
   64  uv run -m poocam_core.random_sensor_process
   65  sudo apt update
   66  sudo apt install libjpeg-dev zlib1g-dev
   67  uv run -m poocam_core.random_sensor_process
   68  sudo apt install python3-numpy
   69  uv run -m poocam_core.random_sensor_process
   70  sudo apt install python3-pydantic
   71  uv run -m poocam_core.random_sensor_process
   72* sudo apt install python3-
   73  uv run -m poocam_core.random_sensor_process
   74  sudo apt install python3-pydantic-core
   75  uv run -v -m poocam_core.random_sensor_process
   76  more /etc/pip.conf 
   77  python3
   78  uv run -v -m poocam_core.random_sensor_process
   79  uv run -m poocam_core.random_sensor_process
   80  python3 poocam_core.random_sensor_process
   81  python3 poocam_core/random_sensor_process
   82  ls
   83  python3 packages/poocam_core/random_sensor_process
   84  python3 packages/poocam-core/src/poocam_core/random_sensor_process.py 
   85  export UV_INDEX_URL=https://piwheels.org/simple
   86  uv run -m poocam_core.random_sensor_process
   87  uv lock
   88  grep -rn ruff (
   89  grep -rn ruff *
   90  git pull
   91  uv run -m poocam_core.random_sensor_process
   92  vi pyproject.toml 
   93  uv run -m poocam_core.random_sensor_process
   94  find .|grep uv.lock
   95  mv uv.lock uv.lock.bak
   96  uv run -m poocam_core.random_sensor_process
   97  python3 -c "import numpy"
   98  python -version
   99  python --version
  100  which python
  101  uv cache clean
  102  uv run -m poocam_core.random_sensor_process
  103  sudo apt-get install libopenblas-dev
  104  uv run -m poocam_core.random_sensor_process
  105  history

```
