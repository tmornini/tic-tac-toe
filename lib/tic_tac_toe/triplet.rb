# -*- encoding : utf-8 -*-

module TicTacToe
  class Triplet
    def initialize args
      @cell_0 = args[:cell_0]
      @cell_1 = args[:cell_1]
      @cell_2 = args[:cell_2]
    end

    def to_s
      "| #{@cell_0} | #{@cell_1} | #{@cell_2} |"
    end
  end
end
