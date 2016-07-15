"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    counted = []
    scores = []
    for element in hand:
        if element not in counted:
            scores.append(hand.count(element)*element)
            counted.append(element)
    return max(scores)

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    result = 0
    outcomes = range(1, num_die_sides + 1)
    possible = sorted(gen_all_sequences(outcomes, num_free_dice))
    for hand in possible:
        result += score(held_dice + hand)
    return float(result)/len(possible)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds_set = [()]
    for entry in hand:
        for subset in all_holds_set:
            # create subsets of hand set
            all_holds_set = all_holds_set + [tuple(subset) + (entry,)]
    return set(sorted(all_holds_set))
    
def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    best_move = (0.0, ())
    all_holds = gen_all_holds(hand)
    for hold in all_holds:
        # hand can be less than 5
        num_free_dice = len(hand) - len(hold)
        expected = expected_value(hold, num_die_sides, num_free_dice)
        if expected > best_move[0]:
            best_move = (expected, hold)
    return best_move

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1,2,5,5,5)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

                                       
    
    
    



