require 'socket'

server = TCPServer.new 2000
pids = []
loop do
  Thread.start(server.accept) do |client|
    p [Thread.current]
    headers = []
    while header = client.gets
      break if header.chomp.empty?
      headers << header.chomp
    end
    p [Thread.current, headers]

    client.puts "HTTP/1.0 200 OK"
    client.puts "Content-Type: text/plain"
    client.puts
    client.puts "message body"
    client.close
  end
end
