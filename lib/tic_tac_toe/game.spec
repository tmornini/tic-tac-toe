# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'
require 'tic_tac_toe/game'

require 'tic_tac_toe/players/random'

# rubocop:disable Metrics/ModuleLength

module TicTacToe
  Class Game do
    let(:args) do
      {
        board:    board,
        x_player: x_player,
        o_player: o_player
      }
    end

    let(:board) { Board.new }

    let(:x_player) { Players::Random.new name: x_player_name, side: :x }
    let(:o_player) { Players::Random.new name: o_player_name, side: :o }

    let(:x_player_name) { 'Tom' }
    let(:o_player_name) { 'John' }

    let(:x_cell) do
      Cell.new(
        player: x_player,
        side:   :x
      )
    end

    let(:o_cell) do
      Cell.new(
        player: o_player,
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
          let(:board) do
            b = Board.new

            b.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    0
            )

            b.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    1
            )

            b.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    2
            )

            b
          end

          ByReturning 'the winning Player' do
            subject.play.must_be_instance_of Players::Random
          end
        end

        When 'the game is a tie' do
          ByReturning nil do
            board.put_cell_at(
              cell: o_cell,
              x:    0,
              y:    0
            )

            board.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    1
            )

            board.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    2
            )

            board.put_cell_at(
              cell: x_cell,
              x:    1,
              y:    0
            )

            board.put_cell_at(
              cell: o_cell,
              x:    1,
              y:    1
            )

            board.put_cell_at(
              cell: o_cell,
              x:    1,
              y:    2
            )

            board.put_cell_at(
              cell: o_cell,
              x:    2,
              y:    0
            )

            board.put_cell_at(
              cell: x_cell,
              x:    2,
              y:    1
            )

            board.put_cell_at(
              cell: x_cell,
              x:    2,
              y:    2
            )

            subject.play.must_be_nil
          end
        end
      end
    end
  end
end
