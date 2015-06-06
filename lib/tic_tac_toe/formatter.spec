# -*- encoding : utf-8 -*-

require '_spec/_helpers'

require 'tic_tac_toe/formatter'

module TicTacToe
  Module Formatter do
    RespondsTo :format do
      ByReturning 'a nicely formatted string' do
        subject.format({ }).must_equal '{}'
      end
    end
  end
end
