require 'test/unit'

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

class TestBracket < Test::Unit::TestCase
    
    def test_accessor_basic
        f = Foo.new # => #<Foo:0x127e678>
        f.bar = 3 
        assert_equal(f.bar, 3)
        assert_equal([3],f.bar_history)
    end
    
    def test_accessor_basic_reset
        f = Foo.new # => #<Foo:0x127e678>
        f.bar = 3 
        f.bar = "HELLO"
        assert_equal(f.bar, "HELLO")
    end
    
    def test_accessor_history
        f = Foo.new # => #<Foo:0x127e678>
        f.bar = 3 
        f.bar = "HELLO"
        assert_equal([3, "HELLO"],f.bar_history)
    end
end