from evennia.contrib import custom_gametime 
from typeclasses.rooms import Room

#If we add places where the bells couldn't be heard, we'll need to change these messages.

def at_1():
    """Set the message for 1st bell"""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("A single low 'bong' echoes through the night.")
        
def start_1_event():
    """Schedule the message for 1st bell."""
    script = custom_gametime.schedule(at_1, repeat=True, hour=1, min=0, sec=0)
    script.key="at 1"
    
def at_2():
    """Set the message for 2 bells"""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Lune sinks towards the horizon as the stars begin to fade, and the tower bells ring twice.")
        
def start_2_event():
    """Schedule the message for 2 bells."""
    script = custom_gametime.schedule(at_2, repeat=True, hour=2, min=0, sec=0)
    script.key="at 2"

def at_3():
    """Set the sunrise message."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The bells of the tower chime thrice, heralding the rising of Sol.")

def start_3_event():
    """Schedule a sunrise event to happen every day at 3 bells."""
    script = custom_gametime.schedule(at_sunrise, repeat=True, hour=3, min=0, sec=0)
    script.key = "at 3"
    
def at_4():
    """Set the message for 4 bells."""
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
    
def at_6():
    """At midday, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Six bells chime as Sol reaches its zenith, bathing the land in light.")

def start_6_event():
    """Schedule a midday event to happen every day at 6 bells."""
    script = custom_gametime.schedule(at_midday, repeat=True, hour=6, min=0, sec=0)
    script.key = "at 6"
    
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
        room.msg_contents("Shadows begin to grow longer, with eight bells announcing the late afternoon.")
        
def start_8_event():
    """Schedule the bells to ring at 8 bells."""
    script = custom_gametime.schedule(at_8, repeat=True, hour=8, min=0, sec=0)
    script.key="at 8"
    
def at_9():
    """When the sun sets, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The dusky hues of crimson and ochre engulf the sky, as nine bells mark the setting of Sol.")

def start_9_event():
    """Schedule a sunset event to happen every day at 9 bells."""
    script = custom_gametime.schedule(at_sunset, repeat=True, hour=9, min=0, sec=0)
    script.key = "at 9"
    
def at_10():
    """Make the clock ring 10 times."""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The stars wink into wakefulness, stirred by the singing of ten bells.")
        
def start_10_event():
    """Schedule the bells to ring at 10 bells."""
    script = custom_gametime.schedule(at_10, repeat=True, hour=10, min=0, sec=0)
    script.key="at 10"

def at_11():
    """Set the message for 11 bells."""
    #Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("As eleven bells ring, Lune gazes down upon the land from its position high in the sky.")
        
def start_4_event():
    """Schedule the 11 bells message."""
    script = custom_gametime.schedule(at_11, repeat=True, hour=11, min=0, sec=0)
    script.key="at 11"
    
def at_12():
    """At midnight, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("Deepest darkness covers the land. A peal of twelve bells marks midnight.")

def start_midnight_event():
    """Schedule a midnight event to happen every day at 12 bells."""
    script = custom_gametime.schedule(at_midnight, repeat=True, hour=12, min=0, sec=0)
    script.key = "at 12"