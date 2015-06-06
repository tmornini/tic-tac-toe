# -*- encoding : utf-8 -*-

clearing :on

require 'guard/compat/plugin'

# rubocop:disable all
module ::Guard
# rubocop:enable all
  class Subledger < Plugin
    def initialize _options_ = { }
      super
    end

    def start
      # run_all
      true
    end

    def stop
      system 'rake clean'
      true
    end

    def reload
      exec 'bundle exec rake guard'
    end

    def run_all
      throw_on_failed_tests { system 'rake' }
    end

    def run_on_additions _pathnames_
      true
    end

    def run_on_modifications pathnames
      pathnames.each do |pathname|
        throw_on_failed_tests do
          take_appropriate_action_for(pathname)
        end
      end

      true
    end

    def run_on_removals _pathnames_
      run_all
    end

    private

    def throw_on_failed_tests
      throw :task_has_failed unless yield
      true
    end

    def spec_helper? pathname
      pathname.match /spec_helper/
    end

    def unit_spec? pathname
      pathname !~ /^spec/
    end

    def take_appropriate_action_for pathname
      return if spec_helper? pathname

      if unit_spec? pathname
        run_unit_spec_for(pathname)
      else
        run_integration_spec_for(pathname)
      end

      run_lint_for(pathname)
    end

    def spec_file_exists_for? pathname
      File.exist? pathname
    end

    def run_unit_spec_for pathname
      spec_pathname = spec_pathname_for pathname

      if spec_file_exists_for? spec_pathname
        system "bundle exec rake spec:unit TEST=#{spec_pathname}"
      else
        puts "#{pathname} is missing spec #{spec_pathname}"
      end
    end

    def run_integration_spec_for pathname
      system 'bundle exec rake spec:integration ' \
             "TEST=#{spec_pathname_for pathname}"
    end

    def spec_pathname_for pathname
      return pathname if pathname.match /[.]spec$/
      spec_pathname_prefix_for(pathname) + '.spec'
    end

    def spec_pathname_prefix_for pathname
      pathname.match(
        %r{^(lib/(.+/)?[^/]+)[.](rb|spec)$}
      )[1]
    end

    def run_lint_for pathname
      system "bundle exec rake lint:file TEST=#{pathname}"
    end
  end
end

guard :subledger do
  watch 'Gemfile' do
    system 'bundle update'

    nil
  end

  watch %r{lib/(.+)[.](rb|spec)$}
end
