# -*- encoding : utf-8 -*-

module TicTacToe
  class Player
    def initialize name
      @name = name
    end

    def to_s
      @name
    end
  end
end
