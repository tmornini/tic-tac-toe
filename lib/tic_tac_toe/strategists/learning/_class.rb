# -*- encoding : utf-8 -*-

require 'tic_tac_toe/strategists/learning/historian'
require 'tic_tac_toe/strategists/learning/move_maker'
require 'tic_tac_toe/strategists/learning/win_recorder'
require 'tic_tac_toe/strategists/learning/loss_recorder'

module TicTacToe
  module Strategists
    class Learning
      DEFAULTS = {
        random:        Random,

        historian:     Historian,
        move_remaker:  MoveMaker,
        win_recorder:  WinRecorder,
        loss_recorder: LossRecorder
      }

      def initialize args = { }
        args = DEFAULTS.merge args

        @random = args[:random]

        @historian     = args[:historian]
        @move_maker    = args[:move_remaker]
        @win_recorder  = args[:win_recorder]
        @loss_recorder = args[:loss_recorder]
      end

      def choose_location _args_
        # Check board history for match, remake move with highest win count
        @historian.check_for_match(args)
        # If there isn't a match, make a random move
        # If random move is a winner, increase all previous moves'
        # winner count by 1
        # If random move is a loser, increase all previous moves'
        # loser count by 1
        {
          x: 1,
          y: 1
        }
      end
    end
  end
end
