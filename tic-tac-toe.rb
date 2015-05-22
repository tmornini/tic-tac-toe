#!/usr/bin/env ruby
# -*- encoding : utf-8 -*-

puts 'Welcome to Tic-Tac-Toe!'

module TicTacToe
  class Game
    def initialize board, player_1, player_2
      @board    = board
      @player_1 = player_1
      @player_2 = player_2
    end

    def play
      puts 'Shall we play?'
    end
  end
end

board    = nil
player_1 = nil
player_2 = nil

a_game = TicTacToe::Game.new board, player_1, player_2
b_game = TicTacToe::Game.new 'board', 'player_1', 'player_2'

puts a_game
puts b_game

a_game.play
