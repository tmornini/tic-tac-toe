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
        players.each do |player|
          player.make_move_on board: @board

          # TODO: Determine order of next two lines statistically
          return player if @board.has_winner?
          return nil    if @board.is_tied?
        end
      end
    end

    private

    def players
      [@player_1, @player_2]
    end
  end
end
