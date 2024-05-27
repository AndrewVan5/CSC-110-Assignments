import doctest
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


def digit_sum(next_val: int) -> int:
    
    '''
    Calculates the sum of each digit of the number, ignores negative numbers.
    
    >>> digit_sum(2)
    2
    >>> digit_sum(23)
    5
    >>> digit_sum(634)
    13
    >>> digit_sum(-927482)
    32
    '''
    
    sum = 0
    
    while next_val != 0:
           
        last_digit = abs(next_val) % 10 #last digit
        next_val = abs(next_val) // 10 #changes number
        
        sum += last_digit
        
    return sum
        
        
def gcd(num1: int, num2: int) -> int:
    
    '''
    Returns the greatest common divisor between the two integers entered.
    Assumes integers entered are positive.
    
    >>> gcd(1,1)
    1
    >>> gcd(3,12)
    3
    >>> gcd(12,3)
    3
    >>> gcd(132, 444)
    12
    '''
    
    if num1 > num2 or num1 == num2:
        gcd = num1
    else:
        gcd = num2
    
    while num1 % gcd != 0 or num2 % gcd != 0:
        
        gcd -= 1
        
    return gcd




def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # die = int(input('enter a simulated dice roll\n'))

    return die


def play_again() -> bool:
    
    '''
    Asks if the user wants to make a bet or if they want to walk away.
    '''
    prompt = 'Do you want to make a bet?  Enter yes if you do: '
    
    return input(prompt) == 'yes'


    
    
def get_guess() -> int:
    
    '''
    Asks for guess of what dice will land on, keeps asking until valid integer
    is provided.
    '''
    
    prompt = 'Enter an integer between 1 and 6 inclusive: '
    guess = input(prompt)

    while guess.isdigit() == False or int(guess) < 1 or int(guess) > 6:
            guess = input(prompt)
            
    return int(guess)


def get_bet(max_bet: int) -> int:
    
    '''
    Asks how much user wants to bet, keeps asking until valid bet amount is
    provided.
    '''
    
    prompt = (f'Enter an integer between {MIN_BET} and {max_bet} inclusive: ')
    
    bet = input(prompt)
    
    while bet.isdigit() == False or int(bet) < MIN_BET or int(bet) > max_bet:
        bet = input(prompt)
        
    return int(bet)


def roll_dice(guess: int) -> int:
    
    '''
    Rolls dice and calculates how many matches to user's prediction there are.
    '''
    
    matches = 0
    print('')
    
    for roll in range(3):
        num = roll_one_die()
        print(f'Dice roll {roll}: {num}')
        
        if num == guess:
            matches += 1
    
    return matches


def compute_winnings(matches: int, bet: int):
    
    '''
    Computes profit/loss of bet.
    '''
    
    if matches == 1:
        bet = bet
   
    elif matches == 2:
        bet += bet
        
    elif matches == 3:
        bet += bet * 9
        
    else:
        bet *= -1
        
    return bet


def play_one_round(bet: int):
    
    '''
    Puts functions together in order to play a round.
    '''
    
    guess = get_guess()
    
    matches = roll_dice(guess)
    
    winnings = compute_winnings(matches, bet)
    
    profit_loss = winnings  
    
    return profit_loss


def play_game(bet_balance: int):
    
    '''
    Full gambling game organized in one function. Calculates and returns the
    user's balance.
    '''
    
    print(f'You have ${bet_balance} to play with\n')
    
    again = play_again()
    
    while bet_balance >= MIN_BET and again == True:
        
        print('')
        bet = get_bet(bet_balance)
        print(f'You bet ${bet}\n')
        
        profit_loss = play_one_round(bet)
        print('')
        
        if profit_loss > 0:
            print(f'Congrats! You won ${profit_loss}')
        
        else:
            print(f'Sorry you lost ${profit_loss * -1}')
            
        bet_balance += profit_loss
            
        print(f'You have ${bet_balance} in your bankroll\n')
        
        again = play_again()
        
    print(f'\nYou have ${bet_balance} left in your bankroll')
    
    return bet_balance
        
        
        
    