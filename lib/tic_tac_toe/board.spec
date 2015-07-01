# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'
require 'tic_tac_toe/cell'
require 'tic_tac_toe/player'

module TicTacToe
  Class Board do
    RespondsTo :new do
      ByReturning 'a new Board' do
        subject.new.must_be_instance_of Board
      end
    end

    Instance do
      subject { Board.new }

      let(:player) do
        Player.new(
          name: player_name,
          side: side
        )
      end

      let(:player_name) { 'Tom' }
      let(:side)        { :x }

      let(:x)      { 1 }
      let(:y)      { 1 }

      let(:cell) do
        Cell.new(
          player: player,
          side:   side
        )
      end

      RespondsTo :put_cell_at do
        When 'the cell is occupied' do
          ByReturning 'the :cell parameter' do
            subject.put_cell_at(
              cell: cell,
              x:    x,
              y:    y
            )

            subject.put_cell_at(
              cell: cell,
              x:    x,
              y:    y
            ).must_be_nil
          end
        end

        When 'the cell is empty' do
          ByReturning 'the :cell parameter' do
            subject.put_cell_at(
              cell: cell,
              x:    x,
              y:    y
            ).must_equal cell
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
              cell: cell,
              x:    0,
              y:    0
            )

            subject.put_cell_at(
              cell: cell,
              x:    0,
              y:    1
            )

            subject.put_cell_at(
              cell: cell,
              x:    0,
              y:    2
            )

            subject.has_winner?.must_equal true
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
