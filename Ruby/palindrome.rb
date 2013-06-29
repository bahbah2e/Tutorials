def palindrome?(string)
    string.downcase!
    string.gsub!(/[\s\W]/, '')
    
    if (string == string.reverse) then
        return true
    end    
    return false
end
    
def count_words(string)
    string = string.downcase
    h1 = Hash.new
    string.scan(/[a-z]+/).each do |i|
        if h1.has_key?(i)
            h1[i] = h1[i] + 1
        else
            h1[i] = 1
        end            
    end
    return h1
end