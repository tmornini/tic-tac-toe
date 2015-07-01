# -*- encoding : utf-8 -*-

require 'tic_tac_toe/cell'

module TicTacToe
  class Triplet
    def initialize args
      @cell_0 = args[:cell_0]
      @cell_1 = args[:cell_1]
      @cell_2 = args[:cell_2]
    end

    def has_winner?
      return nil if @cell_0 == Cell || @cell_1 == Cell || @cell_2 == Cell

      return @cell_0 if @cell_0 == @cell_1 && @cell_1 == @cell_2

      nil
    end

    def to_s
      "| #{@cell_0} | #{@cell_1} | #{@cell_2} |"
    end
  end
end
