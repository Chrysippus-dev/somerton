from evennia.contrib import custom_gametime 
from typeclasses.rooms import Room

#If we add places where the bells couldn't be heard, we'll need to change these messages.

def at_sunrise():
    """When the sun rises, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The bells of the tower chime thrice, heralding the rising of Sol.")

def start_sunrise_event():
    """Schedule a sunrise event to happen every day at 3 bells."""
    script = custom_gametime.schedule(at_sunrise, repeat=True, hour=3, min=0, sec=0)
    script.key = "at sunrise"
    
def at_4():
    """Make the clock ring 4 times."""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Sol continues its climb as four bells ring out into the morning.")
        
def start_4_event():
    """Schedule the bells to ring at 4 bells."""
    script = custom_gametime.schedule(at_4, repeat=True, hour=4, min=0, sec=0)
    script.key="at 4"

def at_5():
    """Make the clock ring 5 times."""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Five bells chime, marking the last hour of the morning.")
        
def start_5_event():
    """Schedule the bells to ring at 5 bells."""
    script = custom_gametime.schedule(at_5, repeat=True, hour=5, min=0, sec=0)
    script.key="at 5"
    
def at_midday():
    """At midday, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Six bells chime as Sol reaches its zenith, bathing the land in light.")

def start_midday_event():
    """Schedule a midday event to happen every day at 6 bells."""
    script = custom_gametime.schedule(at_midday, repeat=True, hour=6, min=0, sec=0)
    script.key = "at midday"
    
def at_7():
    """Make the clock ring 7 times."""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Seven sonorous bells ring out from the clock tower.")
        
def start_7_event():
    """Schedule the bells to ring at 7 bells."""
    script = custom_gametime.schedule(at_7, repeat=True, hour=7, min=0, sec=0)
    script.key="at 7"
    
def at_8():
    """Make the clock ring 8 times."""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Shadows begin to grow longer, with eight bells announcing the late afternoon hour.")
        
def start_8_event():
    """Schedule the bells to ring at 8 bells."""
    script = custom_gametime.schedule(at_8, repeat=True, hour=8, min=0, sec=0)
    script.key="at 8"
    
def at_sunset():
    """When the sun sets, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The dusky hues of crimson and ochre engulf the sky, as nine bells marks the setting of Sol.")

def start_sunset_event():
    """Schedule a sunset event to happen every day at 9 bells."""
    script = custom_gametime.schedule(at_sunset, repeat=True, hour=9, min=0, sec=0)
    script.key = "at sunset"
    
def at_10():
    """Make the clock ring 10 times."""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The stars wink into wakefulness, stirred by the singing of ten bells.")
        
def start_10_event():
    """Schedule the bells to ring at 10 bells."""
    script = custom_gametime.schedule(at_10, repeat=True, hour=10, min=0, sec=0)
    script.key="at 10"
    
def at_midnight():
    """At midnight, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Deepest darkness covers the land. It is midnight.")

def start_midnight_event():
    """Schedule a midnight event to happen every day at 12 bells."""
    script = custom_gametime.schedule(at_midnight, repeat=True, hour=12, min=0, sec=0)
    script.key = "at midnight"