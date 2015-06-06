# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'
require 'tic_tac_toe/game'
require 'tic_tac_toe/player'

module TicTacToe
  Class Game do
    board = Board.new

    board.cell_is_an_o 1, 1

    Game.new(board, Player.new('Tom'), Player.new('John')).play
  end
end
