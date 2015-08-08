# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'

require 'tic_tac_toe/players/terminal'

module TicTacToe
  module Players
    Class Terminal do
      let(:args) do
        {
          name: player_name,
          side: side
        }
      end

      let(:player_name) { 'Tom' }
      let(:side)        { :x    }

      RespondsTo :new do
        ByReturning 'a new Terminal Player' do
          subject.new(args).must_be_instance_of Terminal
        end
      end

      Instance do
        subject { Terminal.new args }

        RespondsTo :to_s do
          ByReturning 'the Players name' do
            subject.to_s.must_equal "name: #{player_name}, side: #{side}"
          end
        end

        RespondsTo :make_move_on do
          let(:move_args) do
            {
              board:  board,
              kernel: kernel
            }
          end

          let(:board)  { Board.new       }
          let(:kernel) { double 'kernel' }

          ByReturning 'a Cell' do
            expect(kernel)
              .to receive(:puts)
              .with(board)

            expect(kernel)
              .to receive(:puts)
              .with('Please select a move.')

            expect(kernel)
              .to receive(:print)
              .with('x-position (0, 1, or 2): ')

            expect(kernel)
              .to receive(:print)
              .with('y-position (0, 1, or 2): ')

            expect(kernel)
              .to receive(:gets)
              .exactly(2).times
              .and_return('1')

            subject.make_move_on(move_args).must_be_instance_of Cell
          end
        end
      end
    end
  end
end