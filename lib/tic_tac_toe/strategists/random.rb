# -*- encoding : utf-8 -*-

module TicTacToe
  module Strategists
    class Random
      DEFAULTS = {
        kernel: Kernel
      }

      def initialize args = { }
        args = DEFAULTS.merge args

        @kernel = args[:kernel]
      end

      def choose_location _args_
        {
          x: @kernel.rand(3),
          y: @kernel.rand(3)
        }
      end
    end
  end
end
