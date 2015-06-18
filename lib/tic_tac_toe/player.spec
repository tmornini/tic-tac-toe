# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/player'

module TicTacToe
  Class Player do
    let(:args) do
      {
        name: player_name,
        side: side
      }
    end

    let(:player_name) { 'Tom' }
    let(:side) { :x }

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

      RespondsTo :x? do
        When 'it is an :x' do
          ByReturning true do
            subject.x?.must_equal true
          end
        end

        When 'it is an :o' do
          let(:side) { :o }

          ByReturning false do
            subject.x?.must_equal false
          end
        end
      end
    end
  end
end
