# -*- encoding : utf-8 -*-

require 'tic_tac_toe/cell'

require 'tic_tac_toe/strategists/random'

module TicTacToe
  class Player
    DEFAULTS = {
      cell:       Cell,
      strategist: Strategists::Random.new
    }

    def initialize args
      args = DEFAULTS.merge args

      @cell       = args[:cell]
      @name       = args[:name]
      @strategist = args[:strategist]
    end

    def to_s
      "name: #{@name}"
    end

    def make_move_on args
      board = args[:board]

      loop do
        move = { cell: @cell }

        move.merge! @strategist.choose_location board: board

        break if board.put_cell_at move.merge cell: @cell
      end

      @cell
    rescue ArgumentError
      retry
    end
  end
end
