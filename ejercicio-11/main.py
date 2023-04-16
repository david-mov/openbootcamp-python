import time

class GoHomeTimer:
    def __init__(self, hour, min=0):
        self.hour = hour
        self.min = min

    def check(self):
        tm = time.localtime()
        current_hour = tm.tm_hour
        current_min = tm.tm_min

        if current_hour > self.hour or (current_hour == self.hour and current_min >= self.min) :
            return "It is time to go home"
        else:
            total_tm_left = self.hour * 60 + self.min - (current_hour * 60 + current_min)
            hours_left = int(total_tm_left / 60)
            min_left = total_tm_left % 60
            return f"{hours_left} hours and {min_left} minutes left to go home"

go_home_timer = GoHomeTimer(7)

print(go_home_timer.check())