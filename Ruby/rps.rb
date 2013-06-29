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