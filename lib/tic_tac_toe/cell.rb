# -*- encoding : utf-8 -*-

module TicTacToe
  class Cell
    def initialize args
      @player = args[:player]
    end

    CONVERT_XNESS_TO_X_OR_O = {
      true  => 'X',
      false => 'O'
    }

    def to_s
      CONVERT_XNESS_TO_X_OR_O[@player.x?]
    end
  end
end
