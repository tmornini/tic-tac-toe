# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/cell'
require 'tic_tac_toe/player'

module TicTacToe
  Class Cell do
    let(:args) do
      {
        x:      x,
        y:      y,
        player: player
      }
    end

    let(:x)      { 1 }
    let(:y)      { 1 }
    let(:player) { Player.new name: player_name }

    let(:player_name) { 'Tom' }

    RespondsTo :new do
      ByReturning 'a new Cell' do
        subject.new(args).must_be_instance_of Cell
      end
    end

    Instance do
      subject { Cell.new }

      RespondsTo :to_s do
        ByReturning 'a String'
      end
    end
  end
end
