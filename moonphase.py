import unicornhat as UH
import time


view = 5 # time in sec to view the moon on the unicorn hat.

    
def full_moon():
    UH.brightness(0.4)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,255,255,255)
    UH.set_pixel(0,4,255,255,255)
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,255,255,255)
    UH.set_pixel(1,3,255,255,255)
    UH.set_pixel(1,4,255,255,255)
    UH.set_pixel(1,5,255,255,255)
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,255,255,255)
    UH.set_pixel(2,2,255,255,255)
    UH.set_pixel(2,3,255,255,255)
    UH.set_pixel(2,4,255,255,255)
    UH.set_pixel(2,5,255,255,255)
    UH.set_pixel(2,6,255,255,255)
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,255,255,255)
    UH.set_pixel(3,1,255,255,255)
    UH.set_pixel(3,2,255,255,255)
    UH.set_pixel(3,3,255,255,255)
    UH.set_pixel(3,4,255,255,255)
    UH.set_pixel(3,5,255,255,255)
    UH.set_pixel(3,6,255,255,255)
    UH.set_pixel(3,7,255,255,255)

    #4
    UH.set_pixel(4,0,255,255,255)
    UH.set_pixel(4,1,255,255,255)
    UH.set_pixel(4,2,255,255,255)
    UH.set_pixel(4,3,255,255,255)
    UH.set_pixel(4,4,255,255,255)
    UH.set_pixel(4,5,255,255,255)
    UH.set_pixel(4,6,255,255,255)
    UH.set_pixel(4,7,255,255,255)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,255,255,255)
    UH.set_pixel(5,2,255,255,255)
    UH.set_pixel(5,3,255,255,255)
    UH.set_pixel(5,4,255,255,255)
    UH.set_pixel(5,5,255,255,255)
    UH.set_pixel(5,6,255,255,255)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,255,255,255)
    UH.set_pixel(6,3,255,255,255)
    UH.set_pixel(6,4,255,255,255)
    UH.set_pixel(6,5,255,255,255)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,255,255,255)
    UH.set_pixel(7,4,255,255,255)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)


def last_quarter():
    UH.brightness(0.3)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,0,0,0)
    UH.set_pixel(0,4,0,0,0)
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,0,0,0)
    UH.set_pixel(1,3,0,0,0)
    UH.set_pixel(1,4,0,0,0)
    UH.set_pixel(1,5,0,0,0)
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,0,0,0)
    UH.set_pixel(2,2,0,0,0)
    UH.set_pixel(2,3,0,0,0)
    UH.set_pixel(2,4,0,0,0)
    UH.set_pixel(2,5,0,0,0)
    UH.set_pixel(2,6,0,0,0)
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,0,0,0)
    UH.set_pixel(3,1,0,0,0)
    UH.set_pixel(3,2,0,0,0)
    UH.set_pixel(3,3,0,0,0)
    UH.set_pixel(3,4,0,0,0)
    UH.set_pixel(3,5,0,0,0)
    UH.set_pixel(3,6,0,0,0)
    UH.set_pixel(3,7,0,0,0)

    #4
    UH.set_pixel(4,0,255,255,255)
    UH.set_pixel(4,1,255,255,255)
    UH.set_pixel(4,2,255,255,255)
    UH.set_pixel(4,3,255,255,255)
    UH.set_pixel(4,4,255,255,255)
    UH.set_pixel(4,5,255,255,255)
    UH.set_pixel(4,6,255,255,255)
    UH.set_pixel(4,7,255,255,255)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,255,255,255)
    UH.set_pixel(5,2,255,255,255)
    UH.set_pixel(5,3,255,255,255)
    UH.set_pixel(5,4,255,255,255)
    UH.set_pixel(5,5,255,255,255)
    UH.set_pixel(5,6,255,255,255)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,255,255,255)
    UH.set_pixel(6,3,255,255,255)
    UH.set_pixel(6,4,255,255,255)
    UH.set_pixel(6,5,255,255,255)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,255,255,255)
    UH.set_pixel(7,4,255,255,255)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)


