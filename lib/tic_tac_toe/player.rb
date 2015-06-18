# -*- encoding : utf-8 -*-

module TicTacToe
  class Player
    def initialize args
      @name = args[:name]
      @side = args[:side]
    end

    def to_s
      @name
    end

    def x?
      @side == :x
    end
  end
end
