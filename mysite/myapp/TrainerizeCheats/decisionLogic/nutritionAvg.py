#Return a list of valuable data
#      -Number of days tracked
#      -Number of days where calories are low
#      -Average Calories
#      -Average Protein
#      -Average Fats
#      -Average Carbs
#      *FOR ALL AVG INFO, OMITT TODAY'S DATA
import datetime

class foodAvg:
    def foodCalc(self, nutritionList):
       
        today = datetime.date.today().strftime("%Y-%m-%d") 

        #Go through 
        if len(nutritionList) != 0:
            a = 0
            trackedDays = 0
            lowCalDays = 0
            avgCals = 0
            avgPro = 0
            avgFats = 0
            avgCarbs = 0
            while a < len(nutritionList):
                if nutritionList[a] != today:
                    avgCals += nutritionList[a+1]
                    avgPro += nutritionList[a+2]
                    avgFats += nutritionList[a+3]
                    avgCarbs += nutritionList[a+4]
                    trackedDays += 1
                    if nutritionList[a+1] <= 700:
                        lowCalDays += 1
                    a +=5                 
                else:
                    a += 5

            #Get Averages
            if trackedDays > 0:
                avgCals = round(avgCals/trackedDays)
                avgPro = round(avgPro/trackedDays)
                avgFats = round(avgFats/trackedDays)
                avgCarbs = round(avgCarbs/trackedDays)

            nutritionAverage = []

            nutritionAverage.extend([trackedDays, lowCalDays, avgCals, avgPro, avgFats, avgCarbs])
            return(nutritionAverage)
        else:
            return(nutritionList)
