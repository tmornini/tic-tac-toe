# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'
require 'tic_tac_toe/game'
require 'tic_tac_toe/player'

module TicTacToe
  Class Game do
    board = Board.new

    board.set x:  1,
              y:  1,
              to: 'X'

    Game.new(board, Player.new('Tom'), Player.new('John')).play
  end
end
