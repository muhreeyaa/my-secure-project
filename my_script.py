# this is the "my-secure-project/my_script.py" file...

import os
from dotenv import load_dotenv

load_dotenv() #> invoking this function loads contents of the ".env" file into the script's environment...

# ... where they can be accessed / read via the os module as usual:
print(os.getenv("SECRET_MESSAGE"))