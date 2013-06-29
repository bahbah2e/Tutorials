def send_quiz()
    x = [1,2,3]
    print x
    x.send :[]=,0,2
    print x
    print x.send(:[],2)
    print x.[](1) 
    x[0] + x.[](1) + x.send(:[],2)
end

def movie_parse()
    movies = [%q{"Aladdin",   "G"},
              %q{"I, Robot", "PG-13"},
              %q{"Star Wars","PG"}]
    regexp = /"(.*)","(.*)"/
    movies.each do |movie|
      movie.match(regexp)
      title,rating = $1,$2
      print "#{title}, #{rating}\n"
    end
end

class something_else
    attr_accessor :something
end


class Book < something_else
    attr_accessor :author
    attr_reader :title
    attr_writer :comments
    def initialize(author, title)
        @author = author
        @title = title
        @comments = []
    end
end


book = Book.new("Chuck Palahniuk", "Fight Club")
book.comments.each { |comment| puts comment }

print book.class.ancestors.include?(something_else)