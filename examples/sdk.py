# Install the Lightning SDK
# pip install lightning-sdk

# login to the platform
# export LIGHTNING_USER_ID=9589da6c-a5c8-4372-a882-49a0efd34a96
# export LIGHTNING_API_KEY=72362c58-bd08-413b-8aba-b1c3e0501361

from lightning_sdk import Machine, Studio, JobsPlugin, MultiMachineTrainingPlugin

# Start the studio
s = Studio(name="my-sdk-studio", teamspace="language-model", org="asanthularithesh", create_ok=True)
print("starting Studio...")
s.start()

# prints Machine.CPU-4
print(s.machine)

print("switching Studio machine...")
s.switch_machine(Machine.A10G)

# prints Machine.A10G
print(s.machine)

# prints Status.Running
print(s.status)

print(s.run("nvidia-smi"))

print("Stopping Studio")
s.stop()

# duplicates Studio, this will also duplicate the environment and all files in the Studio
duplicate = s.duplicate()

# delete original Studio, duplicated Studio is it's own entity and not related to original anymore
s.delete()

# stop and delete duplicated Studio
duplicate.stop()
duplicate.delete()
    