def first_quarter():
    UH.brightness(0.3)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,255,255,255)
    UH.set_pixel(0,4,255,255,255)
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,255,255,255)
    UH.set_pixel(1,3,255,255,255)
    UH.set_pixel(1,4,255,255,255)
    UH.set_pixel(1,5,255,255,255)
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,255,255,255)
    UH.set_pixel(2,2,255,255,255)
    UH.set_pixel(2,3,255,255,255)
    UH.set_pixel(2,4,255,255,255)
    UH.set_pixel(2,5,255,255,255)
    UH.set_pixel(2,6,255,255,255)
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,255,255,255)
    UH.set_pixel(3,1,255,255,255)
    UH.set_pixel(3,2,255,255,255)
    UH.set_pixel(3,3,255,255,255)
    UH.set_pixel(3,4,255,255,255)
    UH.set_pixel(3,5,255,255,255)
    UH.set_pixel(3,6,255,255,255)
    UH.set_pixel(3,7,255,255,255)

    #4
    UH.set_pixel(4,0,0,0,0)
    UH.set_pixel(4,1,0,0,0)
    UH.set_pixel(4,2,0,0,0)
    UH.set_pixel(4,3,0,0,0)
    UH.set_pixel(4,4,0,0,0)
    UH.set_pixel(4,5,0,0,0)
    UH.set_pixel(4,6,0,0,0)
    UH.set_pixel(4,7,0,0,0)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,0,0,0)
    UH.set_pixel(5,2,0,0,0)
    UH.set_pixel(5,3,0,0,0)
    UH.set_pixel(5,4,0,0,0)
    UH.set_pixel(5,5,0,0,0)
    UH.set_pixel(5,6,0,0,0)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,0,0,0)
    UH.set_pixel(6,3,0,0,0)
    UH.set_pixel(6,4,0,0,0)
    UH.set_pixel(6,5,0,0,0)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,0,0,0)
    UH.set_pixel(7,4,0,0,0)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)


def new_moon():
    UH.brightness(0.1)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,255,255,255)
    UH.set_pixel(0,4,255,255,255)
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,255,255,255)
    UH.set_pixel(1,3,255,255,255)
    UH.set_pixel(1,4,255,255,255)
    UH.set_pixel(1,5,255,255,255)
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,255,255,255)
    UH.set_pixel(2,2,255,255,255)
    UH.set_pixel(2,3,255,255,255)
    UH.set_pixel(2,4,255,255,255)
    UH.set_pixel(2,5,255,255,255)
    UH.set_pixel(2,6,255,255,255)
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,255,255,255)
    UH.set_pixel(3,1,255,255,255)
    UH.set_pixel(3,2,255,255,255)
    UH.set_pixel(3,3,255,255,255)
    UH.set_pixel(3,4,255,255,255)
    UH.set_pixel(3,5,255,255,255)
    UH.set_pixel(3,6,255,255,255)
    UH.set_pixel(3,7,255,255,255)

    #4
    UH.set_pixel(4,0,255,255,255)
    UH.set_pixel(4,1,255,255,255)
    UH.set_pixel(4,2,255,255,255)
    UH.set_pixel(4,3,255,255,255)
    UH.set_pixel(4,4,255,255,255)
    UH.set_pixel(4,5,255,255,255)
    UH.set_pixel(4,6,255,255,255)
    UH.set_pixel(4,7,255,255,255)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,255,255,255)
    UH.set_pixel(5,2,255,255,255)
    UH.set_pixel(5,3,255,255,255)
    UH.set_pixel(5,4,255,255,255)
    UH.set_pixel(5,5,255,255,255)
    UH.set_pixel(5,6,255,255,255)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,255,255,255)
    UH.set_pixel(6,3,255,255,255)
    UH.set_pixel(6,4,255,255,255)
    UH.set_pixel(6,5,255,255,255)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,255,255,255)
    UH.set_pixel(7,4,255,255,255)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)


