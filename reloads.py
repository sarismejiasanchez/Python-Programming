# RELOAD FUNCTION
# This function reloads the module specified by the user.

import importlib
import sample

importlib.reload(sample)

print(f"Reloaded {sample.__name__} module.")
importlib.reload(sample)
importlib.reload(sample)

def changes():
    try:
        import filechanges
        print(f"Reloaded {filechanges.__name__} module.")
        importlib.reload(filechanges)
    except ImportError:
        print("Module not found. Please check the module name and try again.")
        return

changes()