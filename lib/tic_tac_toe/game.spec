# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'
require 'tic_tac_toe/game'
require 'tic_tac_toe/player'

module TicTacToe
  Class Game do
    let(:args) do
      {
        board:    Board.new,
        player_1: player_1,
        player_2: player_2
      }
    end

    let(:player_1) { Player.new(name: player_1_name) }
    let(:player_2) { Player.new(name: player_2_name) }

    let(:player_1_name) { 'Tom' }
    let(:player_2_name) { 'John' }

    RespondsTo :new do
      ByReturning 'a new Game' do
        subject.new(args).must_be_instance_of Game
      end
    end

    Instance do
      subject { Game.new args }

      RespondsTo :play do
        ByReturning nil do
          subject.play.must_be_same_as player_1
        end
      end
    end
  end
end
