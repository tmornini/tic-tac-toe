# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/cell'
require 'tic_tac_toe/player'

module TicTacToe
  Class Cell do
    let(:args) do
      {
        side: side
      }
    end

    let(:side) { :x }

    let(:player) { Player.new name: player_name }

    let(:player_name) { 'Tom' }

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
        When 'the cell is on side :x' do
          ByReturning 'an X' do
            subject.to_s.must_equal 'X'
          end
        end

        When 'the cell is on side :o' do
          let(:side) { :o }

          ByReturning 'an O' do
            subject.to_s.must_equal 'O'
          end
        end
      end
    end
  end
end
