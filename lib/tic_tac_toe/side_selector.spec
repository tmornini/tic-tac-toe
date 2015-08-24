# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/side_selector'

module TicTacToe
  Module SideSelector do
    let(:args) do
      {
        random_klass:   random_klass,

        cell_klass:     cell_klass,
        player_klass:   player_klass,
        player_details: [
          player_1_details,
          player_2_details
        ]
      }
    end

    let(:random_klass) { double 'random_klass' }

    let(:cell_klass)   { double 'cell_klass'   }
    let(:player_klass) { double 'player_klass' }

    let(:player_1_details) do
      {
        name:       player_1_name,
        strategist: player_1_strategist
      }
    end

    let(:player_2_details) do
      {
        name:       player_2_name,
        strategist: player_2_strategist
      }
    end

    let(:player_1_name)       { :player_1_name               }
    let(:player_1_strategist) { double 'player_1_strategist' }

    let(:player_2_name)       { :player_2_name               }
    let(:player_2_strategist) { double 'player_2_strategist' }

    RespondsTo :select do
      When 'player 1 wins the coin flip' do
        ByReturning nil do
          expect(random_klass)
            .to receive(:random_number)
            .with(2)
            .and_return(0)

          expect(cell_klass)
            .to receive(:new)
            .with(side: :x)
            .and_return(:x_cell)

          expect(player_klass)
            .to receive(:new)
            .with(player_1_details.merge cell: :x_cell)
            .and_return(:x_player)

          expect(cell_klass)
            .to receive(:new)
            .with(side: :o)
            .and_return(:o_cell)

          expect(player_klass)
            .to receive(:new)
            .with(player_2_details.merge cell: :o_cell)
            .and_return(:o_player)

          subject.select(args).must_equal(
            x_player: :x_player,
            o_player: :o_player
          )
        end
      end

      When 'player 2 wins the coin flip' do
        ByReturning nil do
          expect(random_klass)
            .to receive(:random_number)
            .with(2)
            .and_return(1)

          expect(cell_klass)
            .to receive(:new)
            .with(side: :x)
            .and_return(:x_cell)

          expect(player_klass)
            .to receive(:new)
            .with(player_2_details.merge cell: :x_cell)
            .and_return(:x_player)

          expect(cell_klass)
            .to receive(:new)
            .with(side: :o)
            .and_return(:o_cell)

          expect(player_klass)
            .to receive(:new)
            .with(player_1_details.merge cell: :o_cell)
            .and_return(:o_player)

          subject.select(args).must_equal(
            x_player: :x_player,
            o_player: :o_player
          )
        end
      end
    end
  end
end
