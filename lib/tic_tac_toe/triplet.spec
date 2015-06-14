# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/triplet'

module TicTacToe
  Class Triplet do
    let(:args) do
      {
        cell_0: cell_0,
        cell_1: cell_1,
        cell_2: cell_2
      }
    end

    let(:cell_0) { ' ' }
    let(:cell_1) { ' ' }
    let(:cell_2) { ' ' }

    RespondsTo :new do
      ByReturning 'a new Player' do
        subject.new(args).must_be_instance_of Triplet
      end
    end

    Instance do
      subject { Triplet.new args }

      RespondsTo :to_s do
        ByReturning 'the Players name' do
          subject.to_s.must_equal "| #{cell_0} | #{cell_1} | #{cell_2} |"
        end
      end
    end
  end
end