def waxing_crescent():
    UH.brightness(0.3)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,255,255,255)
    UH.set_pixel(0,4,255,255,255)
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,255,255,255)
    UH.set_pixel(1,3,255,255,255)
    UH.set_pixel(1,4,255,255,255)
    UH.set_pixel(1,5,255,255,255)
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,255,255,255)
    UH.set_pixel(2,2,255,255,255)
    UH.set_pixel(2,3,0,0,0)
    UH.set_pixel(2,4,0,0,0)
    UH.set_pixel(2,5,255,255,255)
    UH.set_pixel(2,6,255,255,255)
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,255,255,255)
    UH.set_pixel(3,1,0,0,0)
    UH.set_pixel(3,2,0,0,0)
    UH.set_pixel(3,3,0,0,0)
    UH.set_pixel(3,4,0,0,0)
    UH.set_pixel(3,5,0,0,0)
    UH.set_pixel(3,6,0,0,0)
    UH.set_pixel(3,7,255,255,255)

    #4
    UH.set_pixel(4,0,0,0,0)
    UH.set_pixel(4,1,0,0,0)
    UH.set_pixel(4,2,0,0,0)
    UH.set_pixel(4,3,0,0,0)
    UH.set_pixel(4,4,0,0,0)
    UH.set_pixel(4,5,0,0,0)
    UH.set_pixel(4,6,0,0,0)
    UH.set_pixel(4,7,0,0,0)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,0,0,0)
    UH.set_pixel(5,2,0,0,0)
    UH.set_pixel(5,3,0,0,0)
    UH.set_pixel(5,4,0,0,0)
    UH.set_pixel(5,5,0,0,0)
    UH.set_pixel(5,6,0,0,0)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,0,0,0)
    UH.set_pixel(6,3,0,0,0)
    UH.set_pixel(6,4,0,0,0)
    UH.set_pixel(6,5,0,0,0)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,0,0,0)
    UH.set_pixel(7,4,0,0,0)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)

def waxing_gibbous():
    UH.brightness(0.3)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,255,255,255)#
    UH.set_pixel(0,4,255,255,255)#
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,255,255,255)#
    UH.set_pixel(1,3,255,255,255)#
    UH.set_pixel(1,4,255,255,255)#
    UH.set_pixel(1,5,255,255,255)#
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,255,255,255)#
    UH.set_pixel(2,2,255,255,255)#
    UH.set_pixel(2,3,255,255,255)
    UH.set_pixel(2,4,255,255,255)
    UH.set_pixel(2,5,255,255,255)#
    UH.set_pixel(2,6,255,255,255)#
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,255,255,255)#
    UH.set_pixel(3,1,255,255,255)
    UH.set_pixel(3,2,255,255,255)
    UH.set_pixel(3,3,255,255,255)
    UH.set_pixel(3,4,255,255,255)
    UH.set_pixel(3,5,255,255,255)
    UH.set_pixel(3,6,255,255,255)
    UH.set_pixel(3,7,255,255,255)#

    #4
    UH.set_pixel(4,0,0,0,0)
    UH.set_pixel(4,1,255,255,255)
    UH.set_pixel(4,2,255,255,255)
    UH.set_pixel(4,3,255,255,255)
    UH.set_pixel(4,4,255,255,255)
    UH.set_pixel(4,5,255,255,255)
    UH.set_pixel(4,6,255,255,255)
    UH.set_pixel(4,7,0,0,0)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,0,0,0)
    UH.set_pixel(5,2,255,255,255)
    UH.set_pixel(5,3,255,255,255)
    UH.set_pixel(5,4,255,255,255)
    UH.set_pixel(5,5,255,255,255)
    UH.set_pixel(5,6,0,0,0)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,0,0,0)
    UH.set_pixel(6,3,0,0,0)
    UH.set_pixel(6,4,0,0,0)
    UH.set_pixel(6,5,0,0,0)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,0,0,0)
    UH.set_pixel(7,4,0,0,0)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)


def waining_gibbous():
    UH.brightness(0.3)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,0,0,0)
    UH.set_pixel(0,4,0,0,0)
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,0,0,0)
    UH.set_pixel(1,3,0,0,0)
    UH.set_pixel(1,4,0,0,0)
    UH.set_pixel(1,5,0,0,0)
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,0,0,0)
    UH.set_pixel(2,2,255,255,255)
    UH.set_pixel(2,3,255,255,255)
    UH.set_pixel(2,4,255,255,255)
    UH.set_pixel(2,5,255,255,255)
    UH.set_pixel(2,6,0,0,0)
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,0,0,0)#
    UH.set_pixel(3,1,255,255,255)
    UH.set_pixel(3,2,255,255,255)
    UH.set_pixel(3,3,255,255,255)
    UH.set_pixel(3,4,255,255,255)
    UH.set_pixel(3,5,255,255,255)
    UH.set_pixel(3,6,255,255,255)
    UH.set_pixel(3,7,0,0,0)#

    #4
    UH.set_pixel(4,0,255,255,255)
    UH.set_pixel(4,1,255,255,255)#
    UH.set_pixel(4,2,255,255,255)#
    UH.set_pixel(4,3,255,255,255)#
    UH.set_pixel(4,4,255,255,255)#
    UH.set_pixel(4,5,255,255,255)#
    UH.set_pixel(4,6,255,255,255)#
    UH.set_pixel(4,7,255,255,255)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,255,255,255)
    UH.set_pixel(5,2,255,255,255)
    UH.set_pixel(5,3,255,255,255)
    UH.set_pixel(5,4,255,255,255)
    UH.set_pixel(5,5,255,255,255)
    UH.set_pixel(5,6,255,255,255)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,255,255,255)
    UH.set_pixel(6,3,255,255,255)
    UH.set_pixel(6,4,255,255,255)
    UH.set_pixel(6,5,255,255,255)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,255,255,255)
    UH.set_pixel(7,4,255,255,255)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)


