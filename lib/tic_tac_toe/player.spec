# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/player'

module TicTacToe
  Class Player do
    let(:args) do
      {
        name: player_name
      }
    end

    let(:player_name) { 'Tom' }

    RespondsTo :new do
      ByReturning 'a new Player' do
        subject.new(args).must_be_instance_of Player
      end
    end

    Instance do
      subject { Player.new args }

      RespondsTo :to_s do
        ByReturning 'the Players name' do
          subject.to_s.must_equal player_name
        end
      end
    end
  end
end
