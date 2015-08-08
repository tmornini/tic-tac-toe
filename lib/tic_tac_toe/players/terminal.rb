# -*- encoding : utf-8 -*-

module TicTacToe
  module Players
    class Terminal
      def initialize args
        @name = args[:name]
        @side = args[:side]
        @cell = Cell.new(player: self, side: @side)
      end

      def to_s
        "name: #{@name}, side: #{@side}"
      end

      DEFAULTS = {
        kernel: Kernel
      }

      def make_move_on args
        args = DEFAULTS.merge args

        args[:kernel].puts args[:board]

        interact_with_terminal args

        @cell
      end

      private

      def interact_with_terminal args
        kernel = args[:kernel]

        loop do
          begin
            break if move_is_successful? args

            kernel.puts 'Space occupied. Try again, dumbass.'
          rescue ArgumentError
            kernel.puts 'Input out of bounds. Nice job.'
          end
        end
      end

      def move_is_successful? args
        args[:board].put_cell_at choose_square(args).merge(cell: @cell)
      end

      def choose_square args
        kernel = args[:kernel]

        kernel.puts 'Please select a move.'

        kernel.print 'x-position (0, 1, or 2): '
        x = kernel.gets.chomp.to_i

        kernel.print 'y-position (0, 1, or 2): '
        y = kernel.gets.chomp.to_i

        {
          x: x,
          y: y
        }
      end
    end
  end
end
