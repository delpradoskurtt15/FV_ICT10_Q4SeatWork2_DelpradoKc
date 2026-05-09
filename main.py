class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
#Method, use inputs to create an introduction message
    def introduce(self):
        return f"Hi, I'm {self.name} from {self.section} and my favorite subject is {self.favorite_subject}."

#List to store classmates
classmates = [
    Classmate("Kc", "Emerald", "Social Studies"),
    Classmate("Alexandra", "Emerald", "Science"),
    Classmate("Janine", "Emerald", "English"),
    Classmate("Cyrene", "Emerald", "PE"),
    Classmate("Xylee", "Emerald", "Math"),
     
]

#Method to add classmates to a list
def add_classmate(event=None):
    from js import document

    
    name = document.getElementById("fname").value
    section = document.getElementById("section").value
    favsub = document.getElementById("favsub").value
    
    #Create a new classmate object and add it to the list of classmates
    new_classmate = Classmate(name, section, favsub)
    classmates.append(new_classmate)

    #Clear input fields after adding a classmate 
    document.getElementById("fname").value = ""
    document.getElementById("section").value = ""
    document.getElementById("favsub").value = ""
    

#Use loop to display all introductions
def show_classmates(event=None):
    from js import document

    output = ""
    for mate in classmates:   # LOOP here
        output += mate.introduce() + "<br>"
    document.getElementById("result").innerHTML = output
