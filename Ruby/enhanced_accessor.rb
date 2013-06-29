class Class
    
    def attr_accessor_with_history(attr_name)
        attr_name = attr_name.to_s # make sure it's a string
        attr_reader attr_name # create the attribute's
        attr_reader attr_name+"_history" # create bar_history
        
        code = %Q{
            attr_accessor :values

            def #{attr_name}=(value)
                if (@values.nil?)
                    @values = Hash.new()
                end
                if (@values[:#{attr_name}].nil?)
                    @values[:#{attr_name}] = [nil]
                end
                @values[:#{attr_name}].push(value)
                print "\#{values} \n"
                @#{attr_name} = value                
            end
            
            def #{attr_name}_history
                return @values[:#{attr_name}]
            end   
        }
        class_eval(code)
    end
end

class Foo
    attr_accessor_with_history :bar
end