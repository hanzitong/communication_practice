
#include <iostream>
#include <boost/asio.hpp>


using boost::asio::ip::udp;

int main(int argc, char* argv[]){
    try {
        boost::asio::io_context io_context;

        udp::socket socket(io_context, udp::endpoint(udp::v4(), 0));
        udp::endpoint receiver_endpoint(boost::asio::ip::make_address("192.168.3.6"), 12345);

        std::string message = "hello world";
        socket.send_to(boost::asio::buffer(message), receiver_endpoint);

    }
    catch (std::exception& e) {
        std::cerr << e.what() << std::endl;
    }


    return 0;
}

