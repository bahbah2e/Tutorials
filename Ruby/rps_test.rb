require 'test/unit'

class WrongNumberOfPlayersError < StandardError ; end
class NoSuchStrategyError < StandardError ; end

def rps_game_winner(game)
    raise WrongNumberOfPlayersError unless game.length == 2
    
    game.each do |player|
        raise NoSuchStrategyError unless is_valid_strategy([player[1].upcase])
    end
    
    playerOne = game[0][1]
    playerTwo =  game[1][1]
    
    return game[rps_game_winner_plays(playerOne, playerTwo)]
end

def rps_game_winner_plays(playerOne, playerTwo)
    if (playerOne == playerTwo)||
        ((playerOne == "R") and (playerTwo == "S")) ||
        ((playerOne == "S") and (playerTwo == "P")) ||
        ((playerOne == "P") and (playerTwo == "R"))
        return 0
    end
    
    return 1
end

def rps_game_loser_index(game)
    raise WrongNumberOfPlayersError unless game.length == 2
    
    game.each do |player|
        raise NoSuchStrategyError unless is_valid_strategy([player[1].upcase])
    end
    
    playerOne = game[0][1]
    playerTwo =  game[1][1]

    if (playerOne == playerTwo)||
        ((playerOne == "R") and (playerTwo == "S")) ||
        ((playerOne == "S") and (playerTwo == "P")) ||
        ((playerOne == "P") and (playerTwo == "R"))
        return 1
    end
    
    return 0
end

def is_valid_strategy(strategy)
    strategies = ["P", "S", "R"]
    
    if (strategies & strategy).length > 0
        return true
    end
    return false
end

def is_match?(match)
    if match.length != 2 
        #print "Not a match #{match}\n"
        return false 
    end

    if (match[0][1].nil?) || (match[1][1].nil?)
        #print "Not a match #{match}\n"
        return false
    end
    
    if is_valid_strategy([match[0][1]]) && is_valid_strategy([match[1][1]])
        #print ( "Match: #{match[0][0]} vs #{match[1][0]}\n" )
        return true
    end
    
    return false
end

def rps_tournament_winner(bracket)    
    if (is_match?(bracket))                
        return rps_game_winner(bracket)        
    else
        winners = []
        bracket.each do |match|
            winners.push(rps_tournament_winner(match))
        end
        if winners.length == 2
            rps_tournament_winner(winners)
        end
    end
end
 
def depth(bracket, length=0)
    if bracket[0] =~ /\w+$/
        return length
    else
        return depth(bracket[0],length + 1)
    end    
end

class TestBracket < Test::Unit::TestCase
    
    ARMANDO = ["Armando", "P"]
    DAVE = ["Dave", "S"]
    DICK = ["Richard", "R"]
    MIKE = ["Michael", "S"]
    ALLEN = ["Allen", "S"]
    OMER = ["Omer", "P"]
    DAVEE = ["David E.", "R"]
    DICKX = ["Richard X.", "P"]
            
    def test_simple_s_beats_p
        bracket = [ARMANDO, DAVE]
        assert_equal(DAVE, rps_tournament_winner(bracket))
    end
    
    def test_simple_r_beats_s
        bracket = [DICK, DAVE]
        assert_equal(DICK, rps_tournament_winner(bracket))
    end
    
    def test_simple_p_beats_r
        bracket = [DAVEE, DICKX]
        assert_equal(DICKX, rps_tournament_winner(bracket))
    end
    
    def test_simple_tie
        bracket = [MIKE, DAVE]
        assert_equal(MIKE, rps_tournament_winner(bracket))
    end
    
    def test_tournament_depth_one_roundd
        bracket = [ARMANDO, DAVE]
        assert_equal(1, depth(bracket))
    end
    
    def test_tournament_depth_two_rounds
        bracket = [[ARMANDO, DAVE], [MIKE, DICK]]
        assert_equal(2, depth(bracket))
    end
    
    def test_tournament_depth_one_round
        bracket = [[ARMANDO, DAVE], [MIKE, DICK]]
        assert_equal(DICK, rps_tournament_winner(bracket))
    end
    
    def test_tournament_depth_two_round
        bracket = [[[ARMANDO, DAVE], [DICK, MIKE]],[[ALLEN, OMER],[DAVEE, DICKX]]]
        assert_equal(DICK, rps_tournament_winner(bracket))
    end    
end