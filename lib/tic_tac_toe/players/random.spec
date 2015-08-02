# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'

require 'tic_tac_toe/players/random'

module TicTacToe
  module Players
    Class Random do
      let(:args) do
        {
          name: player_name,
          side: side
        }
      end

      let(:player_name) { 'Tom' }
      let(:side)        { :x }

      RespondsTo :new do
        ByReturning 'a new Random Player' do
          subject.new(args).must_be_instance_of Random
        end
      end

      Instance do
        subject { Random.new args }

        RespondsTo :to_s do
          ByReturning 'the Players name' do
            subject.to_s.must_equal "name: #{player_name}, side: #{side}"
          end
        end

        RespondsTo :make_move_on do
          let(:move_args) do
            {
              board: Board.new
            }
          end

          ByReturning 'a Cell' do
            subject.make_move_on(move_args).must_be_instance_of Cell
          end
        end
      end
    end
  end
end
