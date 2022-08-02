#        ~Data Structure at this point~
#        ID-First-Last
#        3- [Bodyweight, # of workout sessions this week, # of cardio ]
#        4- [Number of tracked days, Number of Low Calorie Days, Avg Cals, Avg Protein, Avg Fats, Avg Carbs] <- Data from the last 7 days
#        5- [Goal Calories, Goal Protein, Goal Fats, Goal Carbs ]
#        6- [All nutrition data by date, cals, protein, fats, carbs...]
from datetime import datetime

class reportClass:

    def __init__(self, clientData, today, lastMonday):      
 
        self.firstName = clientData[1]
        self.lastName = clientData[2] 
        self.weight = str(clientData[3][0])

        self.workoutCount = str(clientData[3][1]) 
        self.cardioCount = str(clientData[3][2]) 

        if len(clientData[4]) != 0:
            self.foodTrackCount = str(clientData[4][0]) 
            self.lowCaldayCount = str(clientData[4][1])
            self.avgCals = str(int(clientData[4][2])) 
            self.avgProtein = str(int(clientData[4][3]))
            self.avgFats = str(int(clientData[4][4])) 
            self.avgCarbs = str(int(clientData[4][5]))
        else:
            self.foodTrackCount = str(0)
            self.lowCaldayCount = str(0)
            self.avgCals = str(0)
            self.avgProtein = str(0)
            self.avgFats = str(0)
            self.avgCarbs = str(0)
        
        self.calTarget = str(int(clientData[5][0]))  
        self.proteinTarget = str(int(clientData[5][1])) 
        self.fatTarget = str(int(clientData[5][2]))  
        self.carbTarget = str(int(clientData[5][3])) 

        self.dateDif = today - lastMonday
        self.daysSinceLastMonday = str(self.dateDif.days)

    def getGeneralReport(self):
        print( "\n")
        print(" - " + self.firstName + " " + self.lastName + " -  Weight " + self.weight)
        print("Nutrition Tracked: " + self.foodTrackCount + "  Days / " + self.daysSinceLastMonday + " Day(s)")
        print("Average Calories:  " + self.avgCals +  "  Target: " + self.calTarget)
        print("Average Protein:   " + self.avgProtein  + "g" +  "  Target:   " + self.proteinTarget  + "g"  )
        print("Average Fats:      " + self.avgFats  + "g" +  "  Target:   " + self.fatTarget  + "g"  )
        print("Average Carbs:     " + self.avgCarbs  + "g" +  "  Target:   " + self.carbTarget  + "g"  )  
        print("Very Low Cal Days: " + self.lowCaldayCount + " Days")
        print("Workouts:          " + self.workoutCount + " Days")
        print("Cardio Sessions:   " + self.cardioCount + " Days")
        print("   - Recommendations - ")


        if self.weight == "0":
            print("   >Needs to get a weigh in.")

        if int(self.foodTrackCount) < int(self.daysSinceLastMonday):
            missingDays =  int(self.daysSinceLastMonday) -int(self.foodTrackCount) 
            print("   >Missing " + str(missingDays) +" day(s) of tracking food." )

        if self.workoutCount == str(0):
            print("   >No Workouts Completed")
        
        if self.cardioCount == str(0):
            print("   >No Cardio Completed") 

        if self.avgCals == str(0):
            print("   >No Calorie Information")
        else: 
            calorieHolder = (int(self.avgCals) - int(self.calTarget)) / int(self.calTarget)
            if abs(calorieHolder) > 0.1:
                print("   >Need to work on getting closer to calorie target")
 
            proteinHolder = (int(self.avgProtein) - int(self.proteinTarget)) / int(self.proteinTarget)
            if abs(proteinHolder) > 0.2:
                print("   >Need to work on getting closer to protein target")

 