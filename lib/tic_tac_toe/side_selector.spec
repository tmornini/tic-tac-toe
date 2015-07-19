# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/side_selector'

module TicTacToe
  Module SideSelector do
    let(:args) do
      {
        random_klass:   random_klass,
        player_details: [
          player_1_details,
          player_2_details
        ]
      }
    end

    let(:player_1_details) do
      {
        name:  player_1_name,
        klass: player_1_klass
      }
    end

    let(:player_2_details) do
      {
        name:  player_2_name,
        klass: player_2_klass
      }
    end

    let(:random_klass) { double 'random_klass' }

    let(:player_1_name)  { :player_1_name          }
    let(:player_1_klass) { double 'player_1_klass' }

    let(:player_2_name)  { :player_2_name          }
    let(:player_2_klass) { double 'player_2_klass' }

    RespondsTo :select do
      When 'player 1 wins the coin flip' do
        ByReturning nil do
          expect(random_klass)
            .to receive(:random_number)
            .with(2)
            .and_return(0)

          expect(player_1_klass)
            .to receive(:new)
            .with(player_1_details.merge side: :x)
            .and_return(:x_player)

          expect(player_2_klass)
            .to receive(:new)
            .with(player_2_details.merge side: :o)
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

          expect(player_2_klass)
            .to receive(:new)
            .with(player_2_details.merge side: :x)
            .and_return(:x_player)

          expect(player_1_klass)
            .to receive(:new)
            .with(player_1_details.merge side: :o)
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
