from godity.core.Component import Component
from godity.core.Timer import Timer

class Animation(Component):
    def __init__(self, name, image_name, area_list, frame_delay=0, delay_list=None, auto_play=False):
        args = {
            "image name"  : image_name,
            "area list"   : area_list,
            "frame delay" : frame_delay,
            "delay list"  : delay_list,
            "auto play"   : auto_play
        }
        super().__init__("Animation "+name, args)

    def start(self):
        self.image_name = self.args["image name"]
        self.area_list = self.args["area list"]
        self.frame_delay = self.args["frame delay"]
        self.delay_list = self.args["delay list"]

        if self.args["auto play"]:
            self.__state = "run"
        else:
            self.__state = "paused"
        self.__area = self.area_list[0]
        self.__frame = 0
        self.__timer = Timer()

    def pause(self):
        self.__state = "paused"

    def run(self):
        self.__state = "run"
        self.entity.get("Sprite Renderer").image_name = self.image_name

    def restart(self):
        self.__frame = 0
    
    def getState(self):
        return self.__state

    def getArea(self):
        return self.__area

    def getFrame(self):
        return self.__frame

    def update(self):
        if self.getState() == "run":
            self.__area = self.area_list[self.__frame]
            self.entity.get("Sprite Renderer").setArea(self.__area)

            if self.delay_list == None:
                if self.__timer.getTime() >= self.frame_delay:
                    if self.__frame < len(self.area_list)-1:
                        self.__frame += 1
                    else:   self.__frame = 0
                    self.__timer.resetTime()
            else:
                if self.__timer.getTime() >= self.delay_list[self.__frame]:
                    if self.__frame < len(self.area_list)-1:
                        self.__frame += 1
                    else:   self.__frame = 0
                    self.__timer.resetTime()