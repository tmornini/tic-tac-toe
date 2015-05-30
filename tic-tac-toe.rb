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
      puts "board:    #{@board}"
      puts "player_1: #{@player_1}"
      puts "player_2: #{@player_2}"
      puts 'Shall we play?'
    end
  end

  class Board
    def to_s
      '-------' \
      '| | | |' \
      '-------' \
      '| | | |' \
      '-------' \
      '| | | |' \
      '-------'
    end
  end

  class Player
    def initialize name
      @name = name
    end

    def to_s
      @name
    end
  end

  Game.new(Board.new, Player.new('Tom'), Player.new('John')).play
end
