# -*- encoding : utf-8 -*-

require 'tic_tac_toe/board'
require 'tic_tac_toe/game'
require 'tic_tac_toe/side_selector'

module TicTacToe
  module GameStarter
    DEFAULTS = {
      board_klass:          Board,
      game_klass:           Game,
      side_selector_module: SideSelector
    }

    def self.start args
      args = DEFAULTS.merge args

      winner, board = run_game args

      {
        state:  state(winner),
        winner: winner,
        board:  board
      }
    end

    private

    def self.run_game args
      board = args[:board_klass].new

      winner =
        args[:game_klass].new(
          args[:side_selector_module]
            .select(args)
            .merge board: board
        ).play

      [winner, board]
    end

    def self.state winner
      winner.nil? ? :tied : :won
    end
  end
end
