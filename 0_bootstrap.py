## Part 0: Bootstrap File
# Install the requirements
import os

if int(os.environ["CDSW_MEMORY_MB"]) >= 2933:
  !pip3 install -r requirements.txt
else:
  print ("please increase session memory to at least 3GB for installing libraries")
