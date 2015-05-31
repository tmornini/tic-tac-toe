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
      puts "board:"
      puts @board
      puts "player_1: #{@player_1}"
      puts "player_2: #{@player_2}"
      puts 'Shall we play?'
    end
  end

  class Board
    def initialize
      @cells = [ [ ' ', ' ', ' ' ],
                 [ ' ', ' ', ' ' ],
                 [ ' ', ' ', ' ' ] ]
    end

    def cell_is_an_x x, y
      @cells[x][y] = 'x'
    end

    def cell_is_an_o x, y
      @cells[x][y] = 'o'
    end

    def to_s
      "-------\n"                                           \
      "|#{@cells[0][0]}|#{@cells[1][0]}|#{@cells[2][0]}|\n" \
      "-------\n"                                           \
      "|#{@cells[0][1]}|#{@cells[1][1]}|#{@cells[2][1]}|\n" \
      "-------\n"                                           \
      "|#{@cells[0][2]}|#{@cells[1][2]}|#{@cells[2][2]}|\n" \
      "-------\n"
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

  board = Board.new

  board.cell_is_an_o 1, 1

  Game.new(board, Player.new('Tom'), Player.new('John')).play
end
