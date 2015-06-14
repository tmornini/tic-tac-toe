# -*- encoding : utf-8 -*-

module TicTacToe
  class Player
    def initialize args
      @name = args[:name]
    end

    def to_s
      @name
    end
  end
end
