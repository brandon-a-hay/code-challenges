class Dog
  def initialize(breed, name)
    @breed = breed
    @name = name
  end

  def bark
    puts "woof woof!"
  end
end

d = Dog.new('mini-pinscher', 'Penny')
d.bark