# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/board'

require 'tic_tac_toe/strategists/terminal'

module TicTacToe
  module Strategists
    Class Terminal do
      let(:args) do
        {
          board:  :board,
          kernel: kernel
        }
      end

      let(:kernel) { double 'kernel' }

      RespondsTo :new do
        ByReturning 'a new Terminal Strategist' do
          subject.new.must_be_instance_of Terminal
        end
      end

      Instance do
        subject { Terminal.new args }

        RespondsTo :choose_location do
          ByReturning 'Board cell coordinates' do
            expect(kernel)
              .to receive(:puts)
              .with(:board)

            expect(kernel)
              .to receive(:puts)
              .with('Please select a move.')

            expect(kernel)
              .to receive(:print)
              .with('x-position (0, 1, or 2): ')

            expect(kernel)
              .to receive(:print)
              .with('y-position (0, 1, or 2): ')

            expect(kernel)
              .to receive(:gets)
              .exactly(2).times
              .and_return('1')

            response = subject.choose_location(args)

            response.must_be_instance_of Hash

            response.key?(:x).must_equal true
            response.key?(:y).must_equal true

            response[:x].must_be_instance_of Fixnum
            response[:y].must_be_instance_of Fixnum
          end
        end
      end
    end
  end
end
