class Dessert
    
    attr_accessor :name
    attr_accessor :calories
    
    def initialize(name, calories)
        @name = name
        @calories = calories
    end
    
    def healthy?
        if calories < 200
            return true
        end
        
        return false
    end
    
    def delicious?
        return true
    end
end

class JellyBean < Dessert
    
    attr_accessor :flavor
    
    def initialize(name, calories, flavor)
        @name = name
        @calories = calories
        @flavor = flavor.downcase
    end
    
    def delicious?
        if flavor == "black licorice"
            return false
        end
        super
    end
end