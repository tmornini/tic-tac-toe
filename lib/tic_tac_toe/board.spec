# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'

module TicTacToe
  Class Board do
    RespondsTo :new do
      ByReturning 'a new Board' do
        subject.new.must_be_instance_of Board
      end
    end

    Instance do
      subject { Board.new }

      let(:x) { 1 }
      let(:y) { 1 }

      let(:to) { 'o' }

      RespondsTo :set do
        ByReturning 'the :to parameter' do
          subject.set(
            x:  x,
            y:  y,
            to: to
          ).must_equal to
        end
      end

      RespondsTo :to_s do
        ByReturning 'a String' do
          subject.to_s.must_be_instance_of String
        end
      end
    end
  end
end
