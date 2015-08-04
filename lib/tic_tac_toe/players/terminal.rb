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

      DEFAULTS = {
        kernel: Kernel
      }

      def make_move_on args
        args = DEFAULTS.merge args

        kernel = args[:kernel]

        board = args[:board]

        loop do
          kernel.puts board

          break if board.put_cell_at choose_square(args).merge cell: @cell

          kernel.puts 'Space occupied. Try again, dumbass.'
        end

        @cell
      end

      private

      def choose_square args
        kernel = args[:kernel]

        kernel.puts 'Please select a move.'

        {
          x: kernel.gets.chomp.to_i,
          y: kernel.gets.chomp.to_i
        }
      end
    end
  end
end