def waning_crescent():
    UH.brightness(0.3)
    #row 0
    UH.set_pixel(0,0,0,0,0)
    UH.set_pixel(0,1,0,0,0)
    UH.set_pixel(0,2,0,0,0)
    UH.set_pixel(0,3,0,0,0)
    UH.set_pixel(0,4,0,0,0)
    UH.set_pixel(0,5,0,0,0)
    UH.set_pixel(0,6,0,0,0)
    UH.set_pixel(0,7,0,0,0)

    #1
    UH.set_pixel(1,0,0,0,0)
    UH.set_pixel(1,1,0,0,0)
    UH.set_pixel(1,2,0,0,0)
    UH.set_pixel(1,3,0,0,0)
    UH.set_pixel(1,4,0,0,0)
    UH.set_pixel(1,5,0,0,0)
    UH.set_pixel(1,6,0,0,0)
    UH.set_pixel(1,7,0,0,0)

    #2
    UH.set_pixel(2,0,0,0,0)
    UH.set_pixel(2,1,0,0,0)
    UH.set_pixel(2,2,0,0,0)
    UH.set_pixel(2,3,0,0,0)
    UH.set_pixel(2,4,0,0,0)
    UH.set_pixel(2,5,0,0,0)
    UH.set_pixel(2,6,0,0,0)
    UH.set_pixel(2,7,0,0,0)

    #3
    UH.set_pixel(3,0,0,0,0)
    UH.set_pixel(3,1,0,0,0)
    UH.set_pixel(3,2,0,0,0)
    UH.set_pixel(3,3,0,0,0)
    UH.set_pixel(3,4,0,0,0)
    UH.set_pixel(3,5,0,0,0)
    UH.set_pixel(3,6,0,0,0)
    UH.set_pixel(3,7,0,0,0)

    #4
    UH.set_pixel(4,0,255,255,255)
    UH.set_pixel(4,1,0,0,0)
    UH.set_pixel(4,2,0,0,0)
    UH.set_pixel(4,3,0,0,0)
    UH.set_pixel(4,4,0,0,0)
    UH.set_pixel(4,5,0,0,0)
    UH.set_pixel(4,6,0,0,0)
    UH.set_pixel(4,7,255,255,255)

    #5
    UH.set_pixel(5,0,0,0,0)
    UH.set_pixel(5,1,255,255,255)
    UH.set_pixel(5,2,255,255,255)
    UH.set_pixel(5,3,0,0,0)
    UH.set_pixel(5,4,0,0,0)
    UH.set_pixel(5,5,255,255,255)
    UH.set_pixel(5,6,255,255,255)
    UH.set_pixel(5,7,0,0,0)

    #6
    UH.set_pixel(6,0,0,0,0)
    UH.set_pixel(6,1,0,0,0)
    UH.set_pixel(6,2,255,255,255)
    UH.set_pixel(6,3,255,255,255)
    UH.set_pixel(6,4,255,255,255)
    UH.set_pixel(6,5,255,255,255)
    UH.set_pixel(6,6,0,0,0)
    UH.set_pixel(6,7,0,0,0)

    #7
    UH.set_pixel(7,0,0,0,0)
    UH.set_pixel(7,1,0,0,0)
    UH.set_pixel(7,2,0,0,0)
    UH.set_pixel(7,3,255,255,255)
    UH.set_pixel(7,4,255,255,255)
    UH.set_pixel(7,5,0,0,0)
    UH.set_pixel(7,6,0,0,0)
    UH.set_pixel(7,7,0,0,0)
    UH.show()

    time.sleep(view)

#used to test the phases of the moon un comment to run
#new_moon()
#waxing_crescent()
#first_quarter()
#waxing_gibbous()
#full_moon()
#waining_gibbous()
#last_quarter()
#waning_crescent()



