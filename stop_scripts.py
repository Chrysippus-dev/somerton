import evennia

"""
Stops all global scripts
"""

print('Stopping all global scripts')

for script in evennia.ScriptDB.objects.get_all_scripts():
    if not script.obj:  # Global scripts have no object attached to them
        script.stop()
