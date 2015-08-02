# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/cell'

require 'tic_tac_toe/players/random'

module TicTacToe
  Class Cell do
    let(:args) do
      {
        player: player,
        side:   side
      }
    end

    let(:player) { Players::Random.new name: player_name, side: side }

    let(:player_name) { 'Tom' }
    let(:side)        { :x }

    RespondsTo :new do
      ByReturning 'a new Cell' do
        subject.new(args).must_be_instance_of Cell
      end
    end

    RespondsTo :to_s do
      ByReturning 'a space' do
        subject.to_s.must_equal ' '
      end
    end

    Instance do
      subject { Cell.new args }

      RespondsTo :to_s do
        When 'player is on side :x' do
          ByReturning 'an X' do
            subject.to_s.must_equal 'X'
          end
        end

        When 'player is on side :o' do
          let(:side) { :o }

          ByReturning 'an O' do
            subject.to_s.must_equal 'O'
          end
        end
      end
    end
  end
end
