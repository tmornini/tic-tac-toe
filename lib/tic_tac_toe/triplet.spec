# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/player'
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

    let(:cell_0) { Cell }
    let(:cell_1) { Cell }
    let(:cell_2) { Cell }

    RespondsTo :new do
      ByReturning 'a new Player' do
        subject.new(args).must_be_instance_of Triplet
      end
    end

    Instance do
      subject { Triplet.new args }

      RespondsTo :has_winner? do
        When 'a cell is empty' do
          ByReturning nil do
            subject.has_winner?.must_be_nil
          end
        end

        When 'at least one cell is filled and all cells are the same' do
          let(:cell_0) { x_cell }
          let(:cell_1) { x_cell }
          let(:cell_2) { x_cell }

          let(:x_cell)   { Cell.new player: x_player, side: :x }
          let(:x_player) { Player.new name: 'Bob', side: :x }

          ByReturning 'a winning Cell' do
            subject.has_winner?.must_be_instance_of Cell
          end
        end

        When 'all cells are filled and all cells are not the same' do
          let(:cell_0) { x_cell }
          let(:cell_1) { o_cell }
          let(:cell_2) { o_cell }

          let(:x_cell)   { Cell.new player: x_player, side: :x }
          let(:x_player) { Player.new name: 'Bob', side: :x }
          let(:o_cell)   { Cell.new player: o_player, side: :o }
          let(:o_player) { Player.new name: 'Cindy', side: :o }

          ByReturning nil do
            subject.has_winner?.must_be_nil
          end
        end
      end

      RespondsTo :to_s do
        ByReturning 'the Players name' do
          subject.to_s.must_equal '|   |   |   |'
        end
      end
    end
  end
end
