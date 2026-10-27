import random 
class State:
    def __init__(self, state_name: int):
        self.state_name = state_name
        
    def get_next_state(self):
        roll = random.randint(1, 6) + random.randint(1, 6)
        return State(self.state_name + roll)

class Snake(State):
    def __init__(self, state_name, next_state: State):
        super().__init__(state_name)
        self.next_state = next_state
        
        self.next_state = (
            next_state if isinstance(next_state, State) else State(next_state)
        )

    
    def get_next_state(self) -> State:
        return self.next_state
    

class Ladder(State):
    def __init__(self, state_name, next_state: State):
        super().__init__(state_name)
        self.next_state = next_state
        
        self.next_state = (
            next_state if isinstance(next_state, State) else State(next_state)
        )

    
    def get_next_state(self) -> State:
        return self.next_state
    
class Game:
    def __init__(self):
        snakes = [Snake(22, 10), Snake(30, 25), Snake(56, 21), Snake(67, 42), Snake(88, 70), Snake(99, 1)]
        ladders = [Ladder(10, 20), Ladder(33, 48), Ladder(52, 60), Ladder(75, 83), Ladder(80, 92)]
        self.transitions = {
            special.state_name: special
            for special in snakes + ladders
        }

    def resolve_special_squares(self, state: State) -> State:
        while state.state_name in self.transitions:
            state = self.transitions[state.state_name].get_next_state()

        return state

    
    def play(self) -> int:
        moves = 0
        current_state = State(1)

        while True:
            # Dice move
            current_state = current_state.get_next_state()
            moves += 1
            
            # Snake or ladder
            current_state = self.resolve_special_squares(current_state)

            # Winning / absorbing state
            if current_state.state_name >= 100:
                return moves
    
        
def monte_carlo(num_simulations: int = 100_000) -> float:
    game = Game()
    total_moves = 0

    for _ in range(num_simulations):
        total_moves += game.play()

    return total_moves / num_simulations


print(monte_carlo())