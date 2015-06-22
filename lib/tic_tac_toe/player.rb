# -*- encoding : utf-8 -*-

module TicTacToe
  class Player
    def initialize args
      @name = args[:name]
      @side = args[:side]
      @cell = Cell.new(side: self)
    end

    def to_s
      "name: #{@name}, side: #{@side}"
    end

    def x?
      @side == :x
    end

    def make_move_on args
      board = args[:board]

      board.put_cell_at cell: @cell,
                        x:    rand(3),
                        y:    rand(3)
    end
  end
end
