import json
import os

mounts_file = os.path.expanduser("~/.tao_mounts.json")
tlt_configs = {
        "Mounts":[
            {
                "source": os.path.expanduser("~/cmu/tao/data"),
                "destination": "/data"
                },
            {
                "source": os.path.expanduser("~/cmu/tao/action_recognition_net/specs"),
                "destination": "/specs"
                },
            {
                "source": os.path.expanduser("~/cmu/tao/results"),
                "destination": "/results"
                },
            {
                "source": os.path.expanduser("~/.cache"),
                "destination": "/root/.cache"
                }
            ],
        "DockerOptions": {
            "shm_size": "16G",
            "ulimits": {
                "memlock": -1,
                "stack": 67108864
                }
            }
        }
# Writing the mounts file.
with open(mounts_file, "w") as mfile:
    json.dump(tlt_configs, mfile, indent=4)
