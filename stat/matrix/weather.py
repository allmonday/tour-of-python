import numpy as np

#firstDay = np.array([1,0,0])
#trans = np.matrix([[.5,.375,.125],[.25,.125,.625],[.25,.375,.375]])
#secondDay = np.dot(firstDay, trans)
#print(secondDay)
#thirdDay = np.dot(secondDay, trans)
#print(thirdDay)
#fourthDay = np.dot(thirdDay, trans)
#print(fourthDay)
#fivethDay = np.dot(fourthDay, trans)
#print(fivethDay)

firstDay = np.array([1,0,0])
                        #sun, cloud, rain
HidTrans = np.matrix([[.5,.375,.125],       #sun
                      [.25,.125,.625],      #cloud
                      [.25,.375,.375]])     #rain

                       #soggy, damp, dryish, dry
ObsTrans = np.matrix([[.05,.15,.2,.6],  #sun
                      [.25,.25,.25,.25],   #cloud
                      [.5,.35,.1,.05]])  #rain
Weather = np.dot(firstDay, HidTrans)
Obs = np.dot(Weather, ObsTrans)
print(Weather)
print(Obs)
