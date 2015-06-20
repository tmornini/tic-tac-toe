# -*- encoding : utf-8 -*-

require 'tic_tac_toe/triplet'

module TicTacToe
  class Board
    def initialize
      @cells = [ [ Cell, Cell, Cell ],
                 [ Cell, Cell, Cell ],
                 [ Cell, Cell, Cell ] ]
    end

    def put_cell_at args
      @cells[args[:x]][args[:y]] = args[:cell]
    end

    def to_s
      "-------------\n"   \
        "#{row_0}\n"      \
        "|---+---+---|\n" \
        "#{row_1}\n"      \
        "|---+---+---|\n" \
        "#{row_2}\n"      \
        '-------------'
    end

    private

    def row_0
      Triplet.new cell_0: @cells[0][2],
                  cell_1: @cells[1][2],
                  cell_2: @cells[2][2]
    end

    def row_1
      Triplet.new cell_0: @cells[0][1],
                  cell_1: @cells[1][1],
                  cell_2: @cells[2][1]
    end

    def row_2
      Triplet.new cell_0: @cells[0][0],
                  cell_1: @cells[1][0],
                  cell_2: @cells[2][0]
    end

    def column_0
      Triplet.new cell_0: @cells[0][2],
                  cell_1: @cells[0][1],
                  cell_2: @cells[0][0]
    end

    def column_1
      Triplet.new cell_0: @cells[1][2],
                  cell_1: @cells[1][1],
                  cell_2: @cells[1][0]
    end

    def column_2
      Triplet.new cell_0: @cells[2][2],
                  cell_1: @cells[2][1],
                  cell_2: @cells[2][0]
    end

    def diagonal_0
      Triplet.new cell_0: @cells[0][2],
                  cell_1: @cells[1][1],
                  cell_2: @cells[2][0]
    end

    def diagonal_1
      Triplet.new cell_0: @cells[0][0],
                  cell_1: @cells[1][1],
                  cell_2: @cells[2][2]
    end
  end
end
