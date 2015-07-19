# -*- encoding : utf-8 -*-

require 'securerandom'

module TicTacToe
  module SideSelector
    DEFAULTS = {
      random_klass: SecureRandom
    }

    def self.select args
      args = DEFAULTS.merge args

      player_details = args[:player_details]

      x_player_position = args[:random_klass].random_number(2)

      x_player_details = player_details[x_player_position].merge side: :x
      o_player_details = player_details[1 - x_player_position].merge side: :o

      {
        x_player: x_player_details[:klass].new(x_player_details),
        o_player: o_player_details[:klass].new(o_player_details)
      }
    end
  end
end
