# -*- encoding : utf-8 -*-

module TicTacToe
  module Players
    class Terminal
      def initialize args
        @name = args[:name]
        @side = args[:side]
        @cell = Cell.new(player: @player, side: @side)
      end

      def to_s
        "name: #{@name}, side: #{@side}"
      end

      def make_move_on args
        board = args[:board]

        loop do
          puts board

          break if board.put_cell_at choose_square.merge cell: @cell
        end

        @cell
      end

      private

      def choose_square
        {
          x: gets.chomp.to_i,
          y: gets.chomp.to_i
        }
      end
    end
  end
end
