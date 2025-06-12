class BGL_Analyzer:

    #Initiate an Analyzer object with a dedicated user and uses the database associated with the user    
    def __init__(self, user, db):
        pass
    
    #add a food to the database if it is not found
    def _db_add_food(self, food):
        pass
    
    #use python pyplot (matplotlib)
    def display_graph(self):
        pass
    
    #either use a library for this to do it automatically
    #or calculate manually?
    def calculate_correlation(self, food):
        pass
    
    #use lambda to make it easier to read and complete
    #bgl_spike is the differnece in baseline and max
    #foods is a SET. Can't have an empty set
    #set={}
    def add_foods(self, foods, bgl_spike):
        if len(foods) <= 0:
            raise Exception("Set of foods can't be empty")
        pass
    
    #logmeal api?
    #openai api?
    def _identify_food(picture):
        pass
    
    #Blood glucose level for the day
    def get_avg_BGL(self):
        pass
    
    #blood glucose for all time. For use if you can connect to
    #a glucose monitoring app or device
    def get_avg_alltime_BGL(self):
        pass
    
    #update the all time average. Maybe include the date in the database avgerage. Could possibly display trend of BGL over time
    def _update_avg_BGL(self):
        pass
    
    
    #display the blood glucose as y axis with the time as the x axis.
    #shows whether your BGL is changing over a year, month, day, etc
    def display_avg_BGL(self):
        pass
    
    #return the BGl for a food (only values, no dates) 
    def _get_food_BGL_data(self, food):
        pass
    
    