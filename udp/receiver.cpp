
#include <iostream>
#include <boost/asio.hpp>

using boost::asio::ip::udp;

int main(int argc, char* argv[]){
    try {
        boost::asio::io_context io_context;

        udp::socket socket(io_context, udp::endpoint(udp::v4(), 12345));

        while(true){
            char data[1024];
            udp::endpoint sender_endpoint;
            size_t length = socket.receive_from(boost::asio::buffer(data), sender_endpoint);
            std::cout.write(data, length);
            std::cout << std::endl;
        }
    }
    catch (std::exception& e) {
        std::cerr << e.what() << std::endl;
    }


    return 0;
}


