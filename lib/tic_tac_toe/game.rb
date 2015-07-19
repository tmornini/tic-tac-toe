# -*- encoding : utf-8 -*-

module TicTacToe
  class Game
    def initialize args
      @board    = args[:board]
      @x_player = args[:x_player]
      @o_player = args[:o_player]
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
      [@x_player, @o_player]
    end
  end
end
