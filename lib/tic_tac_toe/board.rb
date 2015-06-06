# -*- encoding : utf-8 -*-

module TicTacToe
  class Board
    def initialize
      @cells = [ [ ' ', ' ', ' ' ],
                 [ ' ', ' ', ' ' ],
                 [ ' ', ' ', ' ' ] ]
    end

    def cell_is_an_x x, y
      @cells[x][y] = 'x'
    end

    def cell_is_an_o x, y
      @cells[x][y] = 'o'
    end

    def to_s
      "-------\n"                                           \
      "|#{@cells[0][0]}|#{@cells[1][0]}|#{@cells[2][0]}|\n" \
      "-------\n"                                           \
      "|#{@cells[0][1]}|#{@cells[1][1]}|#{@cells[2][1]}|\n" \
      "-------\n"                                           \
      "|#{@cells[0][2]}|#{@cells[1][2]}|#{@cells[2][2]}|\n" \
      "-------\n"
    end
  end
end
