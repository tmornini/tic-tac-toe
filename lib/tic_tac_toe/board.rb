# -*- encoding : utf-8 -*-

require 'tic_tac_toe/triplet'

module TicTacToe
  class Board
    def initialize
      @cells = [ [ ' ', ' ', ' ' ],
                 [ ' ', ' ', ' ' ],
                 [ ' ', ' ', ' ' ] ]
    end

    def set args
      @cells[args[:x]][args[:y]] = args[:to]
    end

    def to_s
      "-------\n"  +
        row_0.to_s +
        row_1.to_s +
        row_2.to_s +
        "-------\n"
    end

    private

    def row_0
      Triplet.new @cells[0][2], @cells[1][2], @cells[2][2]
    end

    def row_1
      Triplet.new @cells[0][1], @cells[1][1], @cells[2][1]
    end

    def row_2
      Triplet.new @cells[0][0], @cells[1][0], @cells[2][0]
    end

    def column_0
      Triplet.new @cells[0][2], @cells[0][1], @cells[0][0]
    end

    def column_1
      Triplet.new @cells[1][2], @cells[1][1], @cells[1][0]
    end

    def column_2
      Triplet.new @cells[2][2], @cells[2][1], @cells[2][0]
    end

    def diagonal_0
      Triplet.new @cells[0][2], @cells[1][1], @cells[2][0]
    end

    def diagonal_1
      Triplet.new @cells[0][0], @cells[1][1], @cells[2][2]
    end
  end
end