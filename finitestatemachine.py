#Brian Chung
#Lexur w/ Finite State Machine Working Iteration 1
#9/21/2019

class FiniteStateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            print("Must call .set_start() before .run()")
        if not self.endStates:
            print("At least one state must be an end_state")
    
        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                return(newState) 
            else:
                handler = self.handlers[newState.upper()] 
