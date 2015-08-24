# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'

require 'tic_tac_toe/strategists/random'

module TicTacToe
  module Strategists
    Class Random do
      let(:args) do
        {
          kernel: kernel
        }
      end

      let(:kernel) { double 'kernel' }

      RespondsTo :new do
        ByReturning 'a new Random Strategist' do
          subject.new(args).must_be_instance_of Random
        end
      end

      Instance do
        subject { Random.new args }

        RespondsTo :choose_location do
          let(:move_args) do
            {
              board: :board
            }
          end

          ByReturning 'Board cell coordinates' do
            expect(kernel)
              .to receive(:rand)
              .with(3)
              .and_return(:x)

            expect(kernel)
              .to receive(:rand)
              .with(3)
              .and_return(:y)

            subject.choose_location(move_args).must_equal x: :x,
                                                          y: :y
          end
        end
      end
    end
  end
end
