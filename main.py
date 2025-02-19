import mujoco
from mujoco.viewer import launch

# Load the MuJoCo model

model = mujoco.MjModel.from_xml_path("model/myolegs.xml")

data = mujoco.MjData(model)



# Launch the viewer
with launch(model, data) as viewer:
    print("")
