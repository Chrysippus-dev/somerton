from evennia.contrib import custom_gametime

from commands.command import Command

class CmdTime(Command):

    """
    Display the time.

    Syntax:
        time
        
    Time in Somerton runs differently to real life.
    
    1 day in Somerton lasts 12 real life hours.
    
    There are five days in a week: Solday, Washday, Luneday, Marketday and Restday.
    
    There are 12 months a year, each lasting 25 days: Fore, Getheren, Reyn, Gras, Blume, Jolity, Haye, Hervest, Barli, Wynne, Mist, and Yule.

    """

    key = "time"
    aliases = ["date"]
    locks = "cmd:all()"

    def func(self):
        """Execute the time command."""
        # Get the absolute game time
        year, month, week, day, hour, min, sec = custom_gametime.custom_gametime(absolute=True)
        # Work out what day of the week it is
        days = ("Solday", "Washday", "Luneday", "Marketday", "Restday")
        day_name = days[day]
        # Work out the date
        date = week * 5 + (day + 1)
        date_string = str(date)
        if date < 10 or date > 19:
            if date_string[len(date_string)-1] == "1": date_string += "st"
            elif date_string[len(date_string)-1] == "2": date_string += "nd"
            elif date_string[len(date_string)-1] == "3": date_string += "rd"
            else: date_string += "th"
        else: date_string += "th"
        # Work out the month
        months = ("Fore", "Getheren", "Reyn", "Gras", "Blume", "Jolity", "Haye", "Hervest", "Barli", "Wynne", "Mist", "Yule")
        month_name = months[month]
        #Bells
        if hour == 0: bell = "12"
        else: bell = str(hour)
        if bell == "1": bell += "st bell"
        else: bell += " bells"
        # Output the time
        string = "Today is {day_name} the {date} of {month_name}, {year}."
        string += "\nThe clock last chimed {bell}."
        self.msg(string.format(year=year, month_name=month_name, day_name=day_name,
                date=date_string, bell=bell, min=min, sec=sec))
				