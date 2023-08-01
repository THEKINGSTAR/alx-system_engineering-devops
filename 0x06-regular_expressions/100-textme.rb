#!/usr/bin/env ruby
puts ARGV[0].scan(/\bfrom:([^\]]+)\]\s*\[to:(\+\d+)\]\s*\[flags:(.+?)\]/).join(',')
