def combine_anagrams(words)
    sorted = Array.new()
    
    if (words.length == 0)
        return sorted
    end
    
    sets = Hash.new
        
    words.each do |word|
        hash = word.downcase
        letters = Array.new()
        letters = hash.chars.to_a.sort
        if sets.has_key?(letters)
            sets[letters].push(word)
        else
            sets[letters] = Array.new()
            sets[letters].push(word)            
        end            
    end
    
    sets.each do |key, value|
        sorted.push(value)
    end
    return sorted
end