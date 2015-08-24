# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'
require 'tic_tac_toe/game'
require 'tic_tac_toe/player'

module TicTacToe
  Class Game do
    let(:args) do
      {
        board:    board,
        x_player: x_player,
        o_player: o_player
      }
    end

    let(:board) { double 'board' }

    let(:x_player) { double 'x_player' }
    let(:o_player) { double 'y_player' }

    let(:x_player_name) { 'Tom' }
    let(:o_player_name) { 'John' }

    let(:x_cell) do
      Cell.new(
        side:   :x
      )
    end

    let(:o_cell) do
      Cell.new(
        side:   :o
      )
    end

    RespondsTo :new do
      ByReturning 'a new Game' do
        subject.new(args).must_be_instance_of Game
      end
    end

    Instance do
      subject { Game.new args }

      RespondsTo :play do
        When 'there is a winner' do
          ByReturning 'the winning Player' do
            expect(x_player)
              .to receive(:make_move_on)
              .with(board: board)
              .and_return(x_player)

            expect(board)
              .to receive(:has_winner?)
              .and_return(true)

            subject.play.must_be_same_as x_player
          end
        end

        When 'the game is a tie' do
          ByReturning nil do
            expect(x_player)
              .to receive(:make_move_on)
              .with(board: board)
              .and_return(x_player)

            expect(board)
              .to receive(:has_winner?)
              .and_return(false)

            expect(board)
              .to receive(:is_tied?)
              .and_return(true)

            subject.play.must_be_nil
          end
        end
      end
    end
  end
end
