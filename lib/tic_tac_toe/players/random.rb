# -*- encoding : utf-8 -*-

module TicTacToe
  module Players
    class Random
      def initialize args
        @name = args[:name]
        @side = args[:side]
        @cell = Cell.new(player: self, side: @side)
      end

      def to_s
        "name: #{@name}, side: #{@side}"
      end

      def make_move_on args
        board = args[:board]

        loop do
          break if board.put_cell_at cell: @cell,
                                     x:    rand(3),
                                     y:    rand(3)
        end

        @cell
      end
    end
  end
end
