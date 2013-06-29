class CartesianProduct
  include Enumerable
  attr_reader :elements
  def initialize(xs, ys)
    @elements = []
    xs.each do |x|
      ys.each do |y|
       @elements << [x,y]
      end
    end
  end

  def each
    @elements.each do |element|
      yield element
    end
  end
end