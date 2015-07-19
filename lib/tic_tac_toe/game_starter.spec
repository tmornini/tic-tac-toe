# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/game_starter'

module TicTacToe
  Module GameStarter do
    let(:args) do
      {
        board_klass:          board_klass,
        game_klass:           game_klass,
        side_selector_module: side_selector_module,
        player_details:       [
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

    let(:board_klass)          { double 'board_klass'          }
    let(:game_klass)           { double 'game_klass'           }
    let(:game)                 { double 'game'                 }
    let(:side_selector_module) { double 'side_selector_module' }

    let(:player_1_name)  { :player_1_name          }
    let(:player_1_klass) { double 'player_1_klass' }

    let(:player_2_name)  { :player_2_name          }
    let(:player_2_klass) { double 'player_2_klass' }

    RespondsTo :start do
      ByReturning nil do
        expect(side_selector_module)
          .to receive(:select)
          .with(args)
          .and_return(
            x_player: :x_player,
            o_player: :o_player
          )

        expect(board_klass)
          .to receive(:new)
          .and_return(:board)

        expect(game_klass)
          .to receive(:new)
          .with(
            x_player: :x_player,
            o_player: :o_player,
            board:    :board
          )
          .and_return(game)

        expect(game)
          .to receive(:play)
          .and_return(:winner)

        subject.start(args).must_equal(
          state:  :won,
          winner: :winner,
          board:  :board
        )
      end
    end
  end
end
