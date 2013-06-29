require 'test/unit'

class Numeric
  @@currencies = {'dollar' => 1.0, 'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019}
  def method_missing(method_id, currency_target=0)
    singular_currency = method_id.to_s.gsub( /s$/, '')
    currency_target = currency_target.to_s.gsub( /s$/, '')

    if @@currencies.has_key?(singular_currency)
      self * @@currencies[singular_currency]
    elsif (singular_currency == "in")
      if @@currencies.has_key?(currency_target)
        self / @@currencies[currency_target]
      end
    else
      super
    end
  end
end

def palindrome?(string)
  string.downcase!
  string.gsub!(/[\s\W]/, '')

  if (string == string.reverse) then
    return true
  end
  return false
end

module Enumerable
  def method_missing(method_id)
    if (method_id =~ /palindrome\?/)
      return self.to_a == self.to_a.reverse
    end
  end
end

class String
  def method_missing(method_id)
    if (method_id =~ /palindrome\?/)
      return palindrome?(self)
    else
      super
    end
  end
end