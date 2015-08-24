# -*- encoding : utf-8 -*-

module TicTacToe
  module Strategists
    class Learning
      class Historian
        DEFAULTS = {
        }

        def initialize args = { }
          args = DEFAULTS.merge args

          args
        end
      end
    end
  end
end
