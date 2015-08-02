# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'
require 'tic_tac_toe/cell'

require 'tic_tac_toe/players/random'

# rubocop:disable Metrics/ModuleLength

module TicTacToe
  Class Board do
    RespondsTo :new do
      ByReturning 'a new Board' do
        subject.new.must_be_instance_of Board
      end
    end

    Instance do
      subject { Board.new }

      let(:x_player) do
        Players::Random.new(
          name: x_player_name,
          side: :x
        )
      end

      let(:o_player) do
        Players::Random.new(
          name: o_player_name,
          side: :o
        )
      end

      let(:x_player_name) { 'Tom' }
      let(:o_player_name) { 'John' }

      let(:x)      { 1 }
      let(:y)      { 1 }

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

      RespondsTo :put_cell_at do
        When 'the cell is occupied' do
          ByReturning 'the :cell parameter' do
            subject.put_cell_at(
              cell: x_cell,
              x:    x,
              y:    y
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    x,
              y:    y
            ).must_be_nil
          end
        end

        When 'the cell is empty' do
          ByReturning 'the :cell parameter' do
            subject.put_cell_at(
              cell: x_cell,
              x:    x,
              y:    y
            ).must_equal x_cell
          end
        end
      end

      RespondsTo :has_winner? do
        When 'there is no winner' do
          ByReturning false do
            subject.has_winner?.must_equal false
          end
        end

        When 'there is a winner' do
          ByReturning true do
            subject.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    0
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    1
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    2
            )

            subject.has_winner?.must_equal true
          end
        end
      end

      RespondsTo :is_tied? do
        When 'the board is tied' do
          ByReturning true do
            subject.put_cell_at(
              cell: o_cell,
              x:    0,
              y:    0
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    1
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    0,
              y:    2
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    1,
              y:    0
            )

            subject.put_cell_at(
              cell: o_cell,
              x:    1,
              y:    1
            )

            subject.put_cell_at(
              cell: o_cell,
              x:    1,
              y:    2
            )

            subject.put_cell_at(
              cell: o_cell,
              x:    2,
              y:    0
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    2,
              y:    1
            )

            subject.put_cell_at(
              cell: x_cell,
              x:    2,
              y:    2
            )

            subject.is_tied?.must_equal true
          end
        end

        When 'the board is not tied' do
          ByReturning false do
            subject.is_tied?.must_equal false
          end
        end
      end

      RespondsTo :to_s do
        ByReturning 'an ASCII formatted Board' do
          subject.to_s.must_equal "-------------\n" \
                                  "|   |   |   |\n" \
                                  "|---+---+---|\n" \
                                  "|   |   |   |\n" \
                                  "|---+---+---|\n" \
                                  "|   |   |   |\n" \
                                  '-------------'
        end
      end
    end
  end
end
