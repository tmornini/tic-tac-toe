# -*- encoding : utf-8 -*-

module TicTacToe
  class Cell
    def self.to_s
      ' '
    end

    attr_reader :player

    def initialize args = { }
      @player = args[:player]
      @side   = args[:side]
    end

    CONVERT_SIDE_TO_X_OR_O = {
      x: 'X',
      o: 'O'
    }

    def to_s
      CONVERT_SIDE_TO_X_OR_O[@side]
    end
  end
end
