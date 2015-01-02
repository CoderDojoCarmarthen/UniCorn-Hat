
import math, decimal, datetime
import moonphase as moonphase
dec = decimal.Decimal



def position(now=None): 
   if now is None: 
      now = datetime.datetime.now()

   diff = now - datetime.datetime(2001, 1, 1)
   days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
   lunations = dec("0.20439731") + (days * dec("0.03386319269"))

   return lunations % dec(1)

def phase(pos): 
   index = (pos * dec(8)) + dec("0.5")
   index = math.floor(index)
   return {
      0: "New Moon", 
      1: "Waxing Crescent", 
      2: "First Quarter", 
      3: "Waxing Gibbous", 
      4: "Full Moon", 
      5: "Waning Gibbous", 
      6: "Last Quarter", 
      7: "Waning Crescent"
   }[int(index) & 7]

def main(): 
   pos = position()
   phasename = phase(pos)

   roundedpos = round(float(pos), 3)
   print "%s (%s)" % (phasename, roundedpos)
   if phasename == "New Moon":
      moonphase.new_moon()
   elif phasename == "Waxing Creacent":
      moonphase.waxing_crescent()
   elif phasename == "First Quarter":
      moonphase.first_quarter()
   elif phasename == "Waxing Gibbous":
      moonphase.waxing_gibbous()
   elif phasename == "Full Moon":
      moonphase.full_moon()
   elif phasename == "Waning Bibbous":
      moonphase.waining_gibbous()
   elif phasename == "Last Quarter":
      moonphase.last_quarter()
   elif phasename == "Waning Crescent":
      moonphase.waning_crescent()
      



if __name__=="__main__": 
   main()
