# -*- encoding : utf-8 -*-

module TicTacToe
  class Triplet
    def initialize cell_0, cell_1, cell_2
      @cell_0 = cell_0
      @cell_1 = cell_1
      @cell_2 = cell_2
    end

    def to_s
      "| #{@cell_0} | #{@cell_1} | #{@cell_2} |"
    end
  end
end
