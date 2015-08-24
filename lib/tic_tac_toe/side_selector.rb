# -*- encoding : utf-8 -*-

require 'securerandom'

require 'tic_tac_toe/cell'
require 'tic_tac_toe/player'

module TicTacToe
  module SideSelector
    DEFAULTS = {
      random_klass: SecureRandom,

      cell_klass:   Cell,
      player_klass: Player
    }

    def self.select args
      args = DEFAULTS.merge args

      x_player_index = args[:random_klass].random_number(2)
      o_player_index = 1 - x_player_index

      {
        x_player: make_x_player(args, x_player_index),
        o_player: make_o_player(args, o_player_index)
      }
    end

    private

    def self.player_args player_details, cell
      player_details.merge cell: cell
    end

    def self.make_player args, player_index, cell
      player_details = args[:player_details][player_index]

      args[:player_klass].new player_args(player_details, cell)
    end

    def self.make_cell args, side
      args[:cell_klass].new side: side
    end

    def self.make_x_player args, x_player_index
      make_player args, x_player_index, make_cell(args, :x)
    end

    def self.make_o_player args, o_player_index
      make_player args, o_player_index, make_cell(args, :o)
    end
  end
end
