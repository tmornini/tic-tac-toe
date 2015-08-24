# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'

require 'tic_tac_toe/player'

module TicTacToe
  Class Player do
    let(:args) do
      {
        cell:       cell,
        name:       :name,
        strategist: strategist
      }
    end

    let(:cell)       { double 'cell' }
    let(:strategist) { double 'strategist' }

    let(:cell_instance) { double 'cell_instance' }

    RespondsTo :new do
      ByReturning 'a new Player' do
        subject.new(args).must_be_instance_of Player
      end
    end

    Instance do
      subject { Player.new args }

      RespondsTo :to_s do
        ByReturning 'the Players name' do
          subject.to_s.must_equal 'name: name'
        end
      end

      RespondsTo :make_move_on do
        let(:move_args) do
          {
            board: board
          }
        end

        let(:board) { Board.new }

        ByReturning 'a Cell' do
          expect(strategist)
            .to receive(:choose_location)
            .with(
              board: board
            )
            .and_return(
              x: 1,
              y: 1
            )

          subject.make_move_on(move_args).must_equal cell
        end
      end
    end
  end
end
