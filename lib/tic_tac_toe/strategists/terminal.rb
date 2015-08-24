# -*- encoding : utf-8 -*-

module TicTacToe
  module Strategists
    class Terminal
      DEFAULTS = {
        kernel: Kernel
      }

      def initialize args = { }
        args = DEFAULTS.merge args

        @kernel = args[:kernel]
      end

      def choose_location args
        x, y = get_input args

        {
          x: x,
          y: y
        }
      end

      private

      def get_input args
        @kernel.puts args[:board]

        @kernel.puts 'Please select a move.'

        @kernel.print 'x-position (0, 1, or 2): '
        x = @kernel.gets.chomp.to_i

        @kernel.print 'y-position (0, 1, or 2): '
        y = @kernel.gets.chomp.to_i

        [x, y]
      end
    end
  end
end
