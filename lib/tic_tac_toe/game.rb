# -*- encoding : utf-8 -*-

module TicTacToe
  class Game
    def initialize args
      @board    = args[:board]
      @player_1 = args[:player_1]
      @player_2 = args[:player_2]
    end

    def play
      loop do
        @player_1.make_move_on board: @board
        # @board.check_for_winner
        @player_2.make_move_on board: @board
        # @board.check_for_winner
        break
      end
    end
  end
end
