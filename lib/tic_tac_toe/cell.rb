# -*- encoding : utf-8 -*-

module TicTacToe
  class Cell
    def initialize args
      @x      = args[:x]
      @y      = args[:y]
      @player = args[:player]
    end
  end
end